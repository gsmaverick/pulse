import os

from flask import Flask

from utils import set_urls

from flask import request, render_template

def index():
    return render_template('index.html')
def about():
    return render_template('about.html')
def help():
    return render_template('help.html')

routes = [
    ('/', 'index', index),
    ('/about', 'about', about),
    ('/help', 'help', help)
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