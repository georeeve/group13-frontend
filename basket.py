#Setting up routes
from flask import Blueprint, render_template, request, jsonify, redirect, url_for, make_response
import requests
import json
import base64
#request allows us to do profile?name= in browser

#initialise Blueprint
basket = Blueprint(__name__, "basket")

#creating / route

@basket.route("/", methods = ['GET','POST'])
def basketlanding():
    basket_cookie = request.cookies.get("basket")
    user_basket = json.loads(base64.b64decode(basket_cookie.encode('ascii')).decode('ascii')) if basket_cookie is not None else {}

    items = []
    total_price = 0
    for item, quantity in user_basket.items():
        response = requests.get('http://localhost:8080/api/v1/items/' + item)
        data_item = response.json()
        data_item['selected_quantity'] = quantity
        items.append(data_item)
        total_price += data_item['price'] * quantity

    return render_template("basket.html", items=items, total_price=total_price)


@basket.route("/update", methods=['POST'])
def add_item():
    data = request.get_json()
    user_basket = get_basket(request)
    item_id = data['itemId']
    new_quantity = int(data['quantity'])
    user_basket[item_id] = new_quantity
    res = make_response()
    return set_basket(res, user_basket)


@basket.route("/delete", methods=['POST'])
def delete_item():
    data = request.get_json()
    user_basket = get_basket(request)
    item_id = data['itemId']
    del user_basket[item_id]
    res = make_response()
    return set_basket(res, user_basket)


def get_basket(req):
    basket_cookie = req.cookies.get("basket")
    return json.loads(base64.b64decode(basket_cookie.encode('ascii')).decode('ascii')) if basket_cookie is not None else {}


def set_basket(res, user_basket):
    res.set_cookie("basket", base64.b64encode(json.dumps(user_basket).encode('ascii')).decode('ascii'), samesite="Strict")
    return res
