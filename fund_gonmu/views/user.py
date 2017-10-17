#!/usr/bin/env python3
#!-*- coding:utf-8 -*-
from flask import Blueprint, render_template, g, request, redirect, session, url_for
from fund_gonmu.database import User, db, app
from sqlalchemy.orm import sessionmaker
from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_login import LoginManager, login_user, login_required, logout_user

login_manager = LoginManager()
login_manager.init_app(app)

bp = Blueprint('user',__name__,template_folder='/user')


class SignupForm(Form):
    username = StringField('username')
    password = PasswordField('password',
                            validators=[DataRequired()])
    submit = SubmitField("Sign In")


@bp.route('/')
def index():
    return render_template('/user/index.html')

@bp.route('/signup',methods=['GET','POST'])
def signup():
    form = SignupForm()
    if request.method == 'GET':
        return render_template('/user/signup.html',form = form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            if User.query.filter_by(username=form.username.data).first():
                return "username already exists"
            else:
                newuser = User(form.username.data, form.password.data)
                db.session.add(newuser)
                db.session.commit()
                return "user created!"
        else:
            return "form didn't validate"

@bp.route('/login',methods=['GET','POST'])
def login():
    form = SignupForm()
    if request.method == 'GET':
        return render_template('/user/login.html',form = form)
    elif request.method == "POST":
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if user.password == form.password.data:
                login_user(user)
                return "User logged in"
        else:
            return "User doesn't exist"
    else:
        return "form didn't validate"

@login_manager.user_loader
def load_user(username):
    return User.query.filter_by(username=username).first()


