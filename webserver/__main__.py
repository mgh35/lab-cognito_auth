from flask import Flask, request, render_template
import json

app = Flask(__name__)


def stack_context():
    with open("../.build/stack.json", "r") as f:
        return json.loads(f.read())


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html", **stack_context())


@app.route("/login_redirect")
def login_redirect():
    return render_template("login_redirect.html")


app.run(debug=True)
