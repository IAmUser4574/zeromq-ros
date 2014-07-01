
import config
import json
from flask import jsonify


@config.app.route("/address/<name>", methods=["GET"])
def get_address(name):
    db_data = config.store.get_address(name)
    return json.dumps(db_data)


@config.app.route("/config", methods=["GET"])
def get_config():
    return json.dumps(config.store.get_config())
