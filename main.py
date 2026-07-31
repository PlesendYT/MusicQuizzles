#!/usr/bin/env python3
import http.server
import urllib.request
import urllib.parse
import json
import os
import time

PORT = 3001
DEEZER = "https://api.deezer.com"
CACHE_TTL = 300
MAX_RETRIES = 3

_cache = {}

def cached_request(url):
    now = time.time()
    if url in _cache and now - _cache[url]['time'] < CACHE_TTL:
        return _cache[url]['data']
    for attempt in range(MAX_RETRIES):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=10) as r:
                data = r.read()
            _cache[url] = {'data': data, 'time': now}
            return data
        except Exception as e:
            if attempt < MAX_RETRIES - 1:
                time.sleep(2 ** attempt)
            else:
                raise e

class Handler(http.server.BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        if parsed.path == "/deezer":
            self.send_header("Content-Type", "application/json; charset=utf-8")
            api_path = params.get("path", [None])[0]
            if not api_path:
                self.end_headers()
                self.wfile.write(json.dumps({"error": "missing path"}).encode())
                return
            try:
                url = DEEZER + api_path
                data = cached_request(url)
                self.end_headers()
                self.wfile.write(data)
            except Exception as e:
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode())
            return
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        html_path = os.path.join(os.path.dirname(__file__), "index.html")
        with open(html_path, "rb") as f:
            self.wfile.write(f.read())

if __name__ == "__main__":
    server = http.server.HTTPServer(("", PORT), Handler)
    print(f"\n🎵 Music Quiz Server laeuft!")
    print(f"👉 Oeffne im Browser: http://localhost:{PORT}")
    print("   (Strg+C zum Beenden)\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer gestoppt.")
