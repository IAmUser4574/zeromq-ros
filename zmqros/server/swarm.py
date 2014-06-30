
import master
import json
import nsapi


class Swarm(object):

    def __init__(self, **kwargs):
        self.masters = self.init_masters(kwargs.get("bots"))

    def init_masters(self, members):
        masters = dict()
        for member in members:
            masters[member["name"]] = master.Master(
                member["host"], member["port"]
            )

        return masters

    def send_message(self, bot_name, msg_type, topic_name, msg):
        self.masters[bot_name].send_message(msg_type, topic_name, msg)
        return self

    def get_names(self):
        return self.masters.keys()

    def get_bots(self):
        return self.masters.values()

    def __getitem__(self, name):
        return self.masters[name]


def create_swarm_from_file(filename):
    with open(filename) as f:
        f_str = f.read()
        members = json.loads(f_str)
        swarm = Swarm(**members)
        return swarm


def create_swarm_from_ns(ns_host, ns_port):
    ns = nsapi.NameServerAPI(ns_host, ns_port)
    names = ns.get_config()
    swarm = Swarm(**names)
    return swarm
