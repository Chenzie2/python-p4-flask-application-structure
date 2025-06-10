from flask import Flask

# Step 1: Create Flask app instance
app = Flask(__name__)

# Step 2: Route for the home page
@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'

# Step 3: Dynamic route using a variable in the URL
@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

# Step 4: Run the development server
if __name__ == '__main__':
    app.run(port=5555, debug=True)
