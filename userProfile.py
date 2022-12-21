from flask import Blueprint, render_template, request, url_for, make_response

import requests
import json

userprofile = Blueprint(__name__, "userprofile")

@userprofile.route('/', methods = ['GET', 'POST'])
def userProfile():
    userRes = load_userData()
    # print(response_admin)
    

    # if response_admin["admin"] == True:

    #         usersResponse = requests.get("http://localhost:8080/api/v1/users", headers={"Authorization": "Bearer " + token})
    #         users = usersResponse.json()
    #         print(users)
    #         adminRes = make_response(render_template('userProfileAdmin.html', email=email, name=name, lastname=lastname, address=address, addressTwo=addressTwo, city=city, postCode=postCode ))

    #         return adminRes

    # else:
    if request.method == 'GET':
        return userRes

    elif request.method == 'POST':
        form_data = request.form
        
        data = request.form.to_dict()

        for key, val in form_data.items():
            if val == '':
                del data[key]
        
        token = request.cookies.get('token')
        update = requests.patch('http://localhost:8080/api/v1/user', json=data, headers={"Authorization": "Bearer " + token})
            
        userRes = load_userData()
        return userRes

        
        
def load_userData():
    token = request.cookies.get('token')
    response = requests.get("http://localhost:8080/api/v1/user", headers={"Authorization": "Bearer " + token})
    
    response_admin = response.json()
    email = response.json()["email"]
    name = response.json()["firstName"]
    lastname = response.json()["lastName"]
    address = response.json()["addressLine1"]
    addressTwo = response.json()["addressLine2"]
    city = response.json()["city"]
    postCode = response.json()["postCode"]

    userRes = make_response(render_template('userProfile.html',email=email,name=name, lastname=lastname, address=address, addressTwo=addressTwo, city=city, postCode=postCode))
    return userRes