# Configurations for the application
class Config():
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
class LocalDevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///jwtdb.sqlite3'
    JWT_SECRET_KEY = 'secret_key'