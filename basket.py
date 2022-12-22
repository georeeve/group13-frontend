#Setting up routes
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for, make_response
import requests
import json
import base64

from basket_utils import get_basket_data_items, get_basket, set_basket

#request allows us to do profile?name= in browser

#initialise Blueprint
basket = Blueprint(__name__, "basket")

#creating / route

@basket.route("/", methods = ['GET','POST'])
def basketlanding():
    user_basket = get_basket(request)

    items, total_price = get_basket_data_items(user_basket)
    return render_template("basket.html", items=items, total_price=total_price)


@basket.route("/update", methods=['POST'])
def add_item():
    data = request.get_json()
    user_basket = get_basket(request)

    item_id = data['itemId']

    res = requests.get("http://localhost:8080/api/v1/items/" + item_id)
    item = res.json()

    new_quantity = int(data['quantity'])
    total_quantity = max(min(new_quantity, item['quantity']), 1)
    user_basket[item_id] = total_quantity

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
