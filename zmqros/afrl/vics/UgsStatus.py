#! /usr/bin/python

class UgsStatus:

    Green = 0
    Red = 1



def get_UgsStatus_str(str):
    """
    Returns a numerical value from a string
    """
    if str == "Green": return UgsStatus.Green
    if str == "Red": return UgsStatus.Red


def get_UgsStatus_int(val):
    """
    Returns a string representation from an int
    """
    if val == UgsStatus.Green: return "Green"
    if val == UgsStatus.Red: return "Red"
    return UgsStatus.Green


