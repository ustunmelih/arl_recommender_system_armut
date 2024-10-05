
# Association Rule Based Recommender System in a Armut Dataset

![img](https://miro.medium.com/v2/resize:fit:720/format:webp/1*eouiAN1NjcjyiuiFNwPhCg.png)

## What is Recommendation System?

A recommendation system is an AI-powered tool that suggests products or services to users based on their preferences and behavior. It analyzes vast amounts of data, including past purchases, search history, and demographics, to identify patterns and recommend relevant items. This helps people discover new products they might like.

## Business Case

Armut is an online platform connecting service providers with customers for various needs like cleaning, home renovation, and transportation. To enhance user experience, Armut aims to develop a product recommendation system using association rule learning. This system will analyze customer service history data to suggest additional relevant services based on past choices.

## The story of the dataset

The dataset includes information on services utilized by customers, categorized by service type. Additionally, it records the specific date and time of each service transaction.

| Variable Name | Description |
|----------------|----------------|
| **UserId** | Customer ID |
| **ServiceId** | They are anonymized services belonging to each category. (Example: Upholstery washing service under Cleaning category) A ServiceId can be found under different categories and represents different services under different categories. (Example: The service with CategoryId 7 and ServiceId 4 is honeycomb cleaning, while the service with CategoryId 2 and ServiceId 4 is furniture assembly) |
| **CategoryId** | They are anonymized categories. (Example: Cleaning, transportation, renovation category) |
| **CreateDate** | The date the service was purchased |

