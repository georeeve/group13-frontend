# Setting up routes
from flask import Blueprint, request, redirect, url_for

import requests

logout = Blueprint(__name__, "logout")


@logout.route("/", methods=['POST'])
def logout_post():
    token = request.cookies.get("token")
    response = requests.delete('http://localhost:8080/api/v1/session', headers={"Authorization": "Bearer " + token})
    if response.status_code == 200:
        res = redirect(url_for('home.getItems'))
        res.delete_cookie('token')
        return res
