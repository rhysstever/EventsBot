from flask import abort, Flask, request
from os import environ

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def hi():
    if request.form.get('token') != environ['SLACK_VERIFICATION_TOKEN']:
        abort(403)
    return 'Hi'

@app.route('/', methods = ['GET', 'POST'])
def createRoster():
    if request.form.get('token') != environ['SLACK_VERIFICATION_TOKEN']:
        abort(403)
    return 'A roster has been created'