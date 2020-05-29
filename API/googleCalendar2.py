
import requests
import logging
from datetime import datetime, timezone, timedelta

def get_calandarId(access_token):
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(
        'https://www.googleapis.com/calendar/v3/users/me/calendarList',
        headers = headers
    )
    logging.info('calendar response %s %s', response.status_code, response.text)

    return response


def get_events(access_token,calendarId):
    logging.info('start getting calendar events %s %s', calendarId, access_token)
    date_max = datetime.now(timezone.utc).astimezone() + timedelta(days=7)
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(
        'https://www.googleapis.com/calendar/v3/calendars/'+calendarId+'/events',
        headers = headers,
        params = { 'timeMax': date_max }
    )
    logging.info('calendar response %s %s', response.status_code, response.text)

    return response




# def save_to_database(self, id, email, hashedCredentials):
#     item = {"id": id, "email": email, "password": hashedCredentials}
#     self.db.add_item("user-info", item)
#     print(email, hashedCredentials)
#
# def add_event(self, user, event):
#     event = self.service.events().insert(calendarId='primary', body=event).execute()
#
# def get_event(self):
#     event = self.service.events().get(calendarId='primary', eventId='eventId').execute()
#     print(event['summary'])

#
# if __name__ == '__main__':
