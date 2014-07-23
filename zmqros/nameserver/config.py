
from flask import Flask


app = Flask(__name__)
app.config.from_object(__name__)

store = None
live_robots = dict()
heartbeat_delay = 5  # seconds
