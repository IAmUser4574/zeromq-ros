
import config
import zmq
import json
from util import create_addr
import rospy
import nsapi


def run(ns_host, ns_port, name):
    """
    Runs the server. We expect messages to come in this format:

        {
            "route": <String: Some identifying keyword>
            "data": {
                "topic_name": <String>,
                "msg_type": <String: Namespaces delimitted by `/`>,
                "msg": <JSON Dictionary>
            } <JSON Dictionary: Associated data with route>
        }

    """


    ns = nsapi.NameServerAPI(ns_host, ns_port)
    host, port = ns.get_address(name)

    rospy.init_node("zmqros_{}_{}".format(host.replace(".", "_"), port))
    addr = create_addr(host, port)
    context = zmq.Context()
    sub = context.socket(zmq.SUB)
    sub.setsockopt(zmq.SUBSCRIBE, "")
    sub.connect(addr)

    done = False

    while not done:
        zmq_msg = sub.recv()
        zmq_dict = json.loads(zmq_msg)
        route_name = zmq_dict["route"]
        route_data = zmq_dict["data"]
        callback_list = config.callback_functions[route_name]
        for callback in callback_list:
            callback(route_data)
