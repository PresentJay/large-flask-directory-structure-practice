from markupsafe import escape
from flask import Flask, abort


app = Flask(__name__)


# 여러 라우트를 결합 가능
@app.route("/")
@app.route("/index/")
def hello():
    return "<h1>Hello, World</h1>"


@app.route("/about/")
def about():
    return "<h3>This is a Flask web application.</h3>"


@app.route("/capitalize/<word>/")
def capitalize(word):
    return "<h1>{}</h1>".format(escape(word).capitalize())


# 특수변환기 -> n1, n2를 양의 정수만 허용하도록 특수 변환
@app.route("/add/<int:n1>/<int:n2>/")
def add(n1, n2):
    return "<h1>{}</h1>".format(n1 + n2)


@app.route("/users/<int:user_id>/")
def greet_user(user_id):
    users = ["Bob", "Jane", "Adam"]
    try:
        return "<h2>Hi {}</h2>".format(users[user_id])
    except IndexError:
        abort(404)
