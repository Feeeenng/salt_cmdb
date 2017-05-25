# -*- coding: UTF-8 -*-
'''
@author: 'FenG_Vnc'
@date: 2017-05-24 17:06
@file: salt_views.py
'''
from __future__ import unicode_literals

import re

from flask import jsonify,request,Blueprint

from utils.salt import SaltApi
from models import res

instance = Blueprint('salt',__name__,url_prefix='/salt')

salt = SaltApi()

@instance.route('/login')
def login():
    if not salt.redis_cil.get(salt.redis_key):
        a = salt.login()
        return jsonify(a)
    else:
        return jsonify(salt.redis_cil.get(salt.redis_key))


@instance.route('/stats')
def stats():
    for k,v in salt.stats.items():
        m = re.match (r"CherryPy HTTPServer.*", k)
        if m:
            return res(data=salt.stats[m.group(0)])



@instance.route('/jobs')
def jobs():
    return res(data=salt.jobs)

@instance.route('/minions')
def minion():
    return res(data=salt.minions)

@instance.route('/keys')
def keys():
    return res(data=salt.keys)


# @instance.route('/publish',methods=['POST'])
# def git():
#     post_info = request.get_json(force=True)
#     data = salt.run(tgt=post_info['tgt'],fun=post_info['fun'],arg=post_info['arg'])
#     return res(data=data)


