
all: ipip pipr rmc rethink zmqr bin done
	@echo
	@echo I am assuming you have ROS installed...
	@echo

ipip:
	@echo
	@echo Installing Pip
	@echo
	sudo apt-get install python-pip

pipr:
	@echo
	@echo Installing Pip requirements.txt
	@echo
	sudo pip install -r requirements.txt

rmc:
	bash scripts/install_rmc.sh

rethink:
	bash scripts/install_rethink.sh

zmqr: 
	@echo
	@echo Installing ZeroMQ-Ros
	@echo
	sudo python setup.py install

bin: zmqr
	@echo
	@echo Adding Binaries to /usr/local/
	@echo
	chmod a+x bin/*
	sudo cp bin/zmqros /usr/bin/zmqros
	sudo cp bin/zmqros /usr/local/bin

clean:
	sudo rm -rf resources

done:
	@echo
	@echo Remember to set the environment variables
	@echo
