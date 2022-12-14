#Setting up routes
from flask import Blueprint, render_template, request, jsonify, redirect, url_for, make_response

register = Blueprint(__name__, "register")

@register.route("/")
def registering():
    #allows for passing of html to Python, can also pass variables INTO the html
    return render_template("register.html")


@register.route("/createuser", methods = ['GET', 'POST'])
def signup():
    data = request.json()

    new_user = User(
        email=data.get('email')
    )


