from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class Request:
    method: str
    path: str
    version: str
    headers: Dict[str, str]
    body: str

@dataclass
class Response:
    status: str = "200 OK"
    headers: Dict[str, str] = None
    body: str = ""