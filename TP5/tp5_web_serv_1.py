from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        response_content = "<h1>Hello, I am an HTTP server</h1>"
        self.wfile.write(response_content.encode())

port = 8000

httpd = HTTPServer(('127.0.0.1', port), MyHandler)

print(f"Server running on http://127.0.0.1:{port}")
httpd.serve_forever()
