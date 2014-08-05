# Architecture
## Agents

Agents are members of the swarm that will be controlled by a coordinator. They are referenced by
a unique identifying name and listen for JSON serialized ROS messages on a message queue. These
serialized messages are then constructed into ROS messages and published to the associated topic.

## Coordinators

Coordinators are the controllers of the swarm. They can send JSON serialized ROS messages to agents
that get published to the associated topic on the agent's ROS master. To enable bi-directional,
coordinators can also be agents and listen for messages.

## Naming service

The naming service is used to associate a robot's unique name to a host and port of the ZeroMQ
message queue. This is vital for having dynamic swarm membership because instead of manually sharing
a configuration file, a persistent, centralized server runs that holds all of this information. Also,
the naming service holds a record of what agents are currently *alive* and able to be used.
