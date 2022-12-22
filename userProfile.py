from flask import Blueprint, render_template, request, url_for, make_response

import requests
import json

userprofile = Blueprint(__name__, "userprofile")


@userprofile.route('/', methods=['GET', 'POST'])
def userProfile():
    userDict, admin = load_userData()
    print(userDict, admin)

    # allUsers = load_AllUsers()
    # print(type(allUsers))

    if request.method == 'GET':
        template = 'userProfile.html' if not admin else 'userProfileAdmin.html'
        userRes = make_response(render_template(template, user=userDict))
        return userRes

    elif request.method == 'POST':
        form_data = request.form

        data = request.form.to_dict()

        for key, val in form_data.items():
            if val == '':
                del data[key]

        token = request.cookies.get('token')
        update = requests.patch('http://localhost:8080/api/v1/user',
                                json=data, headers={"Authorization": "Bearer " + token})

        userDict = load_userData()

        template = 'userProfile.html' if not admin else 'userProfileAdmin.html'
        userRes = make_response(render_template(template, user=userDict))
        return userRes


def load_userData():
    token = request.cookies.get('token')
    response = requests.get("http://localhost:8080/api/v1/user",
                            headers={"Authorization": "Bearer " + token})

    userDict = response.json()
    return userDict, userDict["admin"]


def load_AllUsers():
    token = request.cookies.get('token')
    response = requests.get("http://localhost:8080/api/v1/admin/users",
                            headers={"Authorization": "Bearer " + token})

    return response.json()
