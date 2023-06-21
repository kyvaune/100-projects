from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request):
    return Response(
        'Hello world from Pyramid!\n',
        content_type='text/plain',
    )

config = Configurator()

config.add_route('hello', '/hello')
config.add_view(hello_world, route_name='hello')

app = config.make_wsgi_app() # This line creates a WSGI (Web Server Gateway Interface) application object that can be served by any WSGI server. The WSGI application is based on the configuration set up using the Configurator object.

# Use $ python3 wsgi-test.py pyramidapp:app to serve the Pyramid application
  # This tells the server to load the "app" callable from the python module pyramidapp
  # After doing so, the server is ready to take requests and forward them to the Pyramid app