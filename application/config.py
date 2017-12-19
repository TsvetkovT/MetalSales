import os
'''activates the cross-site request forgery prevention'''
WTF_CSRF_ENABLED = True
'''config secret key'''
SECRET_KEY = os.urandom(24)
