from flask import Flask,url_for
from markupsafe import escape
app = Flask(__name__)

# 注册一个处理函数，当访问根路径时，返回 "Welcome to my app!"

@app.route('/')
def hello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

@app.route('/user/<name>')
def user_page(name):
    return f'User {escape(name)}'

@app.route('/test')
def test_url_for():
    # 下面的print是会在终端打印的
    print(url_for('hello')) # 生成URL
    print(url_for('user_page',name='greyli')) # 生成URL
    print(url_for('user_page',name='peter')) # 生成URL
    print(url_for('test_url_for')) # 生成URL
    print(url_for('test_url_for',num=2)) # 生成URL
    return 'This is a test page'
