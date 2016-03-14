from __future__ import print_function

import redditsync.wordpress
from wordpress_xmlrpc.methods.posts import GetPosts

def get_posts():
    return redditsync.wordpress.wp.call(GetPosts())

def main():

    for post in get_posts():
        print("ID:", post.id, "Date:", post.date, "Title:", post.title, "Link:", post.link)

if __name__ == "__main__":
    main()