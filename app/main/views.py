
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
    
        return render_template('index.html',title = title, sources = sources,sports = sports_sources,technology = technology_sources,entertainment = entertainment_sources)

@main.route('/sources/<id>')
def articles(id):
	'''
	view articles page
	'''
	articles = get_articles(id)
	title=f'NH | {id}'

	return render_template('articles.html',title= title,articles = articles)
 
    
