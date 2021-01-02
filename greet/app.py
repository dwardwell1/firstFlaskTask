from flask import Flask, request

app = Flask(__name__)


@app.route('/welcome')
def welcome():
    """ return simple "Welcome" greeting """
    return "welcome"

@app.route('/welcome/home')
def home():
    """ return simple "Welcome" greeting """
    return "welcome home"

@app.route('/welcome/back')
def back():
    """ return simple "Welcome" greeting """
    return "welcome back"

