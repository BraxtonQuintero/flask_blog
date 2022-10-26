# Installation Link
# https://flask.palletsprojects.com/en/2.2.x/installation/

# Quickstart Link
# https://flask.palletsprojects.com/en/2.2.x/quickstart/

# Jinja Template 
# https://jinja.palletsprojects.com/en/3.1.x/templates/

# Flask WTF
# https://flask-wtf.readthedocs.io/en/1.0.x/

# Flask SQLAlchemy 
# https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/

# Flask-Migrate
# https://flask-migrate.readthedocs.io/en/latest/

# Import the Flask Class from the flask module
from flask import Flask
# Import SQLAlchemy and Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# import the Config class from the config module
from config import Config


# Create an instance of the Flask class - central object of the whole app
app = Flask(__name__)
# Configure the app using the Config class and the .from_object() method
app.config.from_object(Config)

# Create an instance of SQLAlchemy to represent our database
db = SQLAlchemy(app)
# Create an instance of Migrate to represent our migration engine
migrate = Migrate(app, db)

# import all of the routes from the routes module in the current folder
from . import routes, models

