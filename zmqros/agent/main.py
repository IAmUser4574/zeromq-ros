
import config
import zmq
import json
from util import create_addr
import rospy
import nsapi
import heartbeat


def get_subscriber(host, port):
    addr = create_addr(host, port)
    context = zmq.Context()
    sub = context.socket(zmq.SUB)
    sub.setsockopt(zmq.SUBSCRIBE, "")
    sub.connect(addr)
    return sub


def init_ros_node(host, port):
    host_str = host.replace(".", "_")
    node_name = "zmqros_{}_{}".format(host_str, port)
    rospy.init_node(node_name)


def run(ns_host, ns_port, name):
    """
    Runs the server. We expect messages to come in this format:

        {
            "route": <String: Some identifying keyword>
            "data": {
                "topic_name": <String>,
                "msg_type": <String: Namespaces delimitted by `/`>,
                "msg": <JSON Dictionary>
            }
        }

    """

    ns = nsapi.NameServerAPI(ns_host, ns_port)
    host, port = ns.get_address(name)
    sub = get_subscriber(host, port)
    init_ros_node(host, port)
    heart = heartbeat.Heartbeat(host, port, name, ns_host, ns_port)
    heart.start()

    while True:
        try:
            zmq_msg = sub.recv()
            zmq_dict = json.loads(zmq_msg)
            route_name = zmq_dict["route"]
            route_data = zmq_dict["data"]
            callback_list = config.callback_functions[route_name]
            for callback in callback_list:
                callback(route_data)
        except KeyboardInterrupt:
            heart.kill()
            exit()
