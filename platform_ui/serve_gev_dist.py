import http.server
import socketserver
import os
import sys

PORT = 4173
DIST_DIR = r"F:\documents\SOIC\EconAgent_Platform\platform_ui\gods-eye-view-main\gods-eye-view-main\dist"

class EmbeddedHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIST_DIR, **kwargs)

    def end_headers(self):
        # Enable iframe embedding from anywhere (removes X-Frame-Options and sets permissive CSP)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.send_header('Content-Security-Policy', "frame-ancestors *")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

def run():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("0.0.0.0", PORT), EmbeddedHandler) as httpd:
        print(f"Serving God's Eye View 3D on http://0.0.0.0:{PORT} from {DIST_DIR}")
        sys.stdout.flush()
        httpd.serve_forever()

if __name__ == '__main__':
    run()

