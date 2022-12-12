#Setting up routes
from flask import Blueprint, render_template, request, jsonify, redirect, url_for, make_response

import requests

from register import register

login = Blueprint(__name__, "login")

@login.route("/")
def signInLanding():
    #allows for passing of html to Python, can also pass variables INTO the html
    return render_template("login.html")


@login.route("/success", methods = ['POST'])
def success():
    response = requests.post('http://localhost:8080/api/v1/login', json={
        "email": request.form["email"],
        "password": request.form["password"] 
    })
     
    response_header= response.json()
    print(response_header)
    token = response_header["token"]
    res = make_response(render_template("userProfile.html"))
    res.set_cookie("token",token)
    print(token)

    return res, token
    