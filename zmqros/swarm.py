
import zmqros
import json


class Swarm(object):

    def __init__(self, *args):
        self.masters = self.init_masters(args)

    def init_masters(self, members):
        masters = dict()
        for member in members:
            masters[member["name"]] = zmqros.Master(
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
        swarm = Swarm(*members)
        return swarm
