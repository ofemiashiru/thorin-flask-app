# import os
import os

# import the Flask class
# render template() function allows us to render data to a HTML file
from flask import Flask, render_template


# creating an instance of the Flask class and calling it app.
# the first argument is the name of the applications module.
# since we are using a since we're just using a single module,
# we can use __name__ which is a built-in Python variable.
# Flask needs this so that it knows where to look for templates
# and static files.
app = Flask(__name__)


# a decorator that states when we visit the specified route
# it should return the text hello world
# remember that a decorator modifies the function that it appears above

@app.route('/')
def index():
    # Flask expects to find the index.html file in a folder called templates
    return render_template('index.html')

# app.route()
# this is routing with the decorator(above and below) essentially
# the argument or route passed into the decorator will display the page
# our function returns when it is visited

# the route decorator binds the function beneath to itself so that whenever
# the route is called the function is also called.
# the functions beneath the decorators are also called Views.


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/careers')
def careers():
    return render_template('careers.html')


# __main__ is name of the default module in python. This is the first one that
# that we run
if __name__ == "__main__":
    # we run our app using the arguments passed to the app.run() method
    app.run(
        host=os.environ.get('IP', '0.0.0.0'),
        # default port that our site will be run on
        port=int(os.environ.get('PORT', '5000')),

        # we should never have debug=True in a production application or
        # submitting projects for assessment. debug=True is okay for
        # development and testing, but set it to debug=False when submitting.
        debug=True)