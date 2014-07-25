
from flask import Flask

#  Object for route registration
app = Flask(__name__)
app.config.from_object(__name__)

#  Directory for static files
STATIC_DIR = "zui/static/"

#  Mime type dictionary
MIME_DICT = {
    "js": "text/javascript",
    "css": "text/css",
    "img": "image/png",
    "libraries": "text/javascript",
    "data": "text/csv"
}
