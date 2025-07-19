# BuildYourOwnServer

## Objective

The goal of this project is to understand how an HTTP server works by building one from scratch in Python, without using any high-level web frameworks. This hands-on approach helps demystify the HTTP protocol, request parsing, response formatting, and the basics of network programming.

## Features
- Pure Python implementation using sockets
- Parses HTTP requests (method, path, headers, body)
- Sends basic HTTP responses
- Modular, class-based design for easy extension

## Getting Started

### Prerequisites
- Python 3.7 or higher

### Setup
1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd BuildYourOwnServer
   ```
2. **Run the server:**
   ```sh
   python main.py
   ```
   The server will start and listen on `http://localhost:8080` (or the port you specify).

3. **Test the server:**
   - Open a new terminal and use `curl`:
     ```sh
     curl http://localhost:8080/
     ```
   - Or open `http://localhost:8080/` in your browser.

## Project Structure
```
BuildYourOwnServer/
├── main.py            # Entry point, starts the server
├── MyHTTPServer.py    # Contains the MyHTTPServer class and server logic
```

## How It Works
- The server listens for incoming TCP connections.
- For each connection, it reads the raw HTTP request, parses the method, path, headers, and body.
- It prints the parsed request details for learning purposes.
- It sends a simple HTTP response back to the client.

## Extending the Server
You can extend this project by adding:
- Routing for different paths (e.g., `/about`, `/static/...`)
- Serving static files
- Handling POST/PUT data (form or JSON)
- Logging requests and responses
- Graceful shutdown and error handling

## License
This project is for educational purposes.
