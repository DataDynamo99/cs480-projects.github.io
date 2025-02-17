from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to Justin's Homepage!"

@app.rout('/bry')
def bry():
    return "Welcome to Bryson's Page!"

@app.route('/marco')
def marco():
    return "Welcome! This is DeMarco's page!"

@app.route('/requestsdemo')
def reqdemo():
    r=requests.get('https://google.com')
    return("Get request to google.com returned: " + str(r.status_code))

@app.route('/steven')
def steven():
    return "Welcome! This is Steven's page!"

@app.route('/hello')
def hello():
    return 'Hello world!'


app.run(host='0.0.0.0')
