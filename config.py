 import os
class Config:
    '''
    General configuration parent class
    '''
    News_Api_Base_Url = ''
    News_Api_Key = ''
    SECRET_kEY = os.environ.get('SECRET_KEY')



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
