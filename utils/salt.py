# -*- coding: UTF-8 -*-
from __future__ import print_function

'''
@author: 'FenG_Vnc'
@date: 2017-05-24 15:05
@file: salt.py
'''
from __future__ import unicode_literals

import json
import os
try:
    from urlparse import urljoin
except:
    import urllib.parse as urljoin

from requests import session
import requests

from app import config
from utils.cache import redis_cil




class SaltApi(object):
    '''saltAPI'''

    def __init__(self):
        self.headers = {
            'Accept': 'application/json',
            'Content-type': 'application/json'
        }
        self.url = config.SALT_HOST
        self.user = config.SALT_USER
        self.passwd = config.SALT_PASSWD
        self.eauth = config.SAL_EAUTH
        self.auth = {}
        self.redis_cil = redis_cil()
        self.redis_key  = 'salt:user:{user}:login'.format(user=self.user)

    def req(self,path,info):
        urlpath = urljoin(self.url, path)
        if self.redis_cil.get(self.redis_key):
            token = json.loads(self.redis_cil.get(self.redis_key).decode('utf-8'))
            self.headers['X-Auth-Token'] = token['X-Auth-Token']

        s = session()
        info = json.dumps(info)
        res = s.post(urlpath,data=info,headers=self.headers)
        return res


    def req_get(self,path):

        urlpath = urljoin(self.url,path)
        token = json.loads(self.redis_cil.get(self.redis_key))
        self.headers['X-Auth-Token'] = token['X-Auth-Token']

        s = session()
        res = s.get(urlpath,headers=self.headers)
        return res

    def login(self):
        if self.redis_cil.get(self.redis_key):
            self.auth = self.redis_cil.get(self.redis_key)
            return self.auth
        else:
            login_info = {
                'username': self.user,
                'password': self.passwd,
                'eauth': self.eauth
            }
        ret_info = self.req('/login', login_info).json ()['return'][0]

        start_time = ret_info['start']
        end_time = ret_info['expire']
        expire_time = int(end_time -start_time)
        token = ret_info['token']
        self.auth['X-Auth-Token'] = token
        self.redis_cil.set (self.redis_key, json.dumps(self.auth), expire_time)
        return self.auth

    @property
    def stats(self):
        res = self.req_get('/stats').json()
        return res

    @property
    def jobs(self):
        res =self.req_get('/jobs').json()
        return res

    @property
    def minions(self):
        res = self.req_get('/minions').json()
        return res

    @property
    def keys(self):
        res = self.req_get('/keys').json()
        return res

    def run(self, tgt, fun, arg,):
        data_info = {
            "client":"local",
            "tgt":tgt,
            "fun":fun,
        }

        if arg:
            data_info['arg'] = arg
        # print data_info
        res = self.req('/',data_info).json()
        return res

