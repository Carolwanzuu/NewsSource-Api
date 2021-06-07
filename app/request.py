import urllib.request, json
from models import Sources,Articles
from datetime import datetime

# getting api key
api_key = None

# getting the news_api base url
base_url = None

# getting the articles url
articles_url = None

def configure_request(app):
    global api_key, base_url, articles_url
    api_key = app.config['News_Api_Key']
    base_url = app.config['News_Api_Base_Url']
    articles_url = app.config['Articles_Base_Url']

def get_sources(category):
    '''
    function that gets json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)

        return sources_results

def process_sources(sources_list):
    '''
    function that processes news sources
    Args:
        sources_list:A list of dictionaries that contain sources details
    Returns:
        sources_results:A list of sources objects
    '''

    sources_results = []

    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        sources_object = Sources(id,name, description, url, category, language, country)
        sources_results.append(sources_object)

    return sources_results

def get_articles(id):
    '''
    function that processes articles and returns a list of articles
    '''
    get_articles_url = articles_url.format(id, api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        articles_results = json.loads(url.read())

        articles_object = None
        if articles_results['articles']:
            articles_object = process_articles(articles_results['articles'])

    return articles_object

def process_articles(articles_list):
     '''
    function that processes articles
    Args:
        articles_list:A list of dictionaries that contain articles details
    Returns:
        articles_results:A list of articles objects
    '''
     articles_results = []

     for article_item in articles_list:
         id = article_item.get('id')
         author = article_item.get('author')
		 title = article_item.get('title')
		 description = article_item.get('description')
		 url = article_item.get('url')
		 image = article_item.get('urlToImage')
		 date = article_item.get('publishedAt')

         if image:
             articles_results = Articles(id, author, title,description, url, image,date)
             articles_object.append(articles_results)

         