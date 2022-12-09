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
def endpoint():
    response = requests.post('http://localhost:8080/api/v1/login', data={
        "email": request.form["email"],
        "password": request.form["password"] 
    })
    
    
    response_header= response.json()
    
    token = response_header["token"]
    args = request.args
    email = args.get()
    res = make_response(render_template("userProfile.html", name=email))
    res.set_cookie("token",token)
    print(token)
    print(res)
    return res
    
    
        
    

@login.route("/checkingtoken")
def cookies():
    
    res = make_response("Checking Cookie", 200)
    
    cookies = request.cookies
    
    token = cookies.get("token")
    print(token)
    
    return res


