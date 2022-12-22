import requests
from flask import Blueprint, render_template, request, flash, redirect, url_for

from basket_utils import get_basket_data_items, get_basket

checkout = Blueprint(__name__, "checkout")


@checkout.route("/")
def get_checkout():
    token = request.cookies.get('token')

    if token is None:
        flash("Please sign in first", "info")
        return redirect(url_for('login.signInLanding'))

    user_basket = get_basket(request)
    items, price = get_basket_data_items(user_basket)

    return render_template("checkout.html", items=items)

@checkout.route("/", methods=["POST"])
def post_checkout():
    token = request.cookies.get("token")
    user_basket = get_basket(request)

    response = requests.post("http://localhost:8080/api/v1/checkout", json=user_basket, headers={"Authorization": "Bearer " + token})
    if response.status_code == 200:
        res = redirect(url_for("home.getItems"))
        res.delete_cookie("basket")
        return res
    else:
        items, price = get_basket_data_items(user_basket)
        return render_template("checkout.html", items=items)

if __name__ == '__main__':
    checkout.run()
