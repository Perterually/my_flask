#!/usr/bin/env python3
#!-*- coding:utf-8
from fund_gonmu import app
from fund_gonmu.database import db


def init_db():
    db.init_app(app)
    db.app = app
    db.create_all()


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
    
