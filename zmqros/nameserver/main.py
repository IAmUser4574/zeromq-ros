
import config
import json
import db


def run(host, port, config_file):
    config.store = db.Db()

    try:
        with open(config_file) as f:
            config_data = json.loads(f.read())
            config.store.put_config(config_data)
    except TypeError:
        pass

    config.app.run(host, port, debug=True)
