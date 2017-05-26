# -*- coding: UTF-8 -*-
'''
@author: 'FenG_Vnc'
@date: 2017-05-24 14:28
@file: app.py
'''
from __future__ import unicode_literals

import os
import glob

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config



db = SQLAlchemy()


def __config_blueprint(app):
    dir = os.path.dirname(__file__)
    views_dir = os.path.join(dir, 'views')
    views_files = glob.glob(os.path.join(views_dir, '*.py'))
    for views_file in views_files:
        basename = os.path.basename(views_file)
        if basename == '__init__.py':
            continue

        views_file_name = basename[:basename.rindex('.')]
        module = __import__('views.{0}'.format(views_file_name), fromlist=['instance'])
        if not hasattr(module, 'instance'):
            continue

        instance = getattr(module, 'instance')
        app.register_blueprint(instance)


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)

    __config_blueprint (app)

    return app