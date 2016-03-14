clean:
	find . -name *.pyc | xargs rm

refresh:
	rm -rf last_subreddit_post_ids
