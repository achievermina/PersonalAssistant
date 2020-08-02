import requests
import logging
from datetime import datetime, timedelta

def get_calendar_id(access_token):
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(
        'https://www.googleapis.com/calendar/v3/users/me/calendarList',
        headers = headers
    )
    logging.info('calendar response %s %s', response.status_code, response.text)

    return response

def get_events(access_token, calendarId, next_sync_token=None, cnt = 0):
    logging.info('start getting calendar events %s %s %s', calendarId, access_token, next_sync_token)
    today = datetime.utcnow()
    enddate = today + timedelta(days=7)
    formatted_startdate = today.isoformat("T") + "Z"
    formatted_enddate = enddate.isoformat("T") + "Z"
    logging.info('start date, end date %s %s', formatted_startdate, formatted_enddate)

    if next_sync_token is None:  #full sync
        request_params = {
            'timeMax': formatted_enddate,
            'timeMin': formatted_startdate,
            'maxResults': 10,
        }
    else:
        request_params = {
            'maxResults': 10,
            'syncToken': next_sync_token,
        }

    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(
        'https://www.googleapis.com/calendar/v3/calendars/' + calendarId + '/events',
        headers = headers,
        params = request_params
    )

    if (response.status_code == 401 and cnt !=1):
        logging.error('inside error %s %s %s', response.status_code, response.text, next_sync_token[:-1])
        get_events(access_token, calendarId, None, 1)

    logging.info('outside error %s %s', response.status_code, response)
    return response.text

def add_event(access_token, calendarId, event):
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
