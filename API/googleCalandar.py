from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
import bcrypt


class GoogleCanlandarAPI:
    def __init__(self):
        self.connectCalandar()

    def connectCalandar(self):
        scopes = ['https://www.googleapis.com/auth/calendar']
        flow = InstalledAppFlow.from_client_secrets_file('./Credentials/client_calendar_other2.json', scopes=scopes)
        credentials = flow.run_console()
        self.storePassword("hi", credentials)

    def storePassword(self, email, credentials):
        hashedCredentials = bcrypt.hashpw(credentials, bcrypt.gensalt())
        self.saveToDatabase(email, hashedCredentials)

    def saveToDatabase(self, email, hashedCredentials):
        print(email, hashedCredentials)

if __name__ == '__main__':
    c = GoogleCanlandarAPI()



