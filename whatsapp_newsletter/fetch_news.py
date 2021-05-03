from newsapi import NewsApiClient


def fetch_news(newsapi_personal_key, news_language, news_country, news_category, search_terms):
    newsapi = NewsApiClient(api_key=newsapi_personal_key)

    top_headlines = newsapi.get_top_headlines(
        q=search_terms,
        category=news_category,
        language=news_language,
        country=news_country,
    )

    return top_headlines
