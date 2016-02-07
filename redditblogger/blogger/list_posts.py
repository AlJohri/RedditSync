from __future__ import print_function
from __future__ import unicode_literals
import argparse
from pprint import pprint as pp

from redditblogger import get_google_service

def get_posts(blog_id):

    service = get_google_service()

    posts = []

    request = service.posts().list(blogId=blog_id)
    while request is not None:
        response = request.execute()
        posts += response.get('items', [])
        request = service.posts().list_next(request, response)

    return posts

DEBUG = False

def main():

    parser = argparse.ArgumentParser(description='List posts for a blog.')
    parser.add_argument('blog_ids', type=int, nargs='+',
        help='Blog IDs. Use list_blogs if unknown.')

    args = parser.parse_args()

    for blog_id in args.blog_ids:

        print("Posts for Blog: %d" % blog_id)
        print()

        posts = get_posts(blog_id)

        for post in posts:
            print(post['id'], post['title'], post['url'])
            if DEBUG == True:
                pp(post)
                print()


if __name__ == "__main__":
    main()
