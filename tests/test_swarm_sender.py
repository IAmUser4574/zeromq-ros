
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import zmqros.server
import random
import time
from geometry_msgs.msg import Twist

ns_host = "132.250.85.150"
ns_port = 8000
swarm = zmqros.server.create_swarm_from_ns(ns_host, ns_port)


def run():
    while True:
        for bot in swarm.get_bots():
            t = Twist()
            t.linear.x = random.random()
            t.linear.y = random.random()
            t.linear.z = random.random()
            t.angular.x = random.random()
            t.angular.y = random.random()
            t.angular.z = random.random()

            bot.send_message("geometry_msgs/Twist", "/cmd_vel", t)

        time.sleep(0.1)

if __name__ == "__main__":
    run()
