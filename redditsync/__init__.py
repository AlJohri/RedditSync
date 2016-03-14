from __future__ import print_function

import json
import httplib2
import apiclient, oauth2client
from pprint import pprint as pp

#####################################

# Set up Global Logging

import logging, blessings

t = blessings.Terminal()

class ColorFormatter(logging.Formatter):
    def format(self, record):
        formatted_message = super(ColorFormatter, self).format(record)
        if record.levelname == "ERROR":
            formatted_message = t.red(formatted_message)
        return formatted_message

formatter = ColorFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler = logging.StreamHandler()
handler.setFormatter(formatter)

logger = logging.getLogger() # global
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

#####################################

from redditsync.settings import GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, GOOGLE_SCOPE

flow = oauth2client.client.OAuth2WebServerFlow(
    client_id=GOOGLE_CLIENT_ID,
    client_secret=GOOGLE_CLIENT_SECRET,
    scope=GOOGLE_SCOPE,
    access_type="offline" # default
)

# Google only returns refresh token the first time. Revoke permission.
# https://security.google.com/settings/u/0/security/permissions
storage = oauth2client.file.Storage('credentials.dat')
credentials = storage.get()
if credentials is None or credentials.invalid:
    credentials = oauth2client.tools.run_flow(flow, storage, oauth2client.tools.argparser.parse_args())

def get_google_service():
    global credentials

    http = httplib2.Http()
    http = credentials.authorize(http)

    # list of api_name, api_version: https://developers.google.com/api-client-library/python/apis/
    service = apiclient.discovery.build('blogger', 'v3', http=http)

    return service
