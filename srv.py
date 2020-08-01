import os
import socketserver
from http.server import SimpleHTTPRequestHandler


PORT = int(os.getenv("PORT", 8000))
print(PORT)


class MyHandler(SimpleHTTPRequestHandler):
    def handle_root(self):
        pass

    def handle_hello(self):
        content = f"""
                <html>
                <head><title>XXX</title></head>
                <body>
                <h1>Hello world!</h1>
                <p>PATH: {self.path}</p>
                </body>
                </html>
                """

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-length", str(len(content)))
        self.end_headers()
        self.wfile.write(content.encode())

    def handle_404(self):
        msg = """NOT FOUND!!!!!!!"""
        self.send_response(404)
        self.send_header("Content-type", "text/plain")
        self.send_header("Content-length", str(len(msg)))
        self.end_headers()
        self.wfile.write(msg.encode())

    def respond(self, code):
        msg = """NOT FOUND!!!!!!!"""
        self.send_response(code)
        self.send_header("Content-type", "text/plain")
        self.send_header("Content-length", str(len(msg)))
        self.end_headers()
        self.wfile.write(msg.encode())

    def do_GET(self):
        path = self.build_path()

        if self.path == "/":
            self.handle_root()
        elif self.path == "/hello/":
            self.handle_hello()
        else:
            self.handle_404()

    def build_path(self) -> str:
        result = self.path

        if result[-1] != "/":
            result = f"{result}/"

        return result


if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("it" + " works")
        httpd.serve_forever(poll_interval=1)