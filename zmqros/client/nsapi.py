
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
        except TypeError:
            raise AttributeError("Robot does not exist --> {}".format(name))

    def get_config(self):
        req = urllib2.urlopen(self.address + "/config")
        resp = req.read()
        resp_dict = json.loads(resp)
        return resp_dict

    def get_alive(self):
        req = urllib2.urlopen(self.address + "/alive")
        resp = req.read()
        resp_dict = json.loads(resp)
        return resp_dict
