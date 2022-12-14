#Entry point for website

#importing Flask
from flask import Flask, request, make_response, render_template

#importing views/routes
from home import home

from login import login

from register import register

from apiRouting import apiRouting

#initialising app
app = Flask(__name__)

#calling route
app.register_blueprint(home, url_prefix="/home")


app.register_blueprint(login, url_prefix ="/login")

app.register_blueprint(register, url_prefix ="/register")

app.register_blueprint(apiRouting, url_prefix ="/apiRouting")


#setting port
if __name__ == '__main__':
    app.run(debug=True, port = 8000)