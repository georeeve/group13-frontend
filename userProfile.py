from flask import Blueprint, render_template, request, url_for, make_response

import requests

userprofile = Blueprint(__name__, "userprofile")

@userprofile.route('/', methods = ['GET'])
def userProfile():
    token = request.cookies.get('token')
    response = requests.get("http://localhost:8080/api/v1/user", headers={"Authorization": "Bearer " + token})
    
    response_admin = response.json()
    name = response.json()["firstName"]

    print(response_admin)
    

    if response_admin["admin"] == True:

            print (response.json())
            adminRes = make_response(render_template('userProfileAdmin.html', name=name ))

            return adminRes

    else:
        print (response.json())
        userRes = make_response(render_template('userProfile.html', name=name))
        
        return userRes

