# First, we'll import Flask from the flask library, along with some other functions
from flask import Flask, render_template, request

# Then, we'll create an app variable by giving our Python file's name to the Flask variable

# Turn this file into a Flask application
app = Flask(__name__)

# Next, we'll label a function for the / route with @app.route from Flask
# The @ symbol in Python is called a decorator, which modifies a function

# Define a router for slash (Decorator)
@app.route("/")

# Finally, our index() function will just render a template, or return HTML code, from the file index.html

# Render the file "index.html"
def index():
    return render_template("index.html")