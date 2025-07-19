import asyncio
from models import Request, Response


class MyHTTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.routes = {}

    async def serve_forever(self):
        server = await asyncio.start_server(self.handle_client, self.host, self.port)
        print(f"Asyncio server listening on http://{self.host}:{self.port}")
        async with server:
            await server.serve_forever()

    async def handle_client(self, reader, writer):
        data = await reader.read(1024)
        request_text = data.decode('utf-8')

        method, path, version, headers, body = self.parse_request(request_text)

        request = Request(method=method, path=path, version=version, headers=headers, body=body)
        handler = self.routes.get((method, path))
        if handler:
            response : Response = await handler(request)
            await self.send_response(writer=writer, status=response.status, headers=response.headers, body=response.body)
        else:
            response_body = "404 Not Found"
            await self.send_response(writer, status="404 Not Found", headers={"Content-Type": "text/plain"}, body=response_body)
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

    async def send_response(self, writer, status="200 OK", headers=None, body=""):
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
        writer.write(response.encode('utf-8'))
        await writer.drain()
        writer.close()
        await writer.wait_closed()

    def get(self, path):
        def decocator(func):
            self.routes[('GET', path)] = func
            return func
        return decocator
    
    def post(self, path):
        def decocator(func):
            self.routes[('POST', path)] = func
            return func
        return decocator