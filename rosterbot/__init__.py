from __future__ import print_function
from flask import abort, Flask, request
from os import environ
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import threading

app = Flask(__name__)
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

@app.route('/', methods = ['GET', 'POST'])
def eventbot():
    if request.form.get('token') != environ['SLACK_VERIFICATION_TOKEN']:
        abort(403)

    service = build('calendar', 'v3')

    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

    text = str(request.form.get('text')).lower()

    # If no parameter, the bot will display the next event
    events_result = service.events().list(calendarId='',
                                          timeMin=now, maxResults=1, singleEvents=True, orderBy='startTime').execute()
    # if text == 'today':
    #     events_result = service.events().list(calendarId='',
    #                                           timeMin=now, singleEvents=True, orderBy='startTime').execute()
    # if text == 'tomorrow':
    #     events_result = service.events().list(calendarId='',
    #                                           timeMin=now, singleEvents=True, orderBy='startTime').execute()
    # if text == 'week':
    #     events_result = service.events().list(calendarId='',
    #                                           timeMin=now, singleEvents=True, orderBy='startTime').execute()

    events = events_result.get('items', [])
    event_string = ''
    if not events:
        return 'No upcoming events found.'
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        event_string = str(start, event['summary'])
    return event_string
# def main_thread(text, url):
#     request_url = request.form.get('')
#     thr = threading.Thread(target=eventbot, args=[])
#     thr.start()
