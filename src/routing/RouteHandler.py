import json
from http.server import BaseHTTPRequestHandler

from src.routing.Controller import showRankings


def outputToBytes(data):
    return bytes(json.dumps(data), 'utf-8')


def processRoute(path: str) -> str:
    country: str = path.split('/')[1]
    return showRankings(country)


def allowCors(handler):
    handler.send_header('Access-Control-Allow-Origin', '*')
    handler.send_header('Access-Control-Allow-Methods', 'GET')


class RouteHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        allowCors(self)
        self.end_headers()

        result = processRoute(self.path)

        self.wfile.write(outputToBytes(result))
