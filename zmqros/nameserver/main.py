
import config
import json
import db


def run(host, port, config_file):
    with open(config_file) as f:
        config_data = json.loads(f.read())
        config.store = db.Db()
        config.store.put_config(config_data)
        config.app.run(host, port, debug=True)
