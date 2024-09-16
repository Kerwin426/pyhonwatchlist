from flask import Flask,url_for,render_template
from markupsafe import escape
app = Flask(__name__)

# 注册一个处理函数，当访问根路径时，返回 "Welcome to my app!"

@app.route('/')
def index():
    return render_template('index.html', name=name, movies=movies)

# @app.route('/user/<name>')
# def user_page(name):
#     return f'User {escape(name)}'

# @app.route('/test')
# def test_url_for():
#     # 下面的print是会在终端打印的
#     print(url_for('hello')) # 生成URL
#     print(url_for('user_page',name='greyli')) # 生成URL
#     print(url_for('user_page',name='peter')) # 生成URL
#     print(url_for('test_url_for')) # 生成URL
#     print(url_for('test_url_for',num=2)) # 生成URL
#     return 'This is a test page'

name = 'Kerwin Gu'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]