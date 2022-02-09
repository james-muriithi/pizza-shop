import os

class Config:
    """
    General configuration parent class
    """
    DB_USER = os.environ.get('DB_USER') or  ""
    DB_PASSWORD = os.environ.get('DB_PASSWORD') or ""
    DB = 'pitches'
    
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@localhost/{DB}'

    SECRET_KEY = os.environ.get('SECRET_KEY') or ""



class ProdConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


config_options = {
    'development': DevelopmentConfig,
    'production': ProdConfig
}