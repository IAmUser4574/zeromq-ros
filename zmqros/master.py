
import json
import zmq
import afrl.lmcp.LMCPFactory as lmpcfac
from rospy_message_converter import message_converter


class Master(object):

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.addr = self.generate_address()
        self.init_pub()

    def init_pub(self):
        ctx = zmq.Context()
        self.pub = ctx.socket(zmq.PUB)
        self.pub.bind(self.addr)

    def send_message(self, msg_type, topic_name, msg):
        msg_dict = message_converter.convert_ros_message_to_dictionary(msg)
        send_dict = dict()
        send_dict["route"] = "topic"
        data_dict = dict()
        data_dict["topic_name"] = topic_name
        data_dict["msg_type"] = msg_type
        data_dict["msg"] = msg_dict
        send_dict["data"] = data_dict
        json_msg = json.dumps(send_dict)
        self.pub.send(zmq.Message(json_msg))
        return send_dict

    def send_lmcp(self, topic_name, lmcp_obj):
        msg_str = lmpcfac.packMessage(lmcp_obj, False)
        send_dict = dict()
        send_dict["route"] = "lmcp"
        data_dict = dict()
        data_dict["topic_name"] = topic_name
        data_dict["msg"] = msg_str
        send_dict["data"] = data_dict
        json_msg = json.dumps(send_dict)
        self.pub.send(zmq.Message(json_msg))
        return send_dict

    def generate_address(self):
        return "tcp://{}:{}".format(self.host, self.port)
