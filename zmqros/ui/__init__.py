
__author__ = "Alexander Wallar <aw204@st-andrews.ac.uk>"

__all__ = ["pages"]


import pages
import config


def run(host, port):
    config.app.run(host=host, port=int(port), debug=True)

