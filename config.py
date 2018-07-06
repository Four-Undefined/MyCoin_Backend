#codig: utf-8
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "hard to guess"

class DevelopmentConfig(Config) :
    DEBUG = True
    #SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "data-dev.sqlite")
    SQLALCHEMY_DATABASE_URI = os.getenv('MYCOIN_WEBSITE_SQL')

    """mail configuration"""
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_DEBUG = True
    MAIL_USERNAME = os.getenv('AUTH_MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('AUTH_MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = MAIL_USERNAME
    AUTH_MAIL_SUBJECT_PREFIX = '[MyCoin]'
    #REDIS_BROKER_HOSTNAME = os.getenv('REDIS_BROKER_HOSTNAME')
    #REDIS_BACKEND_HOSTNAME = os.getenv('REDIS_BACKEND_HOSTNAME')

    """celery configuration"""
    CELERY_BROKER_URL = 'redis://{}:6385/0'.format(os.environ.get('REDIS_BROKER_HOSTNAME'))
    CELERY_RESULT_BACKEND = 'redis://{}:6385/1'.format(os.environ.get('REDIS_BACKEND_HOSTNAME'))


config = {
        "default" : DevelopmentConfig
        }
