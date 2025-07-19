# BuildYourOwnServer

A minimal, educational HTTP server built from scratch in Python using `asyncio`.  
**Objective:** Understand how HTTP servers work by building your own, with a FastAPI/Flask-like routing interface.

---

## Features Implemented

- **Asyncio-based server:** Handles multiple clients concurrently using Python's async features.
- **Custom routing with decorators:** Define routes using `@app.get()` and `@app.post()` decorators, similar to FastAPI/Flask.
- **Request/Response data classes:** Clean, structured handling of HTTP requests and responses.
- **Basic HTTP parsing:** Parses method, path, version, headers, and body from raw HTTP requests.
- **404 handling:** Returns a 404 response for unknown routes.

---

## Example Usage

```python
from MyHTTPServer import MyHTTPServer
import asyncio
import json
from models import Request, Response

app = MyHTTPServer('localhost', 8006)

@app.get("/")
async def home(request: Request) -> Response:
    return Response(
        body=json.dumps({"message": "Hello, world!"}),
        headers={"Content-Type": "application/json"}
    )

if __name__ == "__main__":
    asyncio.run(app.serve_forever())
```

---

## Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/BuildYourOwnServer.git
    cd BuildYourOwnServer
    ```

2. **(Optional) Create a virtual environment:**
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. **Install dependencies:**  
   *(If you add any, e.g. `dataclasses` for Python <3.7, or others)*

4. **Run the server:**
    ```sh
    python main.py
    ```

5. **Test with curl or browser:**
    ```sh
    curl http://localhost:8006/
    ```

---

## Next Steps / Important Features To Add

- **Static file serving:** Serve files (HTML, CSS, JS, images) from a `/static/` directory.
- **Query parameter parsing:** Parse and provide access to URL query parameters.
- **Form and JSON body parsing:** Automatically parse `application/x-www-form-urlencoded` and `application/json` request bodies.
- **Middleware support:** Allow pre- and post-processing of requests (e.g., logging, authentication).
- **Custom error handling:** User-defined handlers for 404, 500, etc.
- **Route parameters:** Support dynamic routes like `/user/{id}`.
- **Graceful shutdown:** Handle shutdown signals cleanly.
- **Persistent connections:** Support HTTP keep-alive.
- **Logging:** Add request/response logging for debugging and monitoring.
- **HTTPS support:** Optionally serve over TLS/SSL.

---

## Why Build Your Own?

- **Learning:** Deepen your understanding of HTTP, sockets, and asynchronous programming.
- **Customization:** Add only the features you need, and understand every line of your server.
- **Fun:** It's rewarding to see your own server respond to real HTTP requests!

---

## License

MIT License

---

*Happy hacking!*
