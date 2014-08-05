# Running

1. First run the name server and populate the database with robot information. This step does 
not need to occur every time you run the swarm, however, the name server needs to be running for
agents and coordinators to communicate. The agents and the coordinators need to have their
environment variables pointing to the address and port the name server will be running from.
    - `$ zmqros --ns`
2. On all of the agents in the swarm that are specified in the name server, run the agent code. 
This step also does not need to occur everytime the swarm is to be controlled, however to control an agent,
the agent program must be running.
    - `$ zmqros --agent`
3. Run the coordinator code from where ever the coordinator is located.
4. (Optional) Now you are able to control the swarm. To look at properties in the swarm, run Zui, the web app for the
middleware. Using Zui, you will be able to look at the members of the swarm that are currently alive and
send ROS messages to them through a GUI.
    - `$ zmqros --ui`
