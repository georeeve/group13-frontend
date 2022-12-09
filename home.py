#Setting up routes
from flask import Blueprint, render_template, request, jsonify, redirect, url_for

#request allows us to do profile?name= in browser

#initialise Blueprint
home = Blueprint(__name__, "home")

#creating / route
@home.route("/")
def landing():
    #allows for passing of html to Python, can also pass variables INTO the html
    return render_template("index.html")
