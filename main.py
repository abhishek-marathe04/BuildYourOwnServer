import json
from MyHTTPServer import MyHTTPServer
import asyncio
from models import Request, Response

app = MyHTTPServer('localhost', 8006)

@app.get("/")
async def home(request: Request) -> Response:
    return Response(body=json.dumps({"message": "Hello, world!"}))

if __name__ == "__main__":
    asyncio.run(app.serve_forever())


