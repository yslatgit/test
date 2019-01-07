import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    @staticmethod
    def init__app(app):
        # app.config.setdefault('SQLALCHEMY_DATABASE_URI',DevelopmentConfig.SQLALCHEMY_DATABASE_URI )
        # app.config.setdefault('SQLALCHEMY_COMMIT_ON_TEARDOWN',DevelopmentConfig.SQLALCHEMY_COMMIT_ON_TEARDOWN )
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1/test?charset=utf8'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

class TestingConfig(Config):
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1/test?charset=utf8'
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'PRODUCTURI'

config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig
}

if __name__ == '__main__':
    # print(config.())
    # pass
    print(type(config['default']))