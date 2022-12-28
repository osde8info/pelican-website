from datetime import datetime

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World! ' + datetime.now().strftime("%c")

@app.route('/about')
def about():
    return 'About ' + datetime.now().strftime("%c")
