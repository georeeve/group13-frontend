# Setting up routes
from flask import (
    Blueprint,
    render_template,
    request,
    flash,
    redirect,
    url_for,
    make_response,
)
import requests

from utils.basket_util import get_basket, get_basket_data_items, set_basket

# request allows us to do profile?name= in browser

# initialise Blueprint
basket = Blueprint("basket", "basket")

# creating / routes

# routing to main basket page


@basket.route("/", methods=["GET"])
def basket_get():
    user_basket = get_basket(request)
    if not user_basket:
        flash("You do not have any items in your basket")
        return redirect(url_for("home.items_get"))

    items, total_price = get_basket_data_items(user_basket)
    return render_template("basket.html", items=items, total_price=total_price)


# adds items to the basket, also prompts user to log in
# if they add an item without being signed in
@basket.route("/update", methods=["POST"])
def add_item():
    data = request.get_json()
    user_basket = get_basket(request)

    item_id = data["itemId"]

    response = requests.get("http://localhost:8080/api/v1/items/" + item_id)
    item = response.json()

    new_quantity = max(min(int(data["quantity"]), item["quantity"]), 1)
    user_basket[item_id] = new_quantity

    res = make_response()
    return set_basket(res, user_basket)


# deleting items from the basket
@basket.route("/delete", methods=["POST"])
def delete_item():
    data = request.get_json()
    user_basket = get_basket(request)
    item_id = data["itemId"]
    del user_basket[item_id]
    res = make_response()
    return set_basket(res, user_basket)
