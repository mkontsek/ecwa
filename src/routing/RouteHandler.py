import json
from http.server import BaseHTTPRequestHandler

from src.routing.Controller import showRankings


def outputToBytes(data):
    return bytes(json.dumps(data), 'utf-8')


def processRoute(path: str) -> str:
    country: str = path.split('/')[1]
    return showRankings(country)


class RouteHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()

        result = processRoute(self.path)

        self.wfile.write(outputToBytes(result))
