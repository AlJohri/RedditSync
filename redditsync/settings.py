import os, json

ENVIRONMENT_VARIABLES = [
    'SHORTE_API_KEY',
    'WP_USERNAME',
    'WP_PASSWORD'
]

for var in ENVIRONMENT_VARIABLES:
    if not os.getenv(var):
        raise Exception("source .secret")

# https://shorte.st/tools/api
SHORTE_API_KEY = os.getenv('SHORTE_API_KEY').strip()
WP_USERNAME = os.getenv('WP_USERNAME').strip()
WP_PASSWORD = os.getenv('WP_PASSWORD').strip()

# get credentials from: https://console.developers.google.com/project/_/apiui/credential
with open("credentials.json") as f:
    credentials = json.load(f)
    GOOGLE_CLIENT_ID = credentials['web']['client_id']
    GOOGLE_CLIENT_SECRET = credentials['web']['client_secret']

# list of scopes: https://developers.google.com/identity/protocols/googlescopes
GOOGLE_SCOPE = 'https://www.googleapis.com/auth/blogger'

__all__ = [
    SHORTE_API_KEY,
    WP_USERNAME,
    WP_PASSWORD,
    GOOGLE_CLIENT_ID,
    GOOGLE_CLIENT_SECRET,
    GOOGLE_SCOPE
]