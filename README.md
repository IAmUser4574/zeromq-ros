ZeroMQ-ROS
========

ZeroMQ-ROS is a middleware that allows for the control of multiple ROS masters from
a single coordinator and makes it easy to create swarm applications using the standard
ROS framework. ZeroMQ-ROS uses the ZeroMQ message queue to communicate between the coordinator
and the agents.

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
