#Setting up routes
from flask import Blueprint, render_template, request, jsonify, redirect, url_for, make_response
import requests
#request allows us to do profile?name= in browser

#initialise Blueprint
basket = Blueprint(__name__, "basket")

#creating / route

@basket.route("/", methods = ['GET','POST'])
def basketlanding():
    return render_template("basket.html")
    

 





