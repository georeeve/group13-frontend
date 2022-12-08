#Setting up routes
from flask import Blueprint, render_template, request, jsonify, redirect, url_for, make_response

register = Blueprint(__name__, "register")

@register.route("/")
def registering():
    #allows for passing of html to Python, can also pass variables INTO the html
    return render_template("register.html")

#COOOOOKIEEEEEE
@register.route("/registering")
def cookies():
    #Anything I would pass into return, can be passed into make_response
    res = make_response("Checking Cookie", 200)
    

    
    res.set_cookie(
                    "token", 
                   value="eyJhbGciOiJFUzI1NiJ9.eyJzdWIiOiIxMjM3MzA3NjY0ODcwOTMyNDgifQ.AN",
                   #expiry Age in seconds
                   #max_age=10,
                   #takes date/time object
                   expires = None,
                   #can specify the path
                   path="/",
                   #domain that can read cookie, can work with subdomains etc
                   domain=None,
                   #setting to true only allows HTTPS
                   secure=False,
                   #sets that cookie if cookie is only accessible via JS or HTTP
                   httponly=False,
                   #Limits scope of accessibility
                   #samesite=False
                   )
    
    res.set_cookie("Chocolate type", "dark")
    
    res.set_cookie("chewy", "yes")
    
    return res