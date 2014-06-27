
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import zmqros
import time
import zmqros.afrl.cmasi.AirVehicleState as airvs


master = zmqros.Master("132.250.85.150", 5555)


def run():
    while True:
        avs = airvs.AirVehicleState()
        avs.set_u(10)
        master.send_lmcp("/cmd_vel", avs)
        time.sleep(1)

if __name__ == "__main__":
    run()
