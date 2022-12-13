#Setting up routes
import json
import requests
from flask import Blueprint, render_template, request, jsonify, redirect, url_for, make_response

register = Blueprint(__name__, "register")

@register.route("/")
def registering():
    #allows for passing of html to Python, can also pass variables INTO the html
    return render_template("register.html")


@register.route("/createuser", methods = ['POST'])
def create_user():
    response = requests.post('http://localhost:8080/api/v1/user', json={
        "email": request.form["email"],
        "password": request.form["password"],
        "firstName": request.form["firstName"],
        "lastName": request.form["lastName"],
        "dob": request.form["dob"]
    })

    if response.status_code == 400:
        res = make_response(render_template("error400.html"))
        return res
    
    else:
        response_header= response.json()
        print(response_header)
        token = response_header["token"]
        res = make_response(render_template("userProfile.html"))
        res.set_cookie("token",token)
        print(token)
        return res, token

