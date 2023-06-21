from flask import Flask
from flask import Response
flask_app = Flask('flaskapp')


@flask_app.route('/hello')
def hello_world():
    return Response(
        'Hello world from Flask!\n',
        mimetype='text/plain'
    )

app = flask_app.wsgi_app

# Use $  to serve the Flask application
  # This tells the server to load the "app" callable from the python module flaskapp
  # After doing so, the server is ready to take requests and forward them to the Flask app