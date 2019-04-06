from flask import abort, Flask, request
from os import environ

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def create_roster():
    if request.form.get('token') != environ['SLACK_VERIFICATION_TOKEN']:
        abort(403)
    return 'A roster has been created'

@app.route('/', methods = ['GET', 'POST'])
def addplayer():
    if request.form.get('token') != environ['SLACK_VERIFICATION_TOKEN']:
        abort(403)
    return 'A '

@app.route('/', methods = ['GET', 'POST'])
def addevent():
    if request.form.get('token') != environ['SLACK_VERIFICATION_TOKEN']:
        abort(403)
    return 'An event has been added'