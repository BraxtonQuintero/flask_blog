# Installation Link
# https://flask.palletsprojects.com/en/2.2.x/installation/

# Quickstart Link
# https://flask.palletsprojects.com/en/2.2.x/quickstart/


# Import the Flask Class from the flask module
from flask import Flask

# Create an instance of the Flask class and give it the variable name 'app'
app = Flask(__name__)

# Create a route using the @app.route to trigger function based on endpoint
@app.route('/')
def index():
    return 'Hello this is the index route!'

# Add another route
@app.route('/posts')
def posts():
    return 'Posts will eventually be on this page.'

