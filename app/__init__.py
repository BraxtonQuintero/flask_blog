# Installation Link
# https://flask.palletsprojects.com/en/2.2.x/installation/

# Quickstart Link
# https://flask.palletsprojects.com/en/2.2.x/quickstart/


# Import the Flask Class from the flask module
from flask import Flask

# Create an instance of the Flask class and give it the variable name 'app'
app = Flask(__name__)

# import all of the routes from the routes module in the current folder
from . import routes