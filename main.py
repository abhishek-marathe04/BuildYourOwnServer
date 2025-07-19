from MyHTTPServer import MyHTTPServer
import asyncio

if __name__ == "__main__":
    server = MyHTTPServer('localhost', 8006)
    asyncio.run(server.serve_forever())


