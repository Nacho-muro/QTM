import finnhub
import requests
from newsapi import NewsApiClient
from pysentimiento import SentimentAnalyzer
import pandas as pd
import matplotlib.pyplot as plt

# Setting up API keys and clients
finnhub_client = finnhub.Client(api_key="d163tb9r01qhvkj61lr0d163tb9r01qhvkj61lrg")
newsapi = NewsApiClient(api_key="a9fe25c3e9364dd18f82349010fb28f7")
sentiment_analyzer = SentimentAnalyzer()

# Input company ticker
company_ticker = input("Enter company ticker (e.g. AAPL, AMZN): ")

# Fetching data from Finnhub
company_profile = finnhub_client.company_profile2(symbol=company_ticker)
price = finnhub_client.quote(symbol=company_ticker)
financials = finnhub_client.financials_reported(symbol=company_ticker)

# Fetching real-time news related to the company
news = newsapi.get_everything(q=company_ticker, language='en', sortBy='publishedAt', page_size=5)

# Sentiment analysis on the news
news_sentiments = []
for article in news['articles']:
    text = article['title'] + ' ' + article['description']
    sentiment = sentiment_analyzer.predict(text, lang='es')
    news_sentiments.append(sentiment)

# Fetching economic data from the World Bank
# You can use their API for fetching data

# Simulation of future values
# Custom logic for simulating future values based on current data and sentiment

# Visualization of data
# You can create visualizations using matplotlib and pandas

# Displaying results
print("Company Profile:")
print(company_profile)
print("\nPrice:")
print(price)
print("\nFinancials:")
print(financials)
print("\nNews Sentiments:")
for idx, sentiment in enumerate(news_sentiments):
    print(f"News {idx+1}: {sentiment}")
