#Setting up routes
from flask import Blueprint, render_template, request, flash, redirect, url_for
import requests
import json
import base64
#request allows us to do profile?name= in browser

#initialise Blueprint
basket = Blueprint(__name__, "basket")

#creating / route

@basket.route("/", methods = ['GET','POST'])
def basketlanding():

    signIn = request.cookies.get('token')
    
    if signIn == None:
        flash("Please sign in first", "info")
        res = redirect(url_for('login.signInLanding'))
        return res
    
    else:
        
        basket_cookie = request.cookies.get("basket")
        basket = json.loads(base64.b64decode(basket_cookie.encode('ascii')).decode('ascii')) if basket_cookie is not None else {}
    
        items = []

        for item, quantity in basket.items():
            response = requests.get('http://localhost:8080/api/v1/items/' + item)
            items.append(response.json())

        return render_template("basket.html", items=items)

 





