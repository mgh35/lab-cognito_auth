from flask import Flask, render_template
import json

app = Flask(__name__)


def stack_context():
    with open("../.build/stack.json", "r") as f:
        return json.loads(f.read())


@app.route("/login")
def login():
    return render_template("login.html", **stack_context())


app.run(debug=True)
