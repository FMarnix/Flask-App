class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
    pass

class DevConfig(Config):
    SECRET_KEY = "\r\xf2\x08\xe5RC\xd1\xb9\x8f)=6\x91\x0c\xcb\xc9\xa6\x9dt\xe1\x02o\x9a\xb6"
    debug = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev.db"