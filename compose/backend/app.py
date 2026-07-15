from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        response = {
            "message": "Hello from backend!",
            "service": "python-api"
        }

        self.send_response(200)
        self.send_header(
            "Content-type",
            "application/json"
        )
        self.end_headers()

        self.wfile.write(
            json.dumps(response).encode()
        )


server = HTTPServer(
    ("0.0.0.0", 5000),
    Handler
)

print("Backend running on port 5000")

server.serve_forever()
