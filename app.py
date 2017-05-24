# -*- coding: UTF-8 -*-
'''
@author: 'FenG_Vnc'
@date: 2017-05-24 14:28
@file: app.py
'''
from __future__ import unicode_literals

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import config


db = SQLAlchemy()




def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)


    return app