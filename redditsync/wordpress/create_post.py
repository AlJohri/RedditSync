from redditsync.shorten_link import shorten_link

import redditsync.wordpress

from wordpress_xmlrpc import WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost

import sys, logging

def create_post(title, text="", url="", image_url=""):

    shortened_url = shorten_link(url) if url else ""

    url_html = "<a href='{shortened_url}'>{url}</a><br/>".format(url=url, shortened_url=shortened_url) if url else ""
    image_html = "<img style='width: 100%; height: auto;' src='{image_url}'></img><br/>".format(image_url=image_url) if image_url else ""
    text_html = "<p>" + text + "</p>" + "<br/>" if text else ""
    content = url_html + image_html + text_html

    # https://developer.wordpress.com/docs/api/1.1/post/sites/%24site/posts/new/
    # http://python-wordpress-xmlrpc.readthedocs.org/en/latest/examples/posts.html

    post = WordPressPost()
    post.title = title
    post.content = content
    post.author = "testaccount"
    post.post_status = "publish"
    # post.terms_names = {
    #   'post_tag': ['test', 'firstpost'],
    #   'category': ['Introductions', 'Tests']
    # }

    try:
        redditsync.wordpress.wp.call(NewPost(post))
    except Exception as err:
        logging.error(str(err))
        sys.exit()

if __name__ == "__main__":
    create_post(
        title="This is a test post",
        text="blahblahblah",
        url="http://www.google.com",
        image_url="http://ichef.bbci.co.uk/news/976/media/images/83351000/jpg/_83351965_explorer273lincolnshirewoldssouthpicturebynicholassilkstone.jpg"
    )
