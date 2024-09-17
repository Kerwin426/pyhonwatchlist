# -*- coding: utf-8 -*-
import os
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask('watchlist')
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)# 初始化扩展，传入创建的 Flask 实例app
bootstrap = Bootstrap(app)
moment = Moment(app)
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id): # 创建用户加载回调函数，接受用户 ID 作为参数
    from watchlist.models import User
    user = User.query.get(int(user_id)) # 用 ID 去数据库查询用户
    return user

login_manager.login_view = 'login'
# context_processor 装饰的函数返回的变量将会统一注入到每一个模板的上下文中，因此我们可以在模板中直接使用 user 变量
@app.context_processor
def inject_user():
    from watchlist.models import User
    user = User.query.first()
    return dict(user=user)


from watchlist import views, errors, commands