#! /usr/bin/python

class IntruderType:

    NoDetection = 0
    Unknown = 1
    UGSDetect = 2
    Dismount = 3
    FourWheeledVehicle = 4
    TreadedVehicle = 5



def get_IntruderType_str(str):
    """
    Returns a numerical value from a string
    """
    if str == "NoDetection": return IntruderType.NoDetection
    if str == "Unknown": return IntruderType.Unknown
    if str == "UGSDetect": return IntruderType.UGSDetect
    if str == "Dismount": return IntruderType.Dismount
    if str == "FourWheeledVehicle": return IntruderType.FourWheeledVehicle
    if str == "TreadedVehicle": return IntruderType.TreadedVehicle


def get_IntruderType_int(val):
    """
    Returns a string representation from an int
    """
    if val == IntruderType.NoDetection: return "NoDetection"
    if val == IntruderType.Unknown: return "Unknown"
    if val == IntruderType.UGSDetect: return "UGSDetect"
    if val == IntruderType.Dismount: return "Dismount"
    if val == IntruderType.FourWheeledVehicle: return "FourWheeledVehicle"
    if val == IntruderType.TreadedVehicle: return "TreadedVehicle"
    return IntruderType.NoDetection


