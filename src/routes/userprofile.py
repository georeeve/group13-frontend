from flask import Blueprint, render_template, request, make_response

import requests

userprofile = Blueprint("userprofile", "userprofile")


# Takes user to profile page, based on if they are an admin or not
@userprofile.route("/", methods=["GET", "POST"])
def userprofile_get():
    # POST and patch for user information change
    if request.method == "POST":
        form_data = request.form
        data = request.form.to_dict()
        for key, val in form_data.items():
            if val == "":
                del data[key]

        token = request.cookies.get("token")

        if "mgt-submit" in form_data:
            data["id"] = form_data.get("id")
            requests.patch(
                "http://localhost:8080/api/v1/admin/users",
                json=data,
                headers={"Authorization": "Bearer " + token},
            )

        if "personal-submit" in form_data:
            requests.patch(
                "http://localhost:8080/api/v1/user",
                json=data,
                headers={"Authorization": "Bearer " + token},
            )

    # loads current user page
    user_dict = load_user_data()

    # loads get request for all users, used later for admin area
    all_users = load_all_users()

    # redirection for admin page or regular user page
    if user_dict["admin"] is True:
        template = "user-profile-admin.html"
        userRes = make_response(
            render_template(template, user=user_dict, allUsers=all_users)
        )
    else:
        template = "user-profile.html"
        userRes = make_response(render_template(template, user=user_dict))

    return userRes


# loads the user information


def load_user_data():
    token = request.cookies.get("token")
    response = requests.get(
        "http://localhost:8080/api/v1/user",
        headers={"Authorization": "Bearer " + token},
    )

    user_dict = response.json()
    return user_dict


# loads the information for all users which is then given to the adminpage


def load_all_users():
    token = request.cookies.get("token")
    response = requests.get(
        "http://localhost:8080/api/v1/admin/users",
        headers={"Authorization": "Bearer " + token},
    )
    return response.json()
