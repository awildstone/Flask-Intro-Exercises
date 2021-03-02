from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def root():
    """ Displays the root homepage. """
    html ="""<html><body><h1>Welcome</h1>
    <p><a href="/welcome">Welcome</a>
    <p><a href="/welcome/home">Welcome Home</a>
    <p><a href="/welcome/back">Welcome Back</a>
    </body></html>
    """
    return html

@app.route('/welcome')
def welcome():
    """Return simple "Welcome" Greeting."""
    html = "<html><body><h1>Welcome</h1></body></html>"
    return html

@app.route('/welcome/home')
def welcome_home():
    """Return simple "Welcome Home" Greeting."""
    html = "<html><body><h1>Welcome Home</h1></body></html>"
    return html

@app.route('/welcome/back')
def welcome_back():
    """Return simple "Welcome Back" Greeting."""
    html = "<html><body><h1>Welcome Back</h1></body></html>"
    return html