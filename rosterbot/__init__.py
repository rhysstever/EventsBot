from __future__ import print_function
from flask import abort, Flask, request
from os import environ
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

app = Flask(__name__)
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

@app.route('/', methods = ['GET', 'POST'])
def events():
    if request.form.get('token') != environ['SLACK_VERIFICATION_TOKEN']:
        abort(403)

    # creds = None
    # # The file token.pickle stores the user's access and refresh tokens, and is
    # # created automatically when the authorization flow completes for the first
    # # time.
    # if os.path.exists('token.pickle'):
    #     with open('token.pickle', 'rb') as token:
    #         creds = pickle.load(token)
    # # If there are no (valid) credentials available, let the user log in.
    # if not creds or not creds.valid:
    #     if creds and creds.expired and creds.refresh_token:
    #         creds.refresh(Request())
    #     else:
    #         flow = InstalledAppFlow.from_client_secrets_file(
    #             'credentials.json', SCOPES)
    #         creds = flow.run_local_server()
    #     # Save the credentials for the next run
    #     with open('token.pickle', 'wb') as token:
    #         pickle.dump(creds, token)

    service = build('calendar', 'v3')

    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

    text = str(request.form.get('text')).lower()
    events_result = service.events().list(calendarId='', timeMin=now, maxResults=1, singleEvents=True, orderBy='startTime').execute()

    events = events_result.get('items', [])
    event_string = ''
    if not events:
        return 'No upcoming events found.'
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        event_string = str(start, event['summary'])

    return event_string

