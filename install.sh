
#!/bin/bash

echo
echo I am assuming you have ROS installed...
echo

echo
echo Installing Pip
echo
sudo apt-get install python-pip

echo
echo Installing Pip requirements.txt
echo
sudo pip install -r requirements.txt

echo 
echo Installing rospy_message_converter
echo
mkdir resources;
cd resources; git clone https://github.com/baalexander/rospy_message_converter.git; cd -;
cd resources/rospy_message_converter; sudo python setup.py install; cd -;

echo
echo Installing RethinkDB
echo
source /etc/lsb-release && echo "deb http://download.rethinkdb.com/apt $DISTRIB_CODENAME main" | sudo tee /etc/apt/sources.list.d/rethinkdb.list
wget -qO- http://download.rethinkdb.com/apt/pubkey.gpg | sudo apt-key add -
sudo apt-get update
sudo apt-get install rethinkdb
sudo pip install rethinkdb

echo
echo Installing ZeroMQ-Ros
echo
sudo python setup.py install

echo
echo Done!
echo
