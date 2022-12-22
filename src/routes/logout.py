# Setting up routes
from flask import Blueprint, request, redirect, url_for, flash

import requests

logout = Blueprint("logout", "logout")


# code for POSTing the logout and DELETE of a session/cookie,
# flash created for pop up message verifying that logout was successful
@logout.route("/", methods=["POST"])
def logout_post():
    token = request.cookies.get("token")
    response = requests.delete(
        "http://localhost:8080/api/v1/session",
        headers={"Authorization": "Bearer " + token},
    )
    if response.status_code == 200:
        flash("You have been logged out", "info")
        res = redirect(url_for("home.items_get"))
        res.delete_cookie("token")
        return res
