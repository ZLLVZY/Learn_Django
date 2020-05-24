from .base import *

DEBUG=False

DATABASES={
        'default':{
            'ENGINE':'django.db.backends.mysql',
            'NAME':'typeidea_db',
            'USER':'root',
            'PASSWORD':'123456aa',
            'HOST':'172.17.0.3',
            'PORT':3306,
            'CONN_MAX_AGE':5*60,
            'OPTIONS':{'charset':'utf8mb4'}
            },
        }

REDIS_URL='redis://172.17.0.4:6379'

CACHES={
        'default':{
            'BACKEND':'django_redis.cache.RedisCache',
            'LOCATION':REDIS_URL,
            'TIMEOUT':300,
            'OPTIONS':{
                #'PASSWORD':'',
                'CLIENT_CLASS':'django_redis.client.DefaultClient',
                'PARSER_CLASS':'redis.connection.HiredisParser',
                },
            'CONNECTION_POOL_CLASS':'redis.connection.BlockingConnectionPool',
            }
        }

