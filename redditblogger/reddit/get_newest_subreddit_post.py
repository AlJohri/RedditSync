from __future__ import print_function
from __future__ import unicode_literals

import praw
import argparse

r = praw.Reddit(user_agent='my_cool_application')

def get_newest_subreddit_post(subreddit_name):
    subreddit = r.get_subreddit(subreddit_name)
    submission = list(subreddit.get_new(limit=1))[0]
    return submission

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Show latest post for subreddits.')
    parser.add_argument('subreddit_names', type=str, nargs='+',
        help='Subreddit Names.')

    args = parser.parse_args()

    for subreddit_name in args.subreddit_names:
        submission = get_newest_subreddit_post(subreddit_name)
        print(subreddit_name, "|", submission.id, "|", submission.author.name, "|", submission.title, "|", submission.url)