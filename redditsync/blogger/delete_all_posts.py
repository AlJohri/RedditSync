from redditsync import get_google_service
from redditsync.blogger.list_posts import get_posts
import argparse

import sys, logging
from oauth2client.client import HttpAccessTokenRefreshError

def delete_all_posts(blog_id):
    posts = get_posts(blog_id)
    for post in posts:
        delete_post(blog_id, post['id'])

def delete_post(blog_id, post_id):

    service = get_google_service()
    request = service.posts().delete(blogId=blog_id, postId=post_id)

    try:
        response = request.execute()
    except HttpAccessTokenRefreshError as err:
        logging.error(str(err))
        sys.exit()

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Delete all posts for blog(s).')
    parser.add_argument('blog_ids', type=int, nargs='+',
        help='Blog IDs. Use list_blogs if unknown.')

    args = parser.parse_args()

    for blog_id in args.blog_ids:
        delete_all_posts(blog_id)