
from flask import render_template, Response, redirect
import config

""" Directory for static files """
STATIC_DIR = "static/"

""" Mime type dictionary """
MIME_DICT = {
    "js": "text/javascript",
    "css": "text/css",
    "img": "image/png",
    "libraries": "text/javascript",
    "data": "text/csv"
}

@config.app.route("/", methods=["GET"])
def serve_index():
    return redirect("/index.html")

@config.app.route("/<filename>", methods=["GET"])
def serve_html_page(filename):
    if filename == "favicon.ico":
        with open(STATIC_DIR + "img/favicon.ico") as f:
            return Response(f.read(), mimetype = "image/x-icon")

    return render_template(filename)

@config.app.route("/<filetype>/<filename>", methods=["GET"])
def serve_script(filetype, filename):
    """ Serves the script """
    with open(STATIC_DIR + filetype + "/" + filename) as f:
        return Response(f.read(), mimetype = MIME_DICT[filetype])
