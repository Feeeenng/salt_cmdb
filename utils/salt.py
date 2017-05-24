# -*- coding: UTF-8 -*-
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
        self.r = redis_cil()
        self.redis_key  = 'salt:user:{user}:login'.format(user=self.user)

    def req(self,path,info):

        urlpath = urljoin(self.url, path)
        if self.r.get(self.redis_key):
            token = json.loads(self.r.get(self.redis_key).decode('utf-8'))
            self.headers['X-Auth-Token'] = token['X-Auth-Token']

        s = session()
        info = json.dumps(info)
        res = s.post(urlpath,info,headers=self.headers)
        return res


    def req_get(self,path):

        urlpath = urljoin(self.url,path)
        token = json.loads(self.r.get(self.redis_key).decode('utf-8'))
        self.headers['X-Auth-Token'] = token['X-Auth-Token']

        s = session()
        res = s.get(urlpath,headers=self.headers)
        return res

    def login(self):
        redis_key = 'salt:user:{user}:login'.format (user=self.user)
        if self.r.get (redis_key):
            self.auth = self.r.get(redis_key)
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
        self.r.set (redis_key, json.dumps(self.auth), expire_time)
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

    def run(self,fun,args,tgt):
        data_info = [{
            'clinet':"local",
            "tgt":tgt,
            "fun":fun
        }]

        if args:
            data_info[0]['arg'] = args

        res = self.req('',data_info).json()
        return res

