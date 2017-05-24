# -*- coding: UTF-8 -*-
'''
@author: 'FenG_Vnc'
@date: 2017-05-24 17:06
@file: salt_views.py
'''
from __future__ import unicode_literals

import re

from flask import jsonify,request,session,Blueprint

from utils.salt import SaltApi

instance = Blueprint('salt',__name__)

s = SaltApi()


@instance.route('/stats')
def stats():
    for k,v in s.stats.items():
        print k,v
        m = re.match (r"CherryPy HTTPServer.*", k)
        if m:
            return s.stats[m.group (0)]