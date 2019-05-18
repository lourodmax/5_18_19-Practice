
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
#from flask import request
#import git

app = Flask(__name__)

app.run(host='/')

@app.route('/')
def hello_world():
    return 'Test3!'

#@app.route('/something')

#def something():
#    return 'TestRoute!'

#@app.route('/webhook', methods=['POST'])
#def webhook():
#    if request.method == 'POST':
#        repo = git.Repo('./myproject')
#        origin = repo.remotes.origin
#        repo.create_head('master',
#    origin.refs.master).set_tracking_branch(origin.refs.master).checkout()
#        origin.pull()
#        return '', 200
#    else:
#        return '', 400