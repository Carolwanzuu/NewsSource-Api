class Sources:
    '''
    news source class to define sources objects
    '''
    def __init__(self, id,name, description,url, category,language, country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country
    

class Articles:
    '''
    articles class to define articles objects
    '''
    def __init__(self, author, title, description, url, image, date):
        
       
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.image = image
        self.date = date
