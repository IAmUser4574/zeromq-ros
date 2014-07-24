echo 
echo Installing rospy_message_converter
echo
mkdir resources;
cd resources; git clone https://github.com/baalexander/rospy_message_converter.git; cd -;
cd resources/rospy_message_converter; sudo python setup.py install; cd -;
