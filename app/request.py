import urllib.request, json
from models import Sources,Articles

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