# -*- coding: UTF-8 -*-
'''
@author: 'FenG_Vnc'
@date: 2017-05-25 15:25
@file: hosts.py
'''
from __future__ import unicode_literals

from models import res
from utils.salt import SaltApi

from flask import Blueprint,request

instance = Blueprint('hosts',__name__,url_prefix='/hosts')


salt = SaltApi()


@instance.route('/get/<name>')
def get_host(name):

    if not name:
        return res(message='参数不正确')

    s = salt.minions['return'][0]
    if name not in s.keys():
        return res(message='主机未监控')
    # for i in s['return']:


    content = salt.get_hosts(name)

    return res(data=content)




