from __future__ import print_function

import os, time, argparse
from pprint import pprint as pp

from redditblogger.reddit.get_newest_subreddit_post import get_newest_subreddit_post
from redditblogger.reddit import get_last_recorded_submission_id, write_last_recorded_submission_id
from redditblogger.utils import mkdir_p

if __name__ == "__main__":

    folder = "last_subreddit_post_ids"
    mkdir_p(folder)

    parser = argparse.ArgumentParser(description='Show latest post for subreddits.')
    parser.add_argument('subreddit_names', type=str, nargs='+',
        help='Subreddit Names.')

    args = parser.parse_args()

    while True:

        new_submissions = []

        for subreddit_name in args.subreddit_names:
            last_submission_id = get_last_recorded_submission_id(folder, subreddit_name)
            submission = get_newest_subreddit_post(subreddit_name)

            if submission.id != last_submission_id:
                print("Found new Submission: ", submission.id, submission.title, submission.url ,submission.author.name)
                new_submissions.append(submission)
                write_last_recorded_submission_id(folder, subreddit_name, submission.id)

        print("-------------------------------------")

        if len(new_submissions) == 0:
            print("No new submissions found.")

        for submission in new_submissions:
            print("Writing submission [%s %s] to blogger" % (submission.id, submission.title), " - NOT IMPLEMENTED")

        print("Sleeping for %d minutes..." % 5)
        time.sleep(60*5)

# try:
# except oauth2client.client.AccessTokenRefreshError:
#     print('The credentials have been revoked or expired, please re-run the application to re-authorize')
