
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

def get_events(access_token, calendarId):
    logging.info('start getting calendar events %s %s', calendarId, access_token)
    today = datetime.utcnow()
    enddate = today + timedelta(days=7)
    formatted_startdate = today.isoformat("T") + "Z"
    formatted_enddate = enddate.isoformat("T") + "Z"
    logging.info('start date, end date %s %s %s %s', formatted_startdate, formatted_enddate, type(formatted_startdate), type(formatted_enddate))

    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(
        'https://www.googleapis.com/calendar/v3/calendars/'+calendarId+'/events',
        headers = headers,
        params = { 'timeMax': formatted_enddate,
                   'timeMin': formatted_startdate,
                   'maxResults':10,
                   }
    )
    logging.info('calendar response %s %s', response.status_code, response.text)
    return response.text

def add_event(access_token, calendarId, event):
    # event has start, end, title
    start = {
        "dateTime": event.starDateTime,
        "timeZone": event.timezone
    }
    end = {
        "dateTime": event.endDateTime,
        "timeZone": event.timezone
    }
    eventBody = {
        'start': start,
        'end': end,
        'summary': event.title,
    }

    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.post(
        'https://www.googleapis.com/calendar/v3/calendars/' + calendarId + '/events',
        headers= headers,
        body= eventBody
    )
    logging.info('calendar response %s %s', response.status_code, response.text)



