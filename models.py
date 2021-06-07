from os import name
from re import I


class Sources:
    '''
    news source class to define sources objects
    '''
    def __init__(self, id, title, description,url, category,country,language):
        self.id = id
        self.name = name
        self.title = title
        self.description = description
        self.url = url
        self.category = category
        self.country = country
        self.language = language

class Articles:
    '''
    articles class to define articles objects
    '''
    def __init__(self, id, author, title, description, url, image, date):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.image = image
        self.date = date
