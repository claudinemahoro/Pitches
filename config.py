import os

class Config:
    '''
    General Configuration parent class
    '''
    SECRET_KEY="00000"
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://claudine:1998@localhost/pitches'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
      
class ProdConfig(Config):
    '''
    production configuration child class
    Args:
        Config: parent configuration class with general configuration
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    
class DevConfig(Config):
    '''
    Development configuration child class
    '''
    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}