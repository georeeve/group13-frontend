from flask import Blueprint, render_template, request, url_for, make_response

import requests

userprofile = Blueprint(__name__, "userprofile")

@userprofile.route('/', methods = ['GET', 'PATCH'])
def userProfile():
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

    print(response_admin)
    

    if response_admin["admin"] == True:

            usersResponse = requests.get("http://localhost:8080/api/v1/users", headers={"Authorization": "Bearer " + token})
            users = usersResponse.json()
            print(users)
            adminRes = make_response(render_template('userProfileAdmin.html', email=email, name=name, lastname=lastname, address=address, addressTwo=addressTwo, city=city, postCode=postCode ))

            return adminRes

    else:
        if request.method == 'GET':
            userRes = make_response(render_template('userProfile.html',email=email,name=name, lastname=lastname, address=address, addressTwo=addressTwo, city=city, postCode=postCode))
            return userRes

        elif request.method == 'PATCH':
            update = requests.post('http://localhost:8080/api/v1/user', json={
            "email": request.form["email"],
            "password": request.form["password"],
            "firstName": request.form["firstName"],
            "lastName": request.form["lastName"],
            "dob": request.form["dob"],
            "addressLine1": request.form["addressLine1"],
            "addressLine2": request.form["addressLine2"],
            "city": request.form["city"],
            "postCode": request.form["postCode"]
            })

            return update
        
       


