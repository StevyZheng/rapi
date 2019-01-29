# -*- coding: utf-8 -*-


api_info = {
    "version": "1.0",
    "author": "rk",
}


class Config:
    SECRET_KEY = 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DatabaseConfig:
    TYPE = "mysql"
    NAME = "roycom"
    USERNAME = 'root'
    PASSWORD = '000000'
    HOST = '127.0.0.1'


class DevelopmentConfig(Config):
    DEBUG = True
    DatabaseConfig.NAME = "roycom"
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/{}'.format(DatabaseConfig.USERNAME,
                                                                   DatabaseConfig.PASSWORD,
                                                                   DatabaseConfig.HOST, DatabaseConfig.NAME)


class TestingConfig(Config):
    DEBUG = True
    DatabaseConfig.NAME = "roycom"
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/{}'.format(DatabaseConfig.USERNAME,
                                                                   DatabaseConfig.PASSWORD,
                                                                   DatabaseConfig.HOST, DatabaseConfig.NAME)


class ProductionConfig(Config):
    DEBUG = True
    DatabaseConfig.NAME = "roycom"
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/{}'.format(DatabaseConfig.USERNAME,
                                                                   DatabaseConfig.PASSWORD,
                                                                   DatabaseConfig.HOST, DatabaseConfig.NAME)

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
