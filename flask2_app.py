
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
app = Flask(__name__)

@app.route('127.0.0.1')
def hello_world():
   return 'Hello World'

#app.run(host = '127.0.0.1')
#if __name__ == '__main__':
#   app.run()