import socket
import mimetypes
import pathlib
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import threading
from datetime import datetime, date
import json
import os

UDP_IP = '127.0.0.1'
UDP_PORT = 5000


def run_client(ip, port, MESSAGE):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect((ip, port))
        server = ip, port
        print(MESSAGE)
        sock.sendto(MESSAGE.encode(), server)
        print(f'Clinet send data: {MESSAGE.encode()} to server: {server}')
        print("I'm working - client ! ")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        sock.close()


def run_server(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server = ip, port
    sock.bind(server)
    try:
        while True:
            data, address = sock.recvfrom(1024)
            print(f'Server received data: {data.decode()} from: {address}')
            data_dict = {key: value for key, value in [
                el.split('=') for el in data.decode().split('&')]}
            time = str(datetime.now())
            data_dict["time"] = time
            print(f'Słownik przed zapisem w pliku: {data_dict}')
            folder_path = "Storage"
            try:

                with open(os.path.join(folder_path, "data.json"), "r", encoding='utf-8') as fh:
                    existing_data = json.load(fh)

            except FileNotFoundError:
                existing_data = []

            print(f' Existing data : {existing_data}')
            print(f'Słownik: {data_dict}')

            with open(os.path.join(folder_path, "data.json"), "w", encoding='utf-8') as fh:
                existing_data.append(data_dict)
                json.dump(existing_data, fh)
                print(f'The data have been saved in "data.json" file !')

    except KeyboardInterrupt:
        print(f'Destroy server')
    finally:
        print("I'm working - server ! ")
        sock.close()


server = threading.Thread(target=run_server, args=(UDP_IP, UDP_PORT))
client = threading.Thread(target=run_client, args=(UDP_IP, UDP_PORT))


class HttpHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        data = self.rfile.read(int(self.headers['Content-Length']))
        print(data)
        data_parse = urllib.parse.unquote_plus(data.decode())
        run_client(ip=UDP_IP, port=UDP_PORT, MESSAGE=data_parse)
        self.send_response(302)
        self.send_header('Location', '/')
        self.end_headers()

    def do_GET(self):
        pr_url = urllib.parse.urlparse(self.path)
        if pr_url.path == '/':
            self.send_html_file('index.html')
        elif pr_url.path == '/idea':
            self.send_html_file('idea.html')
        else:
            if pathlib.Path().joinpath(pr_url.path[1:]).exists():
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


def run(server_class=HTTPServer, handler_class=HttpHandler):
    server_address = ('', 3000)
    http = server_class(server_address, handler_class)
    try:
        http.serve_forever()
    except KeyboardInterrupt:
        http.server_close()


if __name__ == '__main__':
    server.start()
    run()  # Tworzę serwer http na localhost:3000 i wystawiam strony:  index.html, idea.html oraz error.html
