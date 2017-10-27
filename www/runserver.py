#!/usr/bin/env python3
# coding: utf-8
from http import server
from urllib import parse
from pathlib import Path


class MyHTTPRequestHandler(server.SimpleHTTPRequestHandler):

    def do_GET(self):
        params = parse.urlparse(self.path)

        # On test si le fichier html existe
        name = "." + "/" + params.path + ".html"
        p = Path(name)
        if p.exists() and p.is_file():
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            with open(name, 'rb') as f:
                self.copyfile(f, self.wfile)
        else:
            super(MyHTTPRequestHandler, self).do_GET()


def run():
    port = 8000
    print(f'run server on {port}')
    server_address = ('', port)
    httpd = server.HTTPServer(server_address, MyHTTPRequestHandler)
    httpd.serve_forever()

if __name__ == '__main__':
    run()
