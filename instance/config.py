import os

#class Config(object):
DEVELOPMENT = True
DEBUG = True
BASEDIR = os.path.abspath(os.path.dirname(__file__))
'''activates the cross-site request forgery prevention'''
WTF_CSRF_ENABLED = True
'''config secret key'''
SECRET_KEY = os.urandom(24)


'''configuration of OPEN ID PROVIDERS'''
OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

'''configuration of the database'''
SQLALCHEMY_DATABASE_URI =  'mysql://root:Bene1979@127.0.0.1/trade'
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASEDIR,'db_repository')

# class ProductionConfig(Config):
#     DEVELOPMENT = False
#     DEBUG = False
#     #DB_HOST =