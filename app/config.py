import os
class config:
    secret_key = os.urandom(40)


class Development(config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///post.db"


class PRODUCTION(config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "postgresql://mostafa:123@localhost:5432/books"
    UPLOADED_PHOTOS_DEST = 'app/static/'


config_option = {
    'dev': Development,
    'prod': PRODUCTION
}