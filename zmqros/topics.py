
import config
from rospy_message_converter import message_converter


def create_msg(msg_dict, msg_type):
    msg = message_converter.convert_dictionary_to_ros_message(
        msg_type, msg_dict
    )
    return msg


@config.route("topic")
def post_topic(form):
    """
    Input:
        {
            "topic_name": <String>,
            "msg_type": <String: Namespaces delimited by `/`>,
            "msg": <JSON Dictionary>
        }

    Output:
        {
            "error": <Int>,
            "message": <String>
        }

    """

    msg = create_msg(form["msg"], form["msg_type"])
    print msg
    return msg
