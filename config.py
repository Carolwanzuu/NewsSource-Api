import os
class Config:
    '''
    General configuration parent class
    '''
    News_Api_Base_Url = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    Articles_Base_Url = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
    News_Api_Key = os.environ.get('News_Api_Key')
    # SECRET_kEY = os.environ.get('SECRET_KEY')
    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
    'development':DevConfig,
    'production': ProdConfig
}
