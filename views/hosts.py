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
    # salt.login()
    # s = salt.minions['return'][0]
    # if name not in s.keys():
    #     return res(message='主机未监控')

    content = salt.get_hosts(name)

    return res(data=content)



@instance.route('/server',methods=['POST'])
def get_server():

    data_info = request.get_json(force=True)
    fun = 'cmd.run'
    content = salt.run(tgt=data_info['tgt'],fun=fun,arg=data_info['arg'])
    print content
    return res(data=content)


# @instance.route('/filename',methods=['POST'])
# def get_filename():
