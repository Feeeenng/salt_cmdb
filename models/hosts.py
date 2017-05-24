# -*- coding: UTF-8 -*-
'''
@author: 'FenG_Vnc'
@date: 2017-05-24 14:56
@file: hosts.py
'''
from __future__ import unicode_literals

from app import db


class Group(db.Model):
    '''主机组表'''
    __tablename__ = "salt_group"
    group_id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    group_name = db.Column(db.VARCHAR(10), unique=True, nullable=False)
    host_name = db.relationship("Host", backref="salt_host", lazy="dynamic")

    def __init__(self, groupname):
        self.group_name = groupname


class Host(db.Model):
    '''主机表'''
    __tablename__ = 'salt_host'
    host_id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    host_name = db.Column(db.VARCHAR(36), unique=True, nullable=False)
    host_group = db.Column(db.VARCHAR(10), db.ForeignKey('salt_group.group_name'), nullable=False)

    def __init__(self, hostname, groupname):
        self.host_name = hostname
        self.host_group = groupname