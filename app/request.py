import urllib.request, json
from .models import Sources, Articles
from datetime import datetime

# getting api key
api_key = None

# getting the news_api base url
base_url = None

# getting the articles url
articles_url = None

def configure_request(app):
        global api_key, base_url, articles_url
        api_key = app.config['NEWS_API_KEY']
        base_url = app.config['NEWS_API_BASE_URL']
        articles_url = app.config['ARTICLES_BASE_URL']

def get_sources(sources):
        '''
        function that gets json response to our url request
        '''
        get_sources_url = base_url.format(sources,api_key)
        
        with urllib.request.urlopen(get_sources_url) as url:
            get_sources_data = url.read()
            get_sources_response = json.loads(get_sources_data)
            
            sources_results = None
            if get_sources_response['sources']:
                sources_results_list = get_sources_response['sources']
                sources_results = process_sources(sources_results_list)
        
        
        return sources_results

def process_sources(sources_resultsList):
        '''
        function that processes news sources results and transforms them to a list of objects
        Args:
            sources_list:A list of dictionaries that contain sources details
        Returns:
            sources_results:A list of sources objects
        '''

        sources_results_list = []

        for source_item in sources_resultsList:
                id = source_item.get('id')
                name = source_item.get('name')
                description = source_item.get('description')
                url = source_item.get('url')
                category = source_item.get('category')
                language = source_item.get('language')
                country = source_item.get('country')

                sources_object = Sources(id,name, description, url, category, language, country)
                sources_results_list.append(sources_object)

        return sources_results_list

def get_articles(title):
        '''
        function that processes articles and returns a list of articles
        '''
        get_articles_url = articles_url.format(title, api_key)

        with urllib.request.urlopen(get_articles_url) as url:
            get_articles_data = url.read()
            get_articles_response = json.loads(get_articles_data)
            # articles_results = json.loads(url.read())

            articles_results = None
            
            if get_articles_response['articles']:
                articles_results_list = get_articles_response['articles']
                articles_results = process_articles(articles_results_list)

        
        return articles_results

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

                
                author = article_item.get('author')
                title = article_item.get('title')
                description = article_item.get('description')
                url = article_item.get('url')
                image = article_item.get('urlToImage')
                date = article_item.get('publishedAt')

            
                articles = Articles(author, title,description, url, image,date)
                articles_results.append(articles)

        return articles_results