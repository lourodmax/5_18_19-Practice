
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Test3!'

@app.route('/something')
def something():
    return 'TestRoute!'