from MyHTTPServer import MyHTTPServer

if __name__ == "__main__":
    server = MyHTTPServer('localhost', 8006)
    server.serve_forever()


