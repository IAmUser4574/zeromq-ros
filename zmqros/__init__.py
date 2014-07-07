
__author__ = "Alexander Wallar <aw204@st-andrews.ac.uk>"

__all__ = ["server", "client", "nameserver", "get_ns_host", "get_ns_port"]

import server
import client
import nameserver
import os


NS_HOST_ID = "ZMQROS_NS_HOST"
NS_PORT_ID = "ZMQROS_NS_PORT"


def get_ns_host():
    try:
        return os.environ[NS_HOST_ID]
    except KeyError:
        raise OSError("NS_HOST_ID not found")


def get_ns_port():
    try:
        return int(os.environ[NS_PORT_ID])
    except KeyError:
        raise OSError("NS_PORT_ID not found")
    except ValueError:
        raise OSError("NS_PORT_ID must be an integer")
