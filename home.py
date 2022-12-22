# Setting up routes
import base64
import json

from flask import Blueprint, render_template, request, make_response
import requests
import math
# request allows us to do profile?name= in browser

# initialise Blueprint
home = Blueprint(__name__, "home")

#route for main home page, also gets the items from the database for rendering onto the home page
@home.route("/", methods = ['GET'])
def getItems():
    response = requests.get('http://localhost:8080/api/v1/items')
    #print (response.json())
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

    if args.get('category') is not None:
        print(items)

        items = list(filter(lambda item: item['category']['id'] == int(args.get('category')), items))
        print(items)

    res = render_template('index.html', items=items, pages=pages, start=start, end=end, length=length, categories=categories)
    return res

#routing for add item button to the basket 
@home.route("/add", methods=['POST'])
def add_item():
    data = request.get_json()
    #gets the current basket cookie
    basket_cookie = request.cookies.get("basket")
    basket = json.loads(base64.b64decode(basket_cookie.encode('ascii')).decode('ascii')) if basket_cookie is not None else {}

    item_id = data['itemId']

    res = requests.get("http://localhost:8080/api/v1/items/" + item_id)
    item = res.json()

    current_quantity = basket[item_id] if basket.get(item_id) is not None else 0
    to_add_quantity = int(data['quantity'])
    total_quantity = max(min(current_quantity + to_add_quantity, item['quantity']), 1)

    basket[item_id] = total_quantity

    res = make_response()
    #wsets the json of the current basket into the cookie, saving the currently added items
    res.set_cookie("basket", base64.b64encode(json.dumps(basket).encode('ascii')).decode('ascii'), samesite="Strict")
    return res

if __name__ == '__main__':
    home.run()
