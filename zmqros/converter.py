
from geometry_msgs.msg import Twist


def convert_avs_to_twist(avs):
    t = Twist()
    t.linear.x = avs.get_u()
    t.linear.y = avs.get_v()
    t.linear.z = avs.get_w()
    t.angular.x = avs.get_p()
    t.angular.y = avs.get_q()
    t.angular.z = avs.get_r()

    return t, Twist


converters = {
    "cmasi.AirVehicleState": convert_avs_to_twist
}

