from __future__ import print_function

import os, csv, time, argparse
from pprint import pprint as pp
from collections import defaultdict

from redditblogger.reddit.get_newest_subreddit_post import get_newest_subreddit_post
from redditblogger.reddit import get_last_recorded_submission_id, write_last_recorded_submission_id
from redditblogger.blogger.create_post import create_post
from redditblogger.utils import mkdir_p

if __name__ == "__main__":

    adjacency_list = {}
    with open("input.csv", "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            blog_id, subreddit_names = int(row[0]), row[1].split("|")
            adjacency_list[blog_id] = subreddit_names

    reversed_adjacency_list = defaultdict(list)
    for blog_id, subreddit_names in adjacency_list.items():
        for subreddit_name in subreddit_names:
            reversed_adjacency_list[subreddit_name].append(blog_id)

    unique_subreddit_names = list(reversed_adjacency_list.keys())

    folder = "last_subreddit_post_ids"
    mkdir_p(folder)

    while True:

        print()
        print("-------------------------------------")

        new_submissions = []

        for subreddit_name in unique_subreddit_names:
            last_submission_id = get_last_recorded_submission_id(folder, subreddit_name)
            submission = get_newest_subreddit_post(subreddit_name)

            if submission.id != last_submission_id:
                print("Found new Submission: ", submission.id, submission.title)
                new_submissions.append(submission)
                write_last_recorded_submission_id(folder, subreddit_name, submission.id)

        if len(new_submissions) == 0:
            print("No new submissions found.")

        for submission in new_submissions:
            subreddit_name = submission.subreddit.display_name
            for blog_id in reversed_adjacency_list[subreddit_name]:
                print("Writing submission [%s %s] to blog %s for subreddit %s" % (submission.id, submission.title, blog_id, subreddit_name))
                create_post(
                    blog_id=blog_id,
                    title=submission.title,
                    url=submission.url,
                    text=submission.selftext_html
                )

        print("Sleeping for %d minutes..." % 5)
        time.sleep(60*5)

    # try:
    # except oauth2client.client.AccessTokenRefreshError:
    #     print('The credentials have been revoked or expired, please re-run the application to re-authorize')
