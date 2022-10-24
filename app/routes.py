from app import app 

# Create a route for our app
@app.route('/')
def index():
    return 'Hello this is the index route!'


@app.route('/posts')
def posts():
    return 'Posts will eventually be on this page.'