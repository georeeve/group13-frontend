#Entry point for website

#importing Flask
from flask import Flask

#importing views/routes
from home import home

from userProfile import profile

from login import login

from register import register

#initialising app
app = Flask(__name__)

#calling route
app.register_blueprint(home, url_prefix="/home")

app.register_blueprint(profile, url_prefix= "/profile")

app.register_blueprint(login, url_prefix ="/login")

app.register_blueprint(register, url_prefix ="/register")

#setting port
if __name__ == '__main__':
    app.run(debug=True, port = 8000)