from flask import Flask, send_file

app = Flask(__name__)


@app.route('/index')
def index():
    # 首页
    return send_file('templates/index.html')


@app.route('/login')
def login():
    # 首页
    return send_file('templates/login.html')


@app.route('/register')
def register():
    # 首页
    return send_file('templates/register.html')


@app.route('/news')
def news():
    # 首页
    return send_file('templates/news.html')


@app.route('/article')
def article():
    # 首页
    return send_file('templates/article.html')


@app.route('/show')
def show():
    # 首页
    return send_file('templates/show.html')


@app.route('/write')
def write():
    # 首页
    return send_file('templates/write.html')


if __name__ == '__main__':
    app.run(debug=True)
