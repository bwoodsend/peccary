import threading
import array
import webbrowser
from http.server import BaseHTTPRequestHandler

import pytest
import requests

from peccary import Scene


def test_basic():
    self = Scene(id="test")
    self.plot(x=[1, 2, 3], y=[9, 3, 5])
    assert self.to_html() == """\
<div id="test"></div>
<script type="text/javascript">
    Plotly.newPlot(document.getElementById('test'), [{"x":[1,2,3],"y":[9,3,5]}], {});
</script>
"""
    assert self.to_html(standalone=True).endswith(self.to_html())
    assert self.to_html(standalone=True).startswith("<!DOCTYPE html>")


def test_array_serialization():
    assert Scene()._dumps(array.array("L", [1, 2, 3])) == "[1,2,3]"
    with pytest.raises(TypeError):
        Scene()._dumps({1, 2})


def test_preview(monkeypatch):
    self = Scene()
    self.plot(x=[1, 2, 3], y=[9, 3, 5], text=["诶", "比", "西"])

    url = []

    # Hack the server/preview to send the URL to a local variable instead of the
    # browser and to raise a KeyboardInterrupt on receiving a POST request.
    def serve():

        @staticmethod
        def do_POST():
            raise KeyboardInterrupt

        monkeypatch.setattr(webbrowser, "open", url.append)
        monkeypatch.setattr(BaseHTTPRequestHandler, "do_POST", do_POST,
                            raising=False)
        self.preview()

    try:
        thread = threading.Thread(target=serve, daemon=True)
        thread.start()
        while not url:
            pass
        url, = url

        response = requests.get(url)
        assert response.ok
        assert response.text == self.to_html(standalone=True)

        # Currently, any request should result in the same page. I may change
        # this in future.
        response = requests.get(url + "/spaghetti?x=8")
        assert response.ok
        assert response.text == self.to_html(standalone=True)

    finally:
        try:
            # Signal the server to exit.
            requests.post(url)
        except requests.exceptions.ConnectionError:
            pass
