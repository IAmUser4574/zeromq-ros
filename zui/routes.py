
import config
from flask import jsonify
from std_msgs.msg import Empty
import zmqros


ns_host = zmqros.get_ns_host()
ns_port = zmqros.get_ns_port()
swarm = zmqros.coordinator.create_swarm_from_ns(ns_host, ns_port)


@config.app.route("/takeoff/<name>", methods=["POST"])
def takeoff(name):
    swarm[name].send_message(
        "std_msgs/Empty", "/takeoff", Empty()
    )
    return jsonify(error=0, message="No error")


@config.app.route("/land/<name>", methods=["POST"])
def land(name):
    swarm[name].send_message(
        "std_msgs/Empty", "/land", Empty()
    )
    return jsonify(error=0, message="No error")
