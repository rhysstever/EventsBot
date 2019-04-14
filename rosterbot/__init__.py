from flask import abort, Flask, request
from os import environ

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def events():
    if request.form.get('token') != environ['SLACK_VERIFICATION_TOKEN']:
        abort(403)

    text = str(request.form.get('text')).lower()

    if text == 'today':
        return 'The events happening today'

    if text == 'this week':
        return 'The events happening this week'

    if text == 'next week':
        return 'The events happening next week'

    return 'bet'
