# Setting up the middleware
## Environment Variables
In order to use ZeroMQ-ROS, you must set a few environmental variables. These can
be set by exporting environmental variables in the terminal every time you start a
new terminal, or you can be sane and add them to your `.bashrc` or `.bash_profile`.
You must set variables described below. These environment variables need to be set on
every computer running ZeroMQ-ROS.

- `ZMQROS_NS_HOST` -- Host of the naming service
- `ZMQROS_NS_PORT` -- Port of the naming service
- `ZMQROS_ROBOT_ID` -- A unique identifying name of the robot running ZeroMQ-ROS
- `ZMQROS_ROOT` -- The location of the root directory of the ZeroMQ-ROS installation

## Database
Wherever you choose to run the name server, you must also be running a RethinkDB database.
This database stores the names and identification numbers of the agents you wish the name
server to supervise. For instance, if you work in a robotics lab, the database
will contain all of the names of the robots in your lab along with some identification number.
All of the names in the database do not need to be used at the same time, they are just there
for reference by the name server.
These names need to be known a priori for more efficient swarm creation and name allocation.
To do this run

    $ rethinkdb --bind all

This will run the RethinkDB instance. In order to populate the database, run Zui, the
ZeroMQ-ROS UI runnning,

    $ zmqros --ui
    
Then to populate the database visit, `localhost:9000/add`. The website will ask you for the
robot names and an identification number. This is useful so that you can link the robot
to IP addresses, Vicon identification and so on.
