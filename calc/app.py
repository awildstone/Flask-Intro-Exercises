from flask import Flask, request
from operations import *

app = Flask(__name__)

@app.route('/')
def index():
    ''' Show the calculator form. '''
    return ''' 
    <html><body>
    <h1>Calculator</h1>
    <h2>Add</h2>
    <form action="/add">
        <input name="a">
        <input name="b">
        <button>Go</button>
      </form>
    <h2>Subtract</h2>
    <form action="/sub">
        <input name="a">
        <input name="b">
        <button>Go</button>
      </form>
    <h2>Multiply</h2>
    <form action="/mult">
        <input name="a">
        <input name="b">
        <button>Go</button>
      </form>
    <h2>Divide</h2>
    <form action="/div">
        <input name="a">
        <input name="b">
        <button>Go</button>
      </form>
    </body></html>
    '''

@app.route('/add')
def add_nums():
    ''' Add a & b and return result on page'''
    a = request.args.get('a')
    b = request.args.get('b')
    return f'<html><body><h1>{add(int(a), int(b))}</h1></body></html>'

@app.route('/sub')
def sub_nums():
    ''' Subtract a & b and display result on page'''
    a = request.args.get('a')
    b = request.args.get('b')
    return f'<html><body><h1>{sub(int(a), int(b))}</h1></body></html>'

@app.route('/mult')
def mult_nums():
    ''' Multiply a & b and display result on page'''
    a = request.args.get('a')
    b = request.args.get('b')
    return f'<html><body><h1>{mult(int(a), int(b))}</h1></body></html>'

@app.route('/div')
def div_nums():
    ''' Divide a & b and display result on page'''
    a = request.args.get('a')
    b = request.args.get('b')
    return f'<html><body><h1>{div(int(a), int(b))}</h1></body></html>'

# All Math

operators = {'add': add, 'sub': sub, 'mult': mult, 'div': div}

@app.route('/math/<type>')
def all_math(type):
    ''' Do math on a & b and display result on page'''
    a = request.args.get('a')
    b = request.args.get('b')
    return f'<html><body><h1>{operators[type](int(a), int(b))}</h1></body></html>'