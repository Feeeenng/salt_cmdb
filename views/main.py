# -*- coding: UTF-8 -*-
'''
@author: 'FenG_Vnc'
@date: 2017-05-26 14:38
@file: main.py
'''
from __future__ import unicode_literals

from flask import Blueprint,render_template


instance = Blueprint('main',__name__)


@instance.route('/')
def index():
    return render_template('index.html')