# import os
import os


# using the os.path.exists() we can check if a file exists and responds
# accordingly based on wheter it was found or not - if found it will be
# imported

if os.path.exists('env.py'):
    import env


# enable application to us json
import json

# import the **Flask** class from flask

# import **render_template()** function allows us to render data to a HTML file

# import **request** the request module will handle the type of method we use
# (GET or POST) and it will also contain our form object when we post it

# import **flash** allows us to feed back a message to the user or flash a
# message to them
# to use flash use flashed messages, we need to create a secret key, because
# Flask cryptographically signs all of the messages for security purposes.
# we need to provide a secret key that Flask can use to sign the messages

from flask import Flask, render_template, request, flash


# creating an instance of the Flask class and calling it app.
# the first argument is the name of the applications module.
# since we are using a since we're just using a single module,
# we can use __name__ which is a built-in Python variable.
# Flask needs this so that it knows where to look for templates
# and static files.
app = Flask(__name__)

# brings in the secret key
app.secret_key = os.environ.get('SECRET_KEY')

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

    data = []

    with open('data/company.json', 'r') as json_data:
        data = json.load(json_data)

    # a second argument is entered with a name of our choice so that we can
    # pass data from the server side to our client side. Above there is a
    # second argument called page_title which we will pass to the client side.

    # you can add as many arguments here as you like, just remember to use
    # snake_case when naming your variables
    return render_template('about.html', page_title='About', company=data)


# creating a new decorater to help navigate to a customer url
# whenever we look at our about page with something after it, it will
# passed into this view
@app.route('/about/<character_name>')
def about_character(character_name):
    character = {}

    with open('data/company.json', 'r') as json_data:
        data = json.load(json_data)

        for obj in data:
            if obj["url"] == character_name:
                character = obj

    return render_template('character.html', character=character)

# in order for our route to handle get and post requests we have to specify
# these methods as a spearate kwargs argument below


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    # this wiil check if the method is a POST or GET. if it is a POST it will
    # action the below
    if request.method == 'POST':

        # request.form is returned and because this is a dictionary, we can
        # actually use a standard Python method (.get()) of accessing the keys
        # for that dictionary. If I print(request.form.get("name")), this will
        # allow us to get the'name' value from our form.
        print(request.form.get('name'))

        # we can also access data from the reqeust.form object with square
        # notation.
        print(request.form['email'])

        # the main difference between the above ways of getting information
        # from the dictionary is that the get.() method will return None if
        # there is no matching key where as the square notation method will
        # throw an exception if the key is not mataching
        flash('Thanks {} we have recieved a message'.format(
            request.form.get("name")))
    return render_template('contact.html', page_title='Contact')


@ app.route('/careers')
def careers():
    return render_template('careers.html', page_title='Careers')


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
