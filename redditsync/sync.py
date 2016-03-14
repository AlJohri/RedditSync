from __future__ import print_function

import os, sys, csv, time, argparse
from pprint import pprint as pp

from redditsync.reddit import get_newest_subreddit_post
from redditsync.reddit import get_last_recorded_submission_id, write_last_recorded_submission_id
from redditsync.utils import mkdir_p, parse_input

from redditsync import blogger, wordpress

import oauth2client

if __name__ == "__main__":

    # TODO: add CLI arguments
    # parser = argparse.ArgumentParser(description='')
    # parser.add_argument('--blogger', type=bool, help='')
    # parser.add_argument('--wordpress', type=bool, help='')
    # args = parser.parse_args()

    unique_subreddit_names, reversed_adjacency_list = parse_input()

    print("Found %d unique subreddits in input.csv." % len(unique_subreddit_names))
    print("Monitoring: %s" % unique_subreddit_names)
    print()

    folder = "last_subreddit_post_ids"
    mkdir_p(folder)

    while True:

        sys.stdout.flush()

        try:

            print("-------------------------------------")

            new_submissions = []

            for subreddit_name in unique_subreddit_names:
                last_submission_id = get_last_recorded_submission_id(folder, subreddit_name)
                submission = get_newest_subreddit_post(subreddit_name)

                if submission.id != last_submission_id:
                    print("Found new Submission: ", submission.id, submission.title.encode('utf-8'))
                    new_submissions.append(submission)
                    write_last_recorded_submission_id(folder, subreddit_name, submission.id)

            if len(new_submissions) == 0:
                print("No new submissions found.")

            for submission in new_submissions:
                subreddit_name = submission.subreddit.display_name

                # Post to Wordpress

                wordpress.create_post(
                    title=submission.title,
                    url=submission.url,
                    text=submission.selftext_html if submission.selftext_html else ""
                )

                print("Writing submission [%s %s] to wordpress blog for subreddit %s" % (submission.id, submission.title.encode('utf-8'), subreddit_name))

                # Post to Blogger
                # for blog_id in reversed_adjacency_list[subreddit_name]:
                #     print("Writing submission [%s %s] to blogger blog %s for subreddit %s" % (submission.id, submission.title.encode('utf-8'), blog_id, subreddit_name))
                #     blogger.create_post(
                #         blog_id=blog_id,
                #         title=submission.title,
                #         url=submission.url,
                #         text=submission.selftext_html if submission.selftext_html else ""
                #     )

            print("Sleeping for %d seconds..." % 30)
            print("-------------------------------------")
            print()
            time.sleep(30)

        except oauth2client.client.AccessTokenRefreshError:
            print('The credentials have been revoked or expired. Hopefully re-authorize by itself...?')

