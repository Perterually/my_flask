#!/usr/bin/env python3
#!-*- coding:utf-8 -*-
from flask import Flask
from flask import render_template, session, g


app = Flask(__name__,instance_relative_config=False)
app.config.from_pyfile('config.py')
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'



@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from .views import user
app.register_blueprint(user.bp)
