
from flask import render_template
from flask import Response
import config


@config.app.route("/<filename>", methods=["GET"])
def serve_html_Page(filename):
    if filename == "favicon.ico":
        with open(config.STATIC_DIR + "img/favicon.ico") as f:
            return Response(f.read(), mimetype="image/x-icon")

    return render_template(filename)


@config.app.route("/", methods=["GET"])
def serve_index():
    return render_template("index.html")


@config.app.route("/<filetype>/<filename>", methods=["GET"])
def serve_script(filetype, filename):
    """ Serves the script """
    with open(config.STATIC_DIR + filetype + "/" + filename) as f:
        return Response(f.read(), mimetype=config.MIME_DICT[filetype])
