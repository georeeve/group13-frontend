# Setting up routes
import requests
from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    make_response,
)

register = Blueprint("register", "register")


# route for loading registering page
@register.route("/")
def register_get():
    return render_template("register.html")


# creates user based on form inputs which are POSTed in JSON format to the server
@register.route("/createuser", methods=["GET", "POST"])
def create_user():
    response = requests.post(
        "http://localhost:8080/api/v1/user",
        json={
            "email": request.form["email"],
            "password": request.form["password"],
            "firstName": request.form["firstName"],
            "lastName": request.form["lastName"],
            "dob": request.form["dob"],
            "addressLine1": request.form["addressLine1"],
            "addressLine2": request.form["addressLine2"],
            "city": request.form["city"],
            "postCode": request.form["postCode"],
        },
    )

    # error message catching based on returned status code
    if response.status_code == 400:
        response_body = response.json()
        msg = response_body["message"]
        res = make_response(render_template("register.html", msg=msg))
        return res, msg

    # user will be created and taken to the user area once registered,
    # cookie created and set
    else:
        response_header = response.json()
        print(response_header)
        token = response_header["token"]

        res = redirect(url_for("home.items_get"))
        res.set_cookie("token", token, httponly=True, samesite="Strict")

        return res
