import os

from flask import Flask

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))

    # Create the app.
    app = Flask(__name__)

    # Let's go!
    app.run(host='0.0.0.0', port=port, debug=True)