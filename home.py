# Setting up routes
import base64
import json

from flask import Blueprint, render_template, request, make_response
import requests
import math
# request allows us to do profile?name= in browser

# initialise Blueprint
home = Blueprint(__name__, "home")


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


@home.route("/basketadd", methods=['POST'])
def add_item():
    data = request.get_json()
    basket_cookie = request.cookies.get("basket")
    basket = json.loads(base64.b64decode(basket_cookie.encode('ascii')).decode('ascii')) if basket_cookie is not None else {}
    item_id = data['itemId']
    current_quantity = basket[item_id] if basket.get(item_id) is not None else 0
    to_add_quantity = int(data['quantity'])
    basket[item_id] = current_quantity + to_add_quantity
    res = make_response()
    res.set_cookie("basket", base64.b64encode(json.dumps(basket).encode('ascii')).decode('ascii'), samesite="Strict")

    return res


if __name__ == '__main__':
    home.run()
