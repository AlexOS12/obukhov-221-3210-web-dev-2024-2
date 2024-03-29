from random import randint
from flask import Flask, render_template, make_response, request

# Самописный файлик для проверки и форматирования номера телефона
import pyScripts.phoneWorker as phoneWorker

app = Flask(__name__)

OPERATORS = {"+": lambda a, b: a + b,
             "-": lambda a, b: a - b,
             "*": lambda a, b: a * b,
             "/": lambda a, b: a / b if b else "На ноль делить нельзя!"
             }


@app.route("/")
def index():
    url = request.url
    title = "ЛР №2"
    return render_template("index.html", title=title, url=url)


@app.route("/args")
def args():
    title = "Параметры URL"
    return render_template("args.html", title=title, request=request)


@app.route("/headers")
def headers():
    title = "Параметры URL"
    return render_template("headers.html", title=title, request=request)


@app.route("/cookies")
def cookies():
    title = "Параметры URL"
    response = make_response(render_template(
        "cookies.html", title=title, request=request))
    if "cookies" in request.cookies:
        response.delete_cookie("cookies")
    else:
        response.set_cookie("cookies", "1 piece")

    return response


@app.route("/form", methods=["GET", "POST"])
def form():
    title = "Форма"
    return render_template("form.html", title=title, request=request)


@app.route("/calculator", methods=["GET", "POST"])
def calculator():
    title = "Квакулятор"
    result = ""
    if request.method == "POST":
        try:
            numA = int(request.form.get("numA", ""))
            numB = int(request.form.get("numB", ""))
        except ValueError:
            result = "Математические операции над буквами ещё не придумали!"
            return render_template("calculator.html", title=title, request=request, result=result, operators=OPERATORS)
        operator = request.form.get("operator", "")
        try:
            result = OPERATORS[operator](numA, numB)
        except KeyError:
            result = "Этой математической операции нет и никогда не было!"

    return render_template("calculator.html", title=title, request=request, result=result, operators=OPERATORS.keys())

@app.route("/phoneCheck", methods=["GET", "POST"])
def phoneCheck():
    title = "Проверка номера Телефона"
    if request.method == "GET":
        return render_template("phoneCheck.html", title=title)
    
    phone = request.form.get("phone", "")
    
    phoneCheckResult = phoneWorker.checkPhone(phone)

    if not phoneCheckResult:
        phone = phoneWorker.formatPhone(phone)
        return render_template("phoneCheck.html", title=title, request=request, phoneChecked=True, formattedPhone=phone)
    else:
        return render_template("phoneCheck.html", title=title, request=request, phoneChecked=True, error=phoneCheckResult)
