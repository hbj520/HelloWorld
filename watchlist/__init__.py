from flask import Flask, render_template
from flask import  url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import os
import click
from flask_login import LoginManager, UserMixin, login_required, logout_user, login_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
# import flask_login

prefix = 'sqlite:////'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(os.path.dirname(app.root_path), os.getenv('DATABASE_FILE', 'data.db'))
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')

db = SQLAlchemy(app)
login_manager = LoginManager(app)  # 实例化扩展类
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    from watchlist.models import User
    user = User.query.get(int(user_id))
    return user

# 上下文处理函数，等同于全局计算属性
@app.context_processor
def inject_user():
    from watchlist.models import User
    user = User.query.filter_by(name='Lebron Han').first()
    return dict(user=user) #需要返回字典，等于 {'user': user}

from watchlist import views, errors, commands