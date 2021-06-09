class Sources:
    '''
    news source class to define sources objects
    '''
    def __init__(self, id, title, description,url, category,country):
        self.id = id
        self.title = title
        self.description = description
        self.url = url
        self.category = category
        self.country = country
    

class Articles:
    '''
    articles class to define articles objects
    '''
    def __init__(self, author, title, description, url, image, date):
        self.url = url
        self.author = author
        self.title = title
        self.description = description
        self.image = image
        self.date = date
