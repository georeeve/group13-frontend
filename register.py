#Setting up routes
from flask import Blueprint, render_template, request, jsonify, redirect, url_for

register = Blueprint(__name__, "register")

@register.route("/")
def signInLanding():
    #allows for passing of html to Python, can also pass variables INTO the html
    return render_template("register.html")