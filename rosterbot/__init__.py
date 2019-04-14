from flask import abort, Flask, request
from os import environ

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def events():
    if request.form.get('token') != environ['SLACK_VERIFICATION_TOKEN']:
        abort(403)

    if request.form.get('text') == 'today':
        return 'The events happening today'

    return 'bet'
