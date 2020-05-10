from .base import *

DEBUG=False

ALLOWED_HOST=['the5fire.com']

DATABASES={
        'default':{
            'ENGINE':'django.db.backends.mysql',
            'NAME':'typeidea_db',
            'USER':'root',
            'PASSWORD':'password',
            'HOST':'172.17.0.3',
            'PORT':3306,
            'CONN_MAX_AGE':5*60,
            'OPTIONS':{'charset':'utf8mb4'}
            },
        }
