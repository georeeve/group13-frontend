# Entry point for website

# importing Flask
from flask import Flask

# importing views/routes
from src.routes.home import home

from src.routes.login import login

from src.routes.logout import logout

from src.routes.register import register

from src.routes.userprofile import userprofile

from src.routes.basket import basket

from src.routes.checkout import checkout

# from login import resetpassword


# initialising app
app = Flask(__name__)
# needed for Flash
app.secret_key = "the super secret key"

# calling routes
app.register_blueprint(home, url_prefix="/")

app.register_blueprint(login, url_prefix="/login")

app.register_blueprint(logout, url_prefix="/logout")

app.register_blueprint(register, url_prefix="/register")

app.register_blueprint(userprofile, url_prefix="/userprofile")

app.register_blueprint(basket, url_prefix="/basket")

app.register_blueprint(checkout, url_prefix="/checkout")


# setting port and initialising
if __name__ == "__main__":
    app.run(debug=True, port=8000)
