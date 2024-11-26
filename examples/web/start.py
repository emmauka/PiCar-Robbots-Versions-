#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess
import os

user_name = "pi"  # Replace with the actual username if different

def start_http_server():
    subprocess.run(["sudo", "python3", "-m", "http.server", "80"], cwd=f"/home/{user_name}/picar_projects/picar-4wd/examples/web/client")

def close_http_server():
    subprocess.run(["sudo", "pkill", "-f", "python3 -m http.server"], cwd=f"/home/{user_name}/picar_projects/picar-4wd/examples/web/client")

def start_websocket(port):
    subprocess.run(["sudo", "python3", "/home/{user_name}/picar_projects/picar-4wd/examples/web/server/web_server.py", str(port)])

def close_websocket():
    subprocess.run(["sudo", "pkill", "-f", "python3 web_server.py"], cwd=f"/home/{user_name}/picar_projects/picar-4wd/examples/web/server")

class RestartServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/restart':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            close_websocket()
            start_websocket(9001)  # Adjust port numbers as needed
            self.wfile.write("OK".encode())
        else:
            print('error', self.path)
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write('<html><head></head><body>'.encode())
            self.wfile.write('<h1>{0!s} not found</h1>'.format(self.path).encode())

if __name__ == '__main__':
    try:
        start_http_server()
        start_websocket(9001)  # Start WebSocket server on port 9001

        print(f"Web example starts at http://localhost")
        print(f"Open http://localhost in your web browser to control the car!")

        server = HTTPServer(('localhost', 80), RestartServer)
        server.serve_forever()

    except KeyboardInterrupt:
        print('KeyboardInterrupt')
    finally:
        print("Finished")
        close_http_server()
        close_websocket()

      #  port = 9000 start_http_server() start_websocket() print("Web example starts at %s" % (ip)) print("Open http://%s in your web browser to control the car!" % (ip)) server = 
      #  HTTPServer((ip, port), restartServer) server.serve_foreve #
  # except KeyboardInterrupt:
      #  print('KeyboardInterrupt')
  # finally:
      #  print("Finished") server.socket.close() close_http_server() close_websocket()

