#http://flask.pocoo.org/docs/0.10/tutorial/setup/
import os

class Config(object):

    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):

    # host
    HOST = '127.0.0.1'
    DB_URL = '192.168.99.100'

class DevelopmentContainerConfig(DevelopmentConfig):

    # host
    HOST = '0.0.0.0'
