import base64
import json

import requests


def get_basket(req):
    basket_cookie = req.cookies.get("basket")
    return json.loads(base64.b64decode(basket_cookie.encode('ascii')).decode('ascii')) if basket_cookie is not None else {}


def set_basket(res, user_basket):
    res.set_cookie("basket", base64.b64encode(json.dumps(user_basket).encode('ascii')).decode('ascii'), samesite="Strict")
    return res


def get_basket_data_items(user_basket):
    items = []
    total_price = 0.0
    for item, quantity in user_basket.items():
        response = requests.get('http://localhost:8080/api/v1/items/' + item)
        data_item = response.json()
        data_item['selected_quantity'] = quantity
        items.append(data_item)
        total_price += data_item['price'] * quantity
    return items, total_price
