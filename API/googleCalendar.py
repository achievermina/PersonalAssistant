
import requests
import logging
from datetime import datetime, timezone, timedelta

def get_calendar_id(access_token):
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
    #logging.info('calendar response %s %s', response.status_code, response.text)
    return response.text

def add_event(access_token, calendarId, event):
    # event has start, end, title
    start = {
        "dateTime": event['start_date_time'],
        "timeZone": event['timezone']
    }
    end = {
        "dateTime": event['end_date_time'],
        "timeZone": event['timezone']
    }
    event_body = {
        'start': start,
        'end': end,
        'summary': event['title'],
    }
    try:
        headers = {'Authorization': f'Bearer {access_token}'}
        response = requests.post(
            'https://www.googleapis.com/calendar/v3/calendars/' + calendarId + '/events',
            headers=headers,
            body=event_body
        )
        logging.info('Success: calendar added response %s', response.status_code)
        return True

    except Exception as e:
        logging.info("Failed: unable to add a calendar", e)
        return False



