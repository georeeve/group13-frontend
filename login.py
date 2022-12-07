#Setting up routes
from flask import Blueprint, render_template, request, jsonify, redirect, url_for

login = Blueprint(__name__, "login")

@login.route("/")
def signInLanding():
    #allows for passing of html to Python, can also pass variables INTO the html
    return render_template("login.html")

@login.route("/login")
def goToRegister():
    return redirect(url_for("register.html"))



