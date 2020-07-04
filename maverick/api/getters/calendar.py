import httplib2

from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow
from oauth2client import tools
from datetime import datetime, timedelta, date
import pandas as pd

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

class calendar_fun:
    
    def __init__(self):
        
        FLOW = OAuth2WebServerFlow(
            client_id='480509766318-n95p64vh8budq9megb29tiekuumvho4r.apps.googleusercontent.com',
            client_secret='96St0SCvltFDQWSCeczGSt1F',
            scope='https://www.googleapis.com/auth/calendar',
            user_agent='maverick/2.0')
        
        storage = Storage('calendar.dat')
        credentials = storage.get()
        if credentials is None or credentials.invalid == True:
          flags = tools.argparser.parse_args(args=[])
          credentials = tools.run_flow(FLOW, storage, flags)
          
        http = httplib2.Http()
        http = credentials.authorize(http)
        
        self.service = build('calendar', 'v3', http=http, developerKey='AIzaSyD8hYjZkcTfohL4wCdFnlVVVj3xyrEBlt0')

    def get_result(self, intent, parameters):
        if (intent == 'get_events'):
            return self.get_events(parameters)
        else:
            return self.create_event(parameters)

    def get_events(self, params):
        # now = datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        # print('Getting the upcoming 10 events')
        events_result = self.service.events().list(calendarId='primary', timeMin=params['date'], maxResults=10, singleEvents=True, orderBy='startTime').execute()
        events = events_result.get('items', [])
        events_list = []
        if not events:
            return {'msg': 'No upcoming events found.', 'data': None}
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            end = event['end'].get('dateTime', event['end'].get('date'))
            events_list.append([event['summary'], event.get('location', ''), start, end])
        data = pd.DataFrame(events_list, columns=['Name', 'Location', 'Start Time', 'Ending Time'])
        # return data
        return {'msg': None, 'data': data.to_dict('list')}
        # return data.to_string()
        # return data.to_string()
    
    def create_event(self, params):
        GMT_TIME = '+05:30'
        startdate = params['date'][:11] + params['time'][11:]
        t=params['time'][11:16]
        final = str(pd.to_datetime(t, format='%H:%M') + timedelta(hours=0.5))[11:]
        endtime = params['date'][:11] + final + GMT_TIME
        event = {'summary': params['event_title'],
                 'start': {
                     'dateTime': startdate,
                     },
                 'end': {
                     'dateTime': endtime,
                     },
                 }
        if params.get('location'):
            event['location'] = params['location']
        try:
            self.service.events().insert(calendarId='primary', sendUpdates='all', body=event).execute()
            return {'msg': 'Event added successfully.', 'data': None}
        except:
            return{'msg': 'Error in adding event', 'data': None}
