
import zmq
import json


#  Dictionary containing a mapping from route to callback
callback_functions = dict()

#  Default queue size used by the ROS publishers
DEFAULT_QUEUE_SIZE = 10

#  Publisher dictionary
publishers = dict()

class route(object):

    def __init__(self, route_name):
        self.route_name = route_name

    def __call__(self, f):
        global callback_functions
        try:
            callback_functions[self.route_name].append(f)
        except KeyError:
            callback_functions[self.route_name] = [f]
        return f


def create_addr(host, port):
    addr = "tcp://{}:{}".format(host, port)
    return addr


def run(host, port):
    """

    We expect messages to come in this format:

        {
            "route": <String: Some identifying keyword>
            "data": {
                "topic_name": <String>,
                "msg_type": <String: Namespaces delimitted by `/`>,
                "msg": <JSON Dictionary>
            } <JSON Dictionary: Associated data with route>
        }

    """

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
        callback_list = callback_functions[route_name]
        for callback in callback_list:
            callback(route_data)

    return 0
