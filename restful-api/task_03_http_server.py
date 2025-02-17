#!/usr/bin/python3
"""
Develop a simple API using Python with the `http.server` module
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class mysubclass(BaseHTTPRequestHandler):
    """
    subclass of http.server.BaseHTTPRequestHandler
    """


    def do_GET(self):
        """
        handle GET requests
        """
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Hello, this is a simple API!")
        if self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            json.dumps(data)
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=mysubclass):
    """
    initialize the server
    """
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    run()
