import requests
from gcloud import dns
from oauth2client.client import flow_from_clientsecrets

flow = flow_from_clientsecrets('path_to_directory/client_secrets.json',
                               scope='https://www.googleapis.com/auth/calendar',
                               redirect_uri='http://example.com/auth_return')

r=requests.get('https://api.ipify.org?format=json')
ip = r.json()['ip']
