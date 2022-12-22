#Entry point for website

#importing Flask
from flask import Flask, request, make_response, render_template

#importing views/routes
from home import home

from login import login

from logout import logout

from register import register

from basket import basket

from userProfile import userprofile

# from login import resetpassword


#initialising app
app = Flask(__name__)
#needed for Flash
app.secret_key = 'the super secret key'

#calling routes
app.register_blueprint(home, url_prefix="/")

app.register_blueprint(login, url_prefix="/login")

app.register_blueprint(logout, url_prefix="/logout")

app.register_blueprint(register, url_prefix="/register")

app.register_blueprint(basket, url_prefix="/basket")

app.register_blueprint(userprofile, url_prefix="/userprofile")



#setting port and initialising
if __name__ == '__main__':
    app.run(debug=True, port = 8000)
