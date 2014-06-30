
__author__ = "Alexander Wallar <aw204@st-andrews.ac.uk>"
__all__ = ["Master", "swarm", "topics", "log"]

from master import Master
import swarm
import topics
import log


def run(host, port):
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

    import config
    import zmq
    import json
    from util import create_addr
    import rospy

    rospy.init_node("zmqros_{}_{}".format(host.replace(".", "_"), port))

    done = False
    addr = create_addr(host, port)
    context = zmq.Context()
    sub = context.socket(zmq.SUB)
    sub.setsockopt(zmq.SUBSCRIBE, "")
    sub.connect(addr)

    while not done:
        zmq_msg = sub.recv()
        zmq_dict = json.loads(zmq_msg)
        route_name = zmq_dict["route"]
        route_data = zmq_dict["data"]
        callback_list = config.callback_functions[route_name]
        for callback in callback_list:
            callback(route_data)
