from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import mimetypes
import pathlib
from UDP_client import run_client
from UDP_server import run_server_socket
from threading import Thread
import logging


BASE_DIR = pathlib.Path()
HTTP_PORT = 3000
HTTP_HOST = '0.0.0.0'
UDP_HOST = '127.0.0.1'
UDP_PORT = 5000

class HttpHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        data = self.rfile.read(int(self.headers['Content-Length']))
        # print(data)
        data_parse = urllib.parse.unquote_plus(data.decode())
        # print(data_parse)
        data_dict = {key: value for key, value in [
            el.split('=') for el in data_parse.split('&')]}
        print(data_dict)
        
        run_client(data_dict)
        
        self.send_response(302)
        self.send_header('Location', '/')
        self.end_headers()

    def do_GET(self):
        pr_url = urllib.parse.urlparse(self.path)
        if pr_url.path == '/':
            self.send_html_file('index.html')
        elif pr_url.path == '/message':
            self.send_html_file('message.html')
        else:
            if pathlib.Path().joinpath(pr_url.path[1:]).exists():
                print(pr_url.path)
                self.send_static()
            else:
                self.send_html_file('error.html', 404)

    def send_html_file(self, filename, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open(filename, 'rb') as fd:
            self.wfile.write(fd.read())

    def send_static(self):
        self.send_response(200)
        mt = mimetypes.guess_type(self.path)
        if mt:
            self.send_header("Content-type", mt[0])
        else:
            self.send_header("Content-type", 'text/plain')
        self.end_headers()
        with open(f'.{self.path}', 'rb') as file:
            self.wfile.write(file.read())

def run_http(host, port):
    server_address = (host, port)
    http = HTTPServer(server_address, HttpHandler)
    logging.info("Starting http server")
    try:
        http.serve_forever()
    except KeyboardInterrupt:
        http.server_close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    
    http_thread = Thread(target=run_http, args=(HTTP_HOST, HTTP_PORT))
    http_thread.start()
    
    udp_thread_server = Thread(target=run_server_socket, args=(UDP_HOST, UDP_PORT))
    udp_thread_server.start()


