from flask import render_template 
from app import app 

# Create a route for our app
@app.route('/')
def index():
    user_info = { 
        'username': 'brians',
        'email': 'brians@codingtemple.com'
    }
    return render_template('index.html')


@app.route('/posts')
def posts():
    return 'Posts will eventually be on this page.'