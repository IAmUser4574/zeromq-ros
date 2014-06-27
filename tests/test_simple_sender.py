
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import zmqros
import random
import time
from geometry_msgs.msg import Twist

master = zmqros.Master("132.250.85.150", 8317)

def run():
    while True:
        t = Twist()
        t.linear.x = random.random()
        t.linear.y = random.random()
        t.linear.z = random.random()
        t.angular.x = random.random()
        t.angular.y = random.random()
        t.angular.z = random.random()

        master.send_message("geometry_msgs/Twist", "/cmd_vel", t)
        time.sleep(1)

if __name__ == "__main__":
    run()
