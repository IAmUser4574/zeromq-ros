
import master
import json
import ns


class Swarm(object):

    def __init__(self, host):
        self.host = host
        self.masters = dict()
        self.name_to_id = dict()
        self.id_to_name = dict()

    def add_bot(self, name, bot_id, port):
        new_master = master.Master(self.host, port)
        self.masters[name] = new_master
        self.name_to_id[name] = bot_id
        self.id_to_name[bot_id] = name

    def send_message(self, bot_name, msg_type, topic_name, msg):
        self.masters[bot_name].send_message(msg_type, topic_name, msg)
        return self

    def get_names(self):
        return self.masters.keys()

    def get_bots(self):
        return self.masters.values()

    def get_name_by_id(self, bot_id):
        return self.id_to_name[bot_id]

    def get_id_by_name(self, bot_name):
        return self.name_to_id[bot_name]

    def __getitem__(self, name):
        return self.masters[name]

    def __str__(self):
        return str(self.get_names())


def create_swarm_from_ns(ns_host, ns_port, names):
    nserver = ns.NameServer(ns_host, ns_port)
    host, ports = nserver.create_swarm(names)
    swarm = Swarm(host)

    for name, port in zip(names, ports):
        bot_id = nserver.get_id(name)
        swarm.add_bot(name, bot_id, port)

    return swarm
