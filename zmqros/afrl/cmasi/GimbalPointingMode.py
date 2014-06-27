#! /usr/bin/python

class GimbalPointingMode:

    AirVehicleRelativeAngle = 0
    AirVehicleRelativeSlewRate = 1
    LatLonSlaved = 2
    InertialRelativeSlewRate = 3
    Scan = 4



def get_GimbalPointingMode_str(str):
    """
    Returns a numerical value from a string
    """
    if str == "AirVehicleRelativeAngle": return GimbalPointingMode.AirVehicleRelativeAngle
    if str == "AirVehicleRelativeSlewRate": return GimbalPointingMode.AirVehicleRelativeSlewRate
    if str == "LatLonSlaved": return GimbalPointingMode.LatLonSlaved
    if str == "InertialRelativeSlewRate": return GimbalPointingMode.InertialRelativeSlewRate
    if str == "Scan": return GimbalPointingMode.Scan


def get_GimbalPointingMode_int(val):
    """
    Returns a string representation from an int
    """
    if val == GimbalPointingMode.AirVehicleRelativeAngle: return "AirVehicleRelativeAngle"
    if val == GimbalPointingMode.AirVehicleRelativeSlewRate: return "AirVehicleRelativeSlewRate"
    if val == GimbalPointingMode.LatLonSlaved: return "LatLonSlaved"
    if val == GimbalPointingMode.InertialRelativeSlewRate: return "InertialRelativeSlewRate"
    if val == GimbalPointingMode.Scan: return "Scan"
    return GimbalPointingMode.AirVehicleRelativeAngle


