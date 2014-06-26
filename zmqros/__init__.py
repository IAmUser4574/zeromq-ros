
__author__ = "Alexander Wallar <aw204@st-andrews.ac.uk>"


def run(host, port):
    """

    Runs the server.

    @param host The host for the server

    @param port The port for the server

    """

    import rospy
    rospy.init_node("zmqros_{}_{}".format(host, port))

    import config
    import topics

    config.run(host, int(port))
