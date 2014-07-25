
__author__ = "Alexander Wallar <aw204@st-andrews.ac.uk>"

__all__ = ["pages", "routes"]


import pages
from config import app
import routes


def run(host, port):
    app.run(host=host, port=int(port), debug=False)
