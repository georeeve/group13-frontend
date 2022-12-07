#Setting up routes
from flask import Blueprint, render_template, request, jsonify, redirect, url_for

profile = Blueprint(__name__, "profile")

@profile.route("/")
def landing():
    #allows for passing of html to Python, can also pass variables INTO the html
    return render_template("userProfile.html")


@profile.route("/userprofile")
def userProfile():
    #we can use request.args as dictionary to access query parameters
    args = request.args
    #allows to get access to query parameter if it exists
    name = args.get('name')
    print(args)
    return render_template("userProfile.html", name=name)
    