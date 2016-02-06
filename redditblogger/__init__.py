from __future__ import print_function

import json
import httplib2
import apiclient, oauth2client
from pprint import pprint as pp

from redditblogger.settings import GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, GOOGLE_SCOPE

flow = oauth2client.client.OAuth2WebServerFlow(
    GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, GOOGLE_SCOPE
)

def get_google_service():

    storage = oauth2client.file.Storage('credentials.dat')
    credentials = storage.get()
    if credentials is None or credentials.invalid:
        credentials = oauth2client.tools.run_flow(flow, storage, oauth2client.tools.argparser.parse_args())

    http = httplib2.Http()
    http = credentials.authorize(http)

    # list of api_name, api_version: https://developers.google.com/api-client-library/python/apis/
    service = apiclient.discovery.build('blogger', 'v3', http=http)

    return service
