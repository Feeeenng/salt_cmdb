# -*- coding: UTF-8 -*-
'''
@author: 'FenG_Vnc'
@date: 2017-05-24 14:37
@file: __init__.py
'''
from __future__ import unicode_literals


from flask import jsonify


def res(code=0,data=None,message=None):

    if message:
        message = message
    else:
        message = '操作成功'
    return jsonify({
        "code":code,
        "data":data,
        "message":message
    })


