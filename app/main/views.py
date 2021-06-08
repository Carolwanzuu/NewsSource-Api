
from flask import render_template,request,redirect,url_for
from .import main
from ..request import get_sources, get_articles
from ..models import Sources


@main.route('/')
def index():
        '''
        view root page function
        '''
        sources = get_sources('business')
        sports_sources = get_sources('sports')
        technology_sources = get_sources('technology')
        entertainment_sources = get_sources('entertainment')
        title = "NEWS"
    
        return render_template('index.html',title = title, sources = sources,sports_sources = sports_sources,technology_sources = technology_sources,entertainment_sources = entertainment_sources)
    


@main.route('/sources/<id>')
def articles(id):
    articles = get_articles(id)
    return render_template('articles.html',articles = articles)