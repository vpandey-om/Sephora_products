**About Dataset and use**
This dataset was collected From [kaggle](https://www.kaggle.com/datasets/nadyinky/sephora-products-and-skincare-reviews):
First download the data in **sephora** folder.

Information about all beauty products (over 8,000) from the Sephora online store, including product and brand names, prices, ingredients, ratings, and all features.
user reviews (over 1 million on over 2,000 products) of all products from the Skincare category, including user appearances, and review ratings by other users

**Dataset Usage Examples**
- Exploratory Data Analysis (EDA): Explore product categories, regular and discount prices, brand popularity, the impact of different characteristics on price, and ingredient trends
- Sentiment Analysis: Is the emotional tone of the review positive, negative, or neutral? Which brands or products have the most positive or negative reviews?
Text Analysis: What do customers say most often in their negative and positive reviews? Do customers have any common problems with their skincare?
- Recommender System: Analyzing the customer's past purchase history and reviews, suggest products that are likely to be of interest to them
- Data Visualization: What are the most popular brands and products? What is the distribution of prices? Which products are closest to each other in ingredients? What does the cloud of the most frequently used words look like?

**Exploratory Data Analysis**
- Examine the dataset's structure, including the number of rows and columns, data types, and any missing values.
- Missing values are handled by imputing or deleting them.
- Examine the influence of outliers or erroneous data points on the analysis and decide whether to keep or remove them
- Here is a Amazon Jupyter Notebook code in Amazon SageMaker Studio Lab [code](https://github.com/vpandey-om/Sephora_products/blob/main/EDA_analysis.ipynb)

## Sentiment Analysis of Sephora Skincare Review Data Set:

A natural language processing approach called sentiment analysis is used to identify the sentiment or emotion expressed in a text. Sentiment analysis can be used to examine the overall sentiment surrounding Sephora skincare goods by applying it to customer reviews or other text data.

Sentiment analysis for Sephora skincare goods aims to categorize customer reviews as favorable, negative, or neutral automatically. This can be used to better understand how consumers generally feel about various skincare brands or products.

- Perform sentiment analysis on customer reviews to understand the overall sentiment (positive, negative, or neutral).
- Use natural language processing techniques to classify reviews and extract sentiment-related information.
- Visualize sentiment patterns using bar plots or word clouds to identify popular sentiment trends.
- Here is a Amazon Jupyter Notebook code in Amazon SageMaker Studio Lab [code](https://github.com/vpandey-om/Sephora_products/blob/main/Sentimnet_analysis.ipynb)
