#! /usr/bin/python

class VicsEntityType:

    Unknown = 0
    VSCS_Ground = 1
    Dismount = 2
    Aircraft = 3
    UGS = 4



def get_VicsEntityType_str(str):
    """
    Returns a numerical value from a string
    """
    if str == "Unknown": return VicsEntityType.Unknown
    if str == "VSCS_Ground": return VicsEntityType.VSCS_Ground
    if str == "Dismount": return VicsEntityType.Dismount
    if str == "Aircraft": return VicsEntityType.Aircraft
    if str == "UGS": return VicsEntityType.UGS


def get_VicsEntityType_int(val):
    """
    Returns a string representation from an int
    """
    if val == VicsEntityType.Unknown: return "Unknown"
    if val == VicsEntityType.VSCS_Ground: return "VSCS_Ground"
    if val == VicsEntityType.Dismount: return "Dismount"
    if val == VicsEntityType.Aircraft: return "Aircraft"
    if val == VicsEntityType.UGS: return "UGS"
    return VicsEntityType.Unknown


