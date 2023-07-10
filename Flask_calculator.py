from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return "welcome"

@app.route('/welcome/back')
def welcome_back():
    return "welcome back"

@app.route('/welcome/home')
def welcome_home():
    return "welcome home"


app = Flask(__name__)

@app.route("/add")
def do_add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = (a + b)
    return str(result)

@app.route("/sub")
def do_sub():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = (a - b)
    return str(result)

@app.route("/mult")
def do_mult():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = (a + b)
    return str(result)

@app.route("/div")
def do_div():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = (a / b)
    return str(result)


