#Setting up routes
from flask import Blueprint, render_template, request, jsonify, redirect, url_for, make_response
import requests
import math
#request allows us to do profile?name= in browser

#initialise Blueprint
home = Blueprint(__name__, "home")

#creating / route

# connect to api
@home.route("/", methods = ['GET'])
def getItems():
    response = requests.get('http://localhost:8080/api/v1/items')
    # print (response.json())
    categoriesRes = requests.get('http://localhost:8080/api/v1/categories')
    categories = categoriesRes.json()
    items = response.json()
    pages = math.ceil(len(items)/24)
    args = request.args
    start = 0
    end = 24
    length = len(items)
    if args.get('start') is not None:
        start = int(args.get('start'))
    if args.get('end') is not None:
        end = int(args.get('end'))
    if args.get('length') is not None:
        length = int(args.get('length'))

    svg = './static/assets/basket.svg'
    res = render_template('index.html', items=items, pages=pages, start=start, end=end, length=length, svg=svg, categories=categories)
    return res

# @home.route("/getitem")
# def get_items(items):
#     results=[]

if __name__ == '__main__':
    home.run()
