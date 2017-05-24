# -*- coding: UTF-8 -*-
'''
@author: 'FenG_Vnc'
@date: 2017-05-24 14:28
@file: manager.py
'''
from __future__ import unicode_literals


from flask_script import Manager,Server,Shell

from app import create_app



app = create_app()
manager = Manager(app)
manager.add_command("runserver",Server(threaded=True,port=80))


@app.before_request
def before_request():
    '''每个请求前执行'''
    pass

@app.teardown_request
def teardown_request(expection):
    ''' 每个请求结束时候执行'''
    pass



if __name__ == '__main__':
    manager.run(default_command="runserver")