from http.server import SimpleHTTPRequestHandler

import settings


class MyHttp(SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.build_path()

        if path == "/":
            self.handle_root()
        elif path == "/hello/":
            self.handle_hello()
        elif path = "/style/"


        else:
            self.handle_404()

    def handle_root(self):
        return super().do_GET()

    def handle_hello(self):
        content = f"""
        <html>
        <head><title>Hello Page</title></head>
        <body>
        <h1>Hello world!</h1>
        <p>path: {self.path}</p>
        </body>
        </html>
        """

        self.respond(content)

        def handle_style(self):
            css_file = settings.PROJECT_DIR / "styles" / "styles.css"
            if not css_file.exists():
                return self.handle_404()

            with css_file.open("r") as fp:
                css = fp.read()

            self.respond(css, content_type="text/css")

        def handle_image(self):
            image_file = settings.PROJECT_DIR / "images" / "xxx.png"
            if not image_file.exists():
                return self.handle_404()

            with image_file.open("rb") as fp:
                img = fp.read()

            self.respond(img, content_type="image/png")

    def handle_404(self):
        msg = """NOT FOUND!!!!!!!!"""

        self.respond(msg, code=404, content_type="text/plain")

    def respond(self, message, code=200, content_type="text/html"):
        self.send_response(code)
        self.send_header("Content-type", content_type)
        self.send_header("Content-length", str(len(message)))
        self.send_header("Cache-control", f"max-age={settings.CACHE_AGE}")
        self.end_headers()
        self.wfile.write(message.encode())

    def build_path(self) -> str:
        result = self.path

        if result[-1] != "/":
            result = f"{result}/"

        return result