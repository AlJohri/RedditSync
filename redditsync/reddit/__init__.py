def get_last_recorded_submission_id(folder, subreddit_name):
    try:
        with open(folder + "/" + subreddit_name + ".txt", "r") as f:
            last_submission_id = f.read()
    except IOError:
        last_submission_id = 0

    return last_submission_id

def write_last_recorded_submission_id(folder, subreddit_name, submission_id):
    with open(folder + "/" + subreddit_name + ".txt", "w") as f:
        f.write(submission_id)
