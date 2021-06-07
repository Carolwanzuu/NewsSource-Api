from os import name


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