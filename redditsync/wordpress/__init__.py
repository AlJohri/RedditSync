from redditsync.wordpress.create_post import create_post
from redditsync.wordpress.list_posts import get_posts

from wordpress_xmlrpc import Client
from redditsync.settings import WP_SERVER, WP_USERNAME, WP_PASSWORD

wp = Client(WP_SERVER, WP_USERNAME, WP_PASSWORD)