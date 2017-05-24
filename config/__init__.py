# -*- coding: UTF-8 -*-
'''
@author: 'FenG_Vnc'
@date: 2017-05-24 14:37
@file: __init__.py.py
'''
from __future__ import unicode_literals

class Config(object):
    SECRET_KEY  = 'sdaasdaaa'
    SQLALCHEMY_TRACK_MODIFICATIONS  = False


    #salt api 配置
    SALT_HOST= ''
    SALT_USER = ''
    SALT_PASSWD = ''

    # mysql 配置
    MYSQL_HOST = ''
    MYSQL_USER = ''
    MYSQL_PASSWD = ''
    MYSQL_PORT = ''
    MYSQL_DB = ''

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{0}:{1}@{2}:{3}/{4}'.format(MYSQL_USER,MYSQL_PASSWD,MYSQL_HOST,MYSQL_PORT,MYSQL_DB)

    #缓存 配置
    REDIS_HOST = ''
    REDIS_PORT = 6379
    REDIS_DB = 0
    CACHE_TYPE = 'redis'
    CACHE_REDIS_URL = '{0}://{1}:{2}/{3}'.format (CACHE_TYPE, REDIS_HOST, REDIS_PORT, REDIS_DB)


    @staticmethod
    def init_app(app):
        pass