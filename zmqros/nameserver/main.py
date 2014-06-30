
import config
import json


def run(host, port, config_file):
    with open(config_file) as f:
        config_dict = json.loads(f.read())
        config.names = config_dict

    config.app.run(host, port, debug=True)
