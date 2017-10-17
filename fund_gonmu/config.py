#!/usr/bin/env python3
#!-*- coding:utf-8
DEBUG = True
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
BCRYPT_LOG_ROUNDS = 12
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@192.168.1.125:3307/relation_configure"
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
MAIL_FROM_EMAIL = "perterually@163.com"