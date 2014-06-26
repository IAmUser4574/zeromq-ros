
import zmq
import json
import time

addr = "tcp://127.0.0.1:5555"
ctx = zmq.Context()
pub = ctx.socket(zmq.PUB)
pub.bind(addr)

while True:
    msg_dict = {
        "route": "topic",
        "data": {
            "topic_name": "/cmd_vel",
            "msg_type": "geometry_msgs/Twist",
            "msg": {
                "linear": {
                    "x": 1,
                    "y": 2,
                    "z": 3
                }, "angular": {
                    "x": 0,
                    "y": 0,
                    "z": 1
                }
            }
        }
    }
    json_msg = json.dumps(msg_dict)
    pub.send(zmq.Message(json_msg))
    time.sleep(1)
