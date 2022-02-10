from email.policy import default
import os
from decouple import config

class Config:
    """
    General configuration parent class
    """

    DB_USER = config('DB_USER', default="")
    DB_PASSWORD = config('DB_PASSWORD', default="")

    DB = 'pizza'
    
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://kibet:KibetFlask@localhost/pizza'

    SECRET_KEY = config('SECRET_KEY', default="fLA28%@ksy")

    SECRET_KEY = os.environ.get('SECRET_KEY') or "fLA28%@ksy"
    UPLOADED_PHOTOS_DEST = 'app/static/photos'


class ProdConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


config_options = {
    'development': DevelopmentConfig,
    'production': ProdConfig
}