# Put your app in here.

from operations import add, sub, div, mult

from flask import Flask, request

app = Flask(__name__)


operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }


@app.route("/add")
def additon():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a,b)

    return str(result)

@app.route("/sub")
def subtraction():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a,b)

    return str(result)

@app.route("/mult")
def multiply():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a,b)

    return str(result)

@app.route("/div")
def division():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a,b)

    return str(result)

@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)



