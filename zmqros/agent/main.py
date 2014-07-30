
import config
import zmq
import json
from util import create_addr
import rospy
import ns
import heartbeat
import subscriber
import time


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

    nserver = ns.NameServer(ns_host, ns_port)
    rospy.init_node("zmqros", anonymous=False, disable_signals=True)
    heart = heartbeat.Heartbeat(name, ns_host, ns_port)
    heart.start()
    thread_list = list()

    while True:
        try:
            new_conns = nserver.get_new_connections(name)
            for conn in new_conns:
                sub = subscriber.Subscriber(conn["host"], conn["port"])
                sub.start()
                thread_list.append(sub)
            time.sleep(2)
        except KeyboardInterrupt:
            heart.kill()
            for thr in thread_list:
                thr.kill()
            exit()
