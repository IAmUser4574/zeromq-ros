
import master
import json
import nsapi


class Swarm(object):

    def __init__(self, *args):
        self.masters = self.init_masters(args)
        self.id_mapping, self.name_mapping = self.init_vicon_mapping(args)

    def init_vicon_mapping(self, members):
        id_mapping = dict()
        name_mapping = dict()
        for member in members:
            id_mapping[member["id"]] = member["name"]
            name_mapping[member["name"]] = member["id"]

        return id_mapping, name_mapping

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

    def get_name_by_id(self, bot_id):
        return self.id_mapping[bot_id]

    def get_id_by_name(self, bot_name):
        return self.name_mapping[bot_name]

    def __getitem__(self, name):
        return self.masters[name]

    def __str__(self):
        return str(self.get_names())


def create_swarm_from_file(filename):
    with open(filename) as f:
        f_str = f.read()
        members = json.loads(f_str)
        swarm = Swarm(*members)
        return swarm


def create_swarm_from_ns(ns_host, ns_port):
    # Change this to specify what members
    ns = nsapi.NameServerAPI(ns_host, ns_port)
    names = ns.get_config()
    swarm = Swarm(*names)
    return swarm
