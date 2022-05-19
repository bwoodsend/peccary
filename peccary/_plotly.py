import json
import os
import uuid
from http.server import BaseHTTPRequestHandler
from http import HTTPStatus
import socketserver
import webbrowser


class Scene:
    header = """<!DOCTYPE html>
<head>
  <meta charset="utf-8" />
  <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
"""

    def __init__(self, id=None, **layout):
        self.data = []
        self.layout = layout
        self.id = id or uuid.uuid1().hex

    def plot(self, **data):
        """Add a new trace to the scene.

        Example::

            scene.plot(x=[1, 2, 3], y=[3, 1, 2], name="Some label",
                       marker={"size": 12}, type="scatter", mode="markers")

        """
        self.data.append(data)

    def to_html(self, *, standalone=False):
        if standalone:
            return self.header + self.to_html()
        return """\
<div id="%s"></div>
<script type="text/javascript">
    Plotly.newPlot(document.getElementById('%s'), %s, %s);
</script>
""" % (self.id, self.id, self._dumps(self.data), self._dumps(self.layout))

    @staticmethod
    def _dumps(data):
        return json.dumps(data, cls=NumPyJSONEncoder, separators=(",", ":"))

    def preview(self_):

        class Handler(BaseHTTPRequestHandler):

            def do_HEAD(self):
                self.send_response(HTTPStatus.OK)
                self.send_header("Content-type", "text/html")
                self.end_headers()

            def do_GET(self):
                self.do_HEAD()
                self.wfile.write(self_.to_html(standalone=True).encode("utf-8"))

            def log_message(self, *args, **kwargs):
                pass

        with socketserver.TCPServer(("", 0), Handler) as httpd:
            host, port = httpd.socket.getsockname()
            host = "localhost" if os.name == "nt" else host
            webbrowser.open("http://{}:{}".format(host, port))
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                pass


class NumPyJSONEncoder(json.JSONEncoder):
    """A JSON encoder which normalises NumPy arrays to lists before serialising.
    """

    def default(self, o):
        if hasattr(o, "tolist"):
            return o.tolist()
        super().default(o)
