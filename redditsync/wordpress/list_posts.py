from __future__ import print_function

from redditsync.wordpress import wp

from wordpress_xmlrpc import WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo

def get_posts():
    return wp.call(GetPosts())

def main():

    for post in get_posts():
        print("ID:", post.id, "Date:", post.date, "Title:", post.title, "Link:", post.link)

if __name__ == "__main__":
    main()