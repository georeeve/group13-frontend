#Setting up routes
from flask import Blueprint, render_template, request, jsonify, redirect, url_for, make_response
import json

import requests

from register import register

login = Blueprint(__name__, "login")

@login.route("/")
def signInLanding():
 
    
    #allows for passing of html to Python, can also pass variables INTO the html
    return render_template("login.html")


@login.route("/session", methods = ['GET', 'POST'])
def signin():

    msg = ""

    response = requests.post('http://localhost:8080/api/v1/session', json={
        "email": request.form["email"],
        "password": request.form["password"] 
    })


    if response.status_code == 200:
     
        response_header= response.json()
        print(response_header)
        token = response_header["token"]
        res = make_response(render_template("userProfile.html"))
  
        print(token)
        
        response = requests.get("http://localhost:8080/api/v1/user", headers={"Authorization": "Bearer " + token})
        response_name = response.json()
        
        
        if response_name["admin"] == True:
            
            
            print (response.json())
            firstName = response.json()['firstName']
            adminRes = make_response(render_template('userProfileAdmin.html', firstName=firstName))
            adminRes.set_cookie("token", token)
            
            return adminRes

        else:
            print (response.json())
            firstName = response.json()['firstName']
            userRes = make_response(render_template('userProfile.html', firstName=firstName))
            userRes.set_cookie("token",token)
        
            return userRes

    elif response.status_code == 401:
        msg = "Incorrect email and/or password, please try again"
        res = make_response(render_template("login.html", msg=msg))
        return res


