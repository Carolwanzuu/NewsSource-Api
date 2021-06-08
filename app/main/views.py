from models import Sources
from flask import render_template
from .import main
from ..request import get_sources, get_articles
# from ...modelsmodels import Sources

@main.route('/')
def index():
    '''
    view root page function
    '''
    business_sources = get_sources('business')
	technology_sources = get_sources('technology')
	entertainment_sources = get_sources('entertainment')
    general_sources = get_sources('general')
    sports_sources = get_sources('sports')
    title = "NEWS"
      return render_template('index.html', title = title, business = business_sources, technology = technology_sources, entertainment = entertainment_sources,sports = sports_sources, general = general_sources )



@main.route('/articles/<id>')
def articles(id):
    articles = get_articles(id)
    return render_template('articles.html')