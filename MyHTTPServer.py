import socket
import threading


class MyHTTPServer:
    def __init__(self, host, port):
        # Setup socket, bind, listen
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))

        # # Listen for incoming connections (backlog of 1)
        self.server_socket.listen(5)
        print(f"Server is listening on http://{host}:{port}")  # Add this line
        return

    def serve_forever(self):
        # Main server loop: accept and handle clients
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Connection from {client_address}")
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.daemon = True
            client_thread.start()

    def handle_client(self, client_socket):
        # Receive, parse, respond
        raw_data = client_socket.recv(1024)
        request_text = raw_data.decode('utf-8')
        print(f"Raw request:\n{request_text}")

        method, path, version, headers, body = self.parse_request(request_text)

        print(f"Method : {method}")
        print(f"Path : {path}")
        print(f"Version : {version}")
        print(f"Headers : {headers}")
        print(f"Body : {body}")

        if path == "/":
            self.send_response(client_socket, status="200 OK", headers={"Content-Type": "text/plain"}, body="Welcome to Main Page")
        elif path == "/about":
            self.send_response(client_socket, status="200 OK", headers={"Content-Type": "text/plain"}, body="Welcome to About Page")
        else:
            response_body = "404 Not Found"
            self.send_response(client_socket, status="404 Not Found", headers={"Content-Type": "text/plain"}, body=response_body)
        
        return

    def parse_request(self, request_text):
        # Split into method, path, version, headers, body
        splitted_request = request_text.split('\r\n')
        request_line = splitted_request[0]
        parts = request_line.split(' ')
        method = parts[0] if len(parts) > 0 else ''
        path = parts[1] if len(parts) > 1 else ''
        version = parts[2] if len(parts) > 2 else ''

        # Headers
        headers = {}
        for line in splitted_request[1:]:
            if line == '':
                break
            if ': ' in line:
                key, value = line.split(': ', 1)
                headers[key] = value

        # Body
        try:
            empty_index = splitted_request.index('')
            body_lines = splitted_request[empty_index+1:]
            body = '\r\n'.join(body_lines)
        except ValueError:
            body = ''

        return method, path, version, headers, body

    def send_response(self, client_socket, status="200 OK", headers=None, body=""):
        # Build and send HTTP response
        if headers is None:
            headers = {}
        if 'Content-Length' not in headers:
            headers['Content-Length'] = str(len(body.encode('utf-8')))
        response_lines = [
            f"HTTP/1.1 {status}"
        ]
        for k, v in headers.items():
            response_lines.append(f"{k}: {v}")
        response_lines.append("")  # blank line
        response_lines.append(body)
        response = '\r\n'.join(response_lines)
        client_socket.sendall(response.encode('utf-8'))
        client_socket.close()