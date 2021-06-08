from models import Sources
from flask import render_template,request,redirect,url_for
from .import main
from ..request import get_sources, get_articles
# from ...modelsmodels import Sources

@main.route('/')
def index():
    '''
    view root page function
    '''
    sources = get_sources('business')
	technology_sources = get_sources('technology')
	entertainment_sources = get_sources('entertainment')
    sports_sources = get_sources('sports')
    title = "NEWS"

     return render_template('index.html', title = title, business = Sources, technology = technology_sources, entertainment = entertainment_sources,sports = sports_sources )