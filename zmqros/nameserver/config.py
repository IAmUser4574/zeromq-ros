
from flask import Flask


app = Flask(__name__)
app.config.from_object(__name__)

store = None
live_robots = dict()
allocated_ports = dict()
min_port = 5555
max_port = 7555
heartbeat_delay = 5  # seconds
