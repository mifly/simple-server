from http.server import HTTPServer, BaseHTTPRequestHandler


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "/index" or self.path == "/index.html":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            html = """<!DOCTYPE html>
<html>
<head>
    <title>Hello</title>
</head>
<body>
    <h1>hello world</h1>
</body>
</html>"""
            self.wfile.write(html.encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"<h1>404 Not Found</h1>")


def main():
    host = "0.0.0.0"
    port = 8080
    server = HTTPServer((host, port), MyHandler)
    print(f"Server running at http://{host}:{port}/")
    server.serve_forever()


if __name__ == "__main__":
    main()
