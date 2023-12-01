from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.path

        try:
            with open("." + path, 'rb') as file:
                content = file.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content)
        except FileNotFoundError:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h1>404 Not Found</h1>")

port = 8000

httpd = HTTPServer(('127.0.0.1', port), MyHandler)

print(f"Server running on http://127.0.0.1:{port}")
httpd.serve_forever()
