import os, json

# https://shorte.st/tools/api
SHORTE_API_KEY = os.getenv('SHORTE_API_KEY')

# get credentials from: https://console.developers.google.com/project/_/apiui/credential
with open("credentials.json") as f:
    credentials = json.load(f)
    GOOGLE_CLIENT_ID = credentials['web']['client_id']
    GOOGLE_CLIENT_SECRET = credentials['web']['client_secret']

# list of scopes: https://developers.google.com/identity/protocols/googlescopes
GOOGLE_SCOPE = 'https://www.googleapis.com/auth/blogger'

__all__ = [
    SHORTE_API_KEY,
    GOOGLE_CLIENT_ID,
    GOOGLE_CLIENT_SECRET,
    GOOGLE_SCOPE
]