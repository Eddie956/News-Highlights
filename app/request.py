from app import app
import urllib.request,json
from .models import news
from .requests import get_news, get_news, search_news

News = news.News
api_key = app.config['NEWS_API_KEY']
base_url = app.config["SOURCE_API_BASE_URL"]

def get_news(category):
    
    get_source_url = base_url.format(category,api_key)
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        news_results = None

        if get_source_response['results']:
            news_results_list = get_source_response['results']
            news_results = process_results(news_results_list)
    
        return news_results

def process_results(news_list):
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        language = news_item.get('language')
        country = news_item.get('country')

        if news :
            news_object = News(id,name,description,url,category,language,country)
            news_results.append(news_object)
        
    return news_results


def get_news(id):
    get_news_details_url = base_url.format(id, api_key)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        if news_details_response:
            id = news_details_response.get('id')
            name = news_details_response.get('name')
            description =news_details_response.get('description')
            url =news_details_response.get('url')
            category = news_details_response.get('category')
            language = news_details_response.get('language')
            country = news_details_response.get('country')
            news_object = News(id, name, description, url,
                                 category, language, country)

    return news_object


def search_news(news_name):
    news_news_url = 'def search_movie(movie_name):
    search_news_url = 'https: // newsapi.org/v2/sources{}?&apiKey = {}'.format(api_key, news_name)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None

        if search_news_response['results']:
            search_news_list = search_news_response['results']
            search_news_results = process_results(search_news_list)

    return search_movie_results.format(
        api_key, news_name)
    with urllib.request.urlopen(news_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None

        if search_news_response['results']:
            search_news_list = search_news_response['results']
            search_news_results = process_results(search_news_list)

    return search_news_results

