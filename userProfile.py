from flask import Blueprint, render_template, request, url_for, make_response

import requests
import json

userprofile = Blueprint(__name__, "userprofile")


#Takes user to profile page, based on if they are an admin or not
@userprofile.route('/', methods=['GET', 'POST'])
def userProfile():

    #POST and patch for user information change
    if request.method == 'POST':
        form_data = request.form

        data = request.form.to_dict()

        for key, val in form_data.items():
            if val == '':
                del data[key]

        token = request.cookies.get('token')
        requests.patch('http://localhost:8080/api/v1/user',
                                json=data, headers={"Authorization": "Bearer " + token})

    #loads current user page
    userDict = load_userData()

    #loads get request for all users, used later for admin area
    allUsers = load_AllUsers()
    print(type(allUsers))

    #redirection for admin page or regular user page
    if userDict['admin'] is True:
        template = 'userProfileAdmin.html'
        userRes = make_response(render_template(template, user=userDict, allUsers=allUsers))
    else:
        template = 'userProfile.html'
        userRes = make_response(render_template(template, user=userDict))

    return userRes

#loads the user information
def load_userData():
    token = request.cookies.get('token')
    response = requests.get("http://localhost:8080/api/v1/user",
                            headers={"Authorization": "Bearer " + token})

    userDict = response.json()
    return userDict

#loads the information for all users which is then given to the adminpage
def load_AllUsers():
    token = request.cookies.get('token')
    response = requests.get("http://localhost:8080/api/v1/admin/users",
                            headers={"Authorization": "Bearer " + token})
    return response.json()
