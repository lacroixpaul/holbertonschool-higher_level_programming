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
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            json.dumps(data)
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, mysubclass)
    print("Serving on http://localhost:8000")
    httpd.serve_forever()
