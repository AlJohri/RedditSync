from __future__ import print_function
from __future__ import unicode_literals
import argparse

from redditblogger import get_google_service

def main():

    service = get_google_service()

    parser = argparse.ArgumentParser(description='List posts for a blog.')
    parser.add_argument('blog_ids', type=int, nargs='+',
        help='Blog IDs. Use list_blogs if unknown.')

    args = parser.parse_args()

    for blog_id in args.blog_ids:

        print("Posts for Blog: %d" % blog_id)
        print()

        request = service.posts().list(blogId=blog_id)
        while request is not None:
            response = request.execute()
            for post in response.get('items', []):
                print(post['id'], post['title'], post['url'])
            request = service.posts().list_next(request, response)

if __name__ == "__main__":
    main()
