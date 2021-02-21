import http.server
import socketserver

from settings import PORT, TITLE, AUTHOR, DESCRIPTION
from logic import get_post_titles
from utils import date_to_str


posts = [f'<p><a href="">{date_to_str(e["date"])} - {e["title"]}</a></p>' for e in get_post_titles()]

main_template = f"""
<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">

  <title>{TITLE}</title>
  <meta name="author" content="{AUTHOR}">

  <link rel="stylesheet" href="css/styles.css?v=1.0">
  <style>
  </style>

</head>

<body>
  <div class="description">
    {DESCRIPTION}
  </div>
  <div class="posts">
    {"".join(posts)}
  </div>
  <script></script>
</body>
</html>
"""


class BlogHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(main_template.encode('utf-8'))


with socketserver.TCPServer(("0.0.0.0", PORT), BlogHandler) as httpd:
    httpd.serve_forever()
