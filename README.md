ZeroMQ-ROS
========

ZeroMQ-ROS is a middleware that allows for the control of multiple ROS masters from
a single coordinator and makes it easy to create swarm applications using the standard
ROS framework. ZeroMQ-ROS uses the ZeroMQ message queue to communicate between the coordinator
and the agents.

## Architecture
#### Agents

Agents are members of the swarm that will be controlled by a coordinator. They are referenced by
a unique identifying name and listen for JSON serialized ROS messages on a message queue. These
serialized messages are then constructed into ROS messages and published to the associated topic.

#### Coordinators

Coordinators are the controllers of the swarm. They can send JSON serialized ROS messages to agents
that get published to the associated topic on the agent's ROS master.

#### Naming service

The naming service is used to associate a robot's unique name to a host and port of the ZeroMQ
message queue. This is vital for having dynamic swarm membership because instead of manually sharing
a configuration file, a persistent, centralized server runs that holds all of this information. Also,
the naming service holds a record of what agents are currently *alive* and able to be used.

## Install

**[Warning] You must already have ROS installed on all machines you would like
to have in your swarm**

    $ git clone https://github.com/wallarelvo/zeromq-ros.git
    $ make
    
## Setting up the middleware

In order to use ZeroMQ-ROS, you must set a few environmental variables. These can
be set by exporting environmental variables in the terminal every time you start a
new terminal, or you can be sane and add them to your `.bashrc` or `.bash_profile`.
You must set variables described below. These environment variables need to be set on
every computer running ZeroMQ-ROS.

- `ZMQROS_NS_HOST` --> Host of the naming service
- `ZMQROS_NS_PORT` --> Port of the naming service
- `ZMQROS_ROBOT_ID` --> A unique identifying name of the robot running ZeroMQ-ROS
- `ZMQROS_ROOT` --> The location of the root directory of the ZeroMQ-ROS installation

## Running

1. First run the name server and populate the database with robot information. This step does 
not need to occur every time you run the swarm, however, the name server needs to be running for
agents and coordinator nodes to function.

    - `$ zmqros --ns`
    
2. On all of the agents in the swarm that are specified in the name server, run the agent code. 
This step also does not need to occur everytime the swarm is to be controlled, however to control an agent,
the agent program must be running.

    - `$ zmqros --agent`
    
3. Run the coordinator code from where ever the coordinator is located.

## Coordinator example

```python
import zmqros
import random
import time
from geometry_msgs.msg import Twist

ns_host = zmqros.get_ns_host()
ns_port = zmqros.get_ns_port()
swarm = zmqros.coordinator.create_swarm_from_ns(ns_host, ns_port)


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
```
