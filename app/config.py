import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = 'postgresql://127.0.0.1:5432/cleverinsight'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    UPLOAD_FOLDER = 'app/uploads'


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'dsadsa3r90haids90py84920hif9-q90d-qud09s'
    SQLALCHEMY_DATABASE_URI = 'postgres://qmfeisyxjvullw:423c7a964f8419b2a0fc8ff5a9fb155ff423de84f690a3fb1d2bc100437385cb@ec2-54-225-129-101.compute-1.amazonaws.com:5432/d71mtfdqmmavap'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    UPLOAD_FOLDER = 'app/uploads'


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
