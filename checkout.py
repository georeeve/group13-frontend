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

if __name__ == '__main__':
    checkout.run()
