
import config
import json
from flask import jsonify


@config.app.route("/address/<name>", methods=["GET"])
def get_address(name):
    for name_dict in config.names["bots"]:
        if name_dict["name"] == name:
            return jsonify(
                host=name_dict["host"],
                port=name_dict["port"]
            )

    return jsonify(error=1, message="Name not found")


@config.app.route("/config", methods=["GET"])
def get_all():
    return json.dumps(config.names)
