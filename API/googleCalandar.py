from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
from DataBase.dynamoDB import Database
import bcrypt



class GoogleCanlandarAPI:
    def __init__(self):
        self.connect_calandar()
        self.db = Database()

    def connect_calandar(self):
        scopes = ['https://www.googleapis.com/auth/calendar']
        flow = InstalledAppFlow.from_client_secrets_file('./Credentials/client_calendar_other2.json', scopes=scopes)
        credentials = flow.run_console()
        self. store_password("hi", credentials)

    def store_password(self, email, credentials):
        hashedCredentials = bcrypt.hashpw(credentials, bcrypt.gensalt())
        self.save_to_database(email, hashedCredentials)

    def save_to_database(self, id, email, hashedCredentials):
        item = {"id": id, "email": email, "password": hashedCredentials}
        self.db.add_item("user-info", item)
        print(email, hashedCredentials)

    def add_event(self, user, event):
        event = service.events().insert(calendarId='primary', body=event).execute()



if __name__ == '__main__':
    c = GoogleCanlandarAPI()
    event = {
        'summary': 'Google I/O 2015',
        'location': '800 Howard St., San Francisco, CA 94103',
        'description': 'A chance to hear more about Google\'s developer products.',
        'start': {
            'dateTime': '2015-05-28T09:00:00-07:00',
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': '2015-05-28T17:00:00-07:00',
            'timeZone': 'America/Los_Angeles',
        },
        'recurrence': [
            'RRULE:FREQ=DAILY;COUNT=2'
        ],
        'attendees': [
            {'email': 'lpage@example.com'},
            {'email': 'sbrin@example.com'},
        ],
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }


