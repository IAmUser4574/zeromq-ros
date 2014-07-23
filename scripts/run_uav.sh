
echo Robot ID: $ZMQROS_ROBOT_ID
echo Nameserver: http://$ZMQROS_NS_HOST:$ZMQROS_NS_PORT
python run.py --host $ZMQROS_NS_HOST --port $ZMQROS_NS_PORT --program client --name $ZMQROS_ROBOT_ID
