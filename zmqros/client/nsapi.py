
import urllib2
import json


class NameServerAPI(object):

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.address = "http://{}:{}".format(host, port)

    def get_address(self, name):
        req = urllib2.urlopen(self.address + "/address/{}".format(name))
        resp = req.read()
        resp_dict = json.loads(resp)
        try:
            return resp_dict["host"], resp_dict["port"]
        except KeyError:
            return None
