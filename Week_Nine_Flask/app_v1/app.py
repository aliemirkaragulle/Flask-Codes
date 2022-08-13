# We can change the URL by adding /?name=David, but our page stays the same
# We'll need to change our code in app.py:
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")

# We can use the request variable from the Flask library to get the arguments from the request.
# Then, we can pass in the name variable as an argument to the render_template function
def index():
    name = request.args.get("name")
    return render_template("index.html", name = name)

# In our HTML file, we can include that variable with two curly braces

# Now, if we visit our URL with our input, we'll see that the page's content now includes it.
# To make sure our templates are reloaded, we can press control and C in the terminal window to exit Flask, and restart our server with flask run again