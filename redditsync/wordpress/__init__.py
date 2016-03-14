from wordpress_xmlrpc import Client
from redditsync.settings import WP_USERNAME, WP_PASSWORD

wp = Client('http://bitlunches.org/test/xmlrpc.php', WP_USERNAME, WP_PASSWORD)
