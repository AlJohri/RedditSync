from __future__ import print_function
from __future__ import unicode_literals

from redditblogger import get_google_service

def main():

    user_id = "self"

    service = get_google_service()
    request = service.blogs().listByUser(userId=user_id)
    response = request.execute()

    print("Blogs for User: %s" % user_id)
    print()

    for blog in response.get('items', []):
        print(blog['id'], blog['name'], blog['url'])

if __name__ == "__main__":
    main()
