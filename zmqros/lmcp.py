
import rospy
import config
import converter
import afrl.lmcp.LMCPFactory as lmcpfac


@config.route("lmcp")
def post_lmcp(form):
    """
    Input:
        {
            "topic_name": <String>,
            "msg": <LMCP encoded string>
        }

    """

    topic_name = form["topic_name"]
    lmcp_obj = lmcpfac.internalFactory.getObject(form["msg"])
    converter_func = converter.converters[lmcp_obj.__module__]
    ros_msg, msg_cls = converter_func(lmcp_obj)

    if not topic_name in config.publishers:
        ros_pub = rospy.Publisher(
            topic_name, msg_cls
        )
        config.publishers[topic_name] = ros_pub

    config.publishers[topic_name].publish(ros_msg)

    return ros_msg
