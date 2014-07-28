
import config
import json
import time
from flask import request, jsonify
import util


@config.app.route("/address/<name>", methods=["GET"])
@util.crossdomain(origin='*')
def get_address(name):
    """
    Route that gets the host and port information about the ZeroMQ
    channel that the robot with name, <name>, talks to

    Input: <name> --> String

    Output: {
        "host": <String>,
        "port": <Int>
    }

    """

    db_data = config.store.get_address(name)
    return json.dumps(db_data)


@config.app.route("/config", methods=["GET"])
@util.crossdomain(origin='*')
def get_config():
    """
    Route that dumps the entire naming database into JSON and
    returns it to the requesting agent

    Input: None

    Output: [
        {
            "host": <String>,
            "port": <Int>,
            "name": <String>
        }, ...
    ]
    """

    return json.dumps(config.store.get_config())


@config.app.route("/create_swarm", methods=["GET"])
@util.crossdomain(origin="*")
def create_swarm():
    """
    Dynamically allocates ports for ZeroMQ channels

    Input: [<String: Name of robots in your swarm>]

    Output: [
        {
            "host": <String>,
            "port": <Int>,
            "name": <String>
        }
    ]

    """

    try:
        used_ports = config.allocated_ports[request.remote_addr]
    except KeyError:
        used_ports = list()

    raise NotImplementedError("Will do this in a sec " + used_ports)


@config.app.route("/alive", methods=["GET"])
@util.crossdomain(origin='*')
def get_alive():
    """
    Route that returns a address information of all the robots who have
    checked in with the server in the last 5 seconds. This shows the
    robots that are "alive".

    Input: None

    Output: [
        {
            "host": <String>,
            "port": <Int>,
            "name": <String>
        }, ...
    ]

    """

    addr_list = list()
    current_time = time.time()
    for name, check_in_time in config.live_robots.iteritems():
        time_diff = current_time - check_in_time
        if time_diff <= config.heartbeat_delay:
            addr_list.append(config.store.get_address(name))

    return json.dumps(addr_list)


@config.app.route("/alive/<name>", methods=["GET"])
@util.crossdomain(origin='*')
def get_robot_alive(name):
    """
    Route that checks if a robot is alive

    Input: <name> --> <String>

    Output: Boolean

    """
    try:
        time_diff = time.time() - config.live_robots[name]
        return jsonify(alive=time_diff < config.heartbeat_delay)
    except KeyError:
        return jsonify(alive=False)


@config.app.route("/alive", methods=["POST"])
@util.crossdomain(origin='*')
def post_alive():
    """
    Route that allows for alive robots to post update the main server
    if they are alive.

    Input: {
        "name": <String>
    }

    Output: {
        "error": <Int>,
        "message": <String>
    }

    """

    name = request.form["name"]
    config.live_robots[name] = time.time()

    return jsonify(error=0, message="No error")
