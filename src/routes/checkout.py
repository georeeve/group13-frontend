import requests
from flask import Blueprint, render_template, request, flash, redirect, url_for

from utils.basket_util import get_basket_data_items, get_basket

checkout = Blueprint("checkout", "checkout")


@checkout.route("/")
def checkout_get():
    token = request.cookies.get("token")

    if token is None:
        flash("Please sign in first", "info")
        return redirect(url_for("login.signin_get"))

    user_basket = get_basket(request)
    items, price = get_basket_data_items(user_basket)

    return render_template("checkout.html", items=items, total=price)


@checkout.route("/", methods=["POST"])
def checkout_post():
    token = request.cookies.get("token")
    user_basket = get_basket(request)

    response = requests.post(
        "http://localhost:8080/api/v1/checkout",
        json=user_basket,
        headers={"Authorization": "Bearer " + token},
    )
    if response.status_code == 200:
        flash("You have successfully checked out", "info")
        res = redirect(url_for("home.items_get"))
        res.delete_cookie("basket")
        return res
    else:
        items, price = get_basket_data_items(user_basket)
        return render_template("checkout.html", items=items)
