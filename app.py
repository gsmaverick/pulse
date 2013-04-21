import os

from flask import Flask

from utils import set_urls
from views import *

routes = [
    # Desktop site pages.
    ('/', 'index', pages.index),
    ('/about', 'about', pages.about),
    ('/help', 'help', pages.help),
    ('/app', 'app', pages.app),

    # API.
    ('/api/search', 'search', endpoint.search)
]

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))

    # Create the app.
    app = Flask(__name__, template_folder='site/templates')

    # Attach all application routes.
    set_urls(app, routes)

    # Let's go!
    app.run(host='0.0.0.0', port=port, debug=True)