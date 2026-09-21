#!/usr/bin/env python3
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from urllib.request import Request, urlopen
import json, os

PORT = int(os.environ.get("PORT", "8080"))
TOKEN_URL = "http://169.254.169.254/latest/api/token"
META = "http://169.254.169.254/latest/meta-data/"

def metadata(path):
    try:
        req = Request(TOKEN_URL, method="PUT", headers={"X-aws-ec2-metadata-token-ttl-seconds":"21600"})
        token = urlopen(req, timeout=.4).read().decode()
        req = Request(META + path, headers={"X-aws-ec2-metadata-token": token})
        return urlopen(req, timeout=.4).read().decode()
    except Exception:
        return None

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.split("?")[0] == "/api/server-info":
            data = {
                "instance_id": metadata("instance-id") or os.environ.get("INSTANCE_ID","local-demo"),
                "availability_zone": metadata("placement/availability-zone") or os.environ.get("AZ","local"),
                "private_ip": metadata("local-ipv4") or os.environ.get("PRIVATE_IP","127.0.0.1"),
            }
            body=json.dumps(data).encode()
            self.send_response(200)
            self.send_header("Content-Type","application/json")
            self.send_header("Cache-Control","no-store")
            self.send_header("Content-Length",str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        elif self.path == "/health":
            body=b"healthy"
            self.send_response(200); self.send_header("Content-Type","text/plain")
            self.send_header("Content-Length",str(len(body))); self.end_headers(); self.wfile.write(body)
        else:
            super().do_GET()

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print(f"CloudNova running on :{PORT}")
    ThreadingHTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
