
# import packages
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# display settings
pd.set_option('display.max_columns', None)


#read data
df_ = pd.read_csv("Case/armut_arl_recommender_system/armut_data.csv")
df = df_.copy()
df.head()

# create a unique ID for each service
df["Service"] = [str(row[1]) + "_" + str(row[2]) for row in df.values]
df.head()


# create a unique ID for each basket
df["CreateDate"] = pd.to_datetime(df["CreateDate"])
df.head()
df["NEW_DATE"] = df["CreateDate"].dt.strftime("%Y-%m")
df.head()
df["BasketID"] = [str(row[0]) + "_" + str(row[5]) for row in df.values]
df.head()

df[df["UserId"] == 7256 ]


# Create a pivot table for services and baskets like below:

# Service         0_8  10_9  11_11  12_7  13_11  14_7  15_1  16_8  17_5  18_4..
# BasketID
# 0_2017-08        0     0      0     0      0     0     0     0     0     0..
# 0_2017-09        0     0      0     0      0     0     0     0     0     0..
# 0_2018-01        0     0      0     0      0     0     0     0     0     0..
# 0_2018-04        0     0      0     0      0     1     0     0     0     0..
# 10000_2017-08    0     0      0     0      0     0     0     0     0     0..

invoice_product_df = df.groupby(['BasketID', 'Service'])['Service'].count().unstack().fillna(0).map(lambda x: 1 if x > 0 else 0)
invoice_product_df.head()


# Create assosiation rules for services
frequent_itemsets = apriori(invoice_product_df, min_support=0.01, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="support", min_threshold=0.01)
rules.head()



# Create a function for recommendation system
def arl_recommender(rules_df, product_id, rec_count=1):
    sorted_rules = rules_df.sort_values("lift", ascending=False)
    recommendation_list = [] 
    for i, product in sorted_rules["antecedents"].items():
        for j in list(product): 
            if j == product_id:
                recommendation_list.append(list(sorted_rules.iloc[i]["consequents"]))         


    recommendation_list = list({item for item_list in recommendation_list for item in item_list})
    return recommendation_list[:rec_count] 


# Test the function with a product "2_0" and get 4 recommendations
arl_recommender(rules,"2_0", 4)