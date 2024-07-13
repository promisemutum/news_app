from newsapi import NewsApiClient
def get_news():
    newsapi = NewsApiClient(api_key='fe5ba247e89046f7bac1511ebecb995d')
    top_headlines = newsapi.get_top_headlines(q="apple")
    print(top_headlines) 
