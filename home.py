#Setting up routes
from flask import Blueprint, render_template, request, jsonify, redirect, url_for, make_response
import requests
#request allows us to do profile?name= in browser

#initialise Blueprint
home = Blueprint(__name__, "home")

#creating / route

# connect to api
@home.route("/", methods = ['GET'])
def getItems():
    response = requests.get('http://localhost:8080/api/v1/items')
    # print (response.json())
    items = response.json()
    res = render_template('index.html', items=items)
    return res

# @home.route("/getitem")
# def get_items(items):
#     results=[]

if __name__ == '__main__':
    home.run()
