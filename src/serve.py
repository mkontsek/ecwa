import sys
from http.server import HTTPServer

from routing.RouteHandler import RouteHandler


SERVER_PORT = 8000


def serve():
    httpd = HTTPServer(('localhost', SERVER_PORT), RouteHandler)
    print('Running ecwa server on port', SERVER_PORT)
    httpd.serve_forever()

serve()