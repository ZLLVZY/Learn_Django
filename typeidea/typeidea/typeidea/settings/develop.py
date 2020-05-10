from .base import *

DEBUG = True

'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''

INSTALLED_APPS+=[
    'debug_toolbar',
    'pympler'
    ]

MIDDLEWARE +=[
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

INTERNAL_IPS=['127.0.0.1']

DATABASES={
    'default':{
        'ENGINE':'django.db.backends.mysql',
        'NAME':'typeidea_db',
        'USER':'root',
        'PASSWORD':'123456aa',
        'HOST':'172.17.0.3',
        'PORT':3306,
        # 'CONN_MAX_AGE':5*60,
        # 'OPTIONS':{'charset','utf8mb4'}
    }
}
