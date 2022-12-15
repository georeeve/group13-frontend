#Setting up routes
from flask import Blueprint, render_template, request, jsonify, redirect, url_for, make_response
import requests
#request allows us to do profile?name= in browser

#initialise Blueprint
checkout = Blueprint(__name__, "checkout")

#creating / route

@checkout.route("/")
def basket():
 
    
    #allows for passing of html to Python, can also pass variables INTO the html
    return render_template("checkout.html")

