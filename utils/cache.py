# -*- coding: UTF-8 -*-
'''
@author: 'FenG_Vnc'
@date: 2017-05-24 15:57
@file: cache.py
'''
from __future__ import unicode_literals


from redis import StrictRedis
from app import config


class redis_cil():

    def __connect(self):
        return StrictRedis.from_url(config.CACHE_REDIS_URL)

    def _r(self):
        return self.__connect()

    def get(self,key):
        return self._r().get(key)

    def set(self,key,value,time):
        if self.get(key):
            return self.get(key)
        else:
            return self._r().set(key,value,ex=time)

