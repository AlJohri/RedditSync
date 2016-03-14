from __future__ import print_function
from __future__ import unicode_literals

from redditsync.settings import SHORTE_API_KEY

import requests
import argparse

def shorten_link(url):

    response = requests.put(
        "https://api.shorte.st/v1/data/url",
        headers={"public-api-token": SHORTE_API_KEY},
        data={"urlToShorten": url}
    )

    data = response.json()

    if data['status'] == 'ok':
        return data['shortenedUrl']
    else:
        raise Exception(data)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Shorten urls.')
    parser.add_argument('urls', type=str, nargs='+',
        help='Urls to shorten')
    args = parser.parse_args()

    for url in args.urls:
        print(url, "\t", shorten_link(url))
