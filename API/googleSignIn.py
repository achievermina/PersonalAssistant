from flask import request
import getpass
import google.oauth2.credentials
import googleapiclient.discovery

try:
    q = getpass.getpass('tell me the master secret key you are going to use')
    p = getpass.getpass('tell me the master secret pwd you are going to use')
except Exception as error:
    print('ERROR', error)
else:
    print('email entered:', q, 'pwd: ', p)



# if __name__ == '__main__':
