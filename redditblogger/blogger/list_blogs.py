from __future__ import print_function
from __future__ import unicode_literals

from redditblogger import get_google_service
from pprint import pprint as pp

DEBUG = False

def get_blogs():

    user_id = "self"

    service = get_google_service()
    request = service.blogs().listByUser(userId=user_id)
    response = request.execute()

    print("Blogs for User: %s" % user_id)
    print()

    return response.get('items', [])

if __name__ == "__main__":
    blogs = get_blogs()

    for blog in blogs:
        print(blog['id'], blog['name'], blog['url'])
        if DEBUG == True:
            pp(blog)
            print()
