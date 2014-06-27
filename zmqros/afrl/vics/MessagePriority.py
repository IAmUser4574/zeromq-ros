#! /usr/bin/python

class MessagePriority:

    Low = 0
    Normal = 1
    High = 2



def get_MessagePriority_str(str):
    """
    Returns a numerical value from a string
    """
    if str == "Low": return MessagePriority.Low
    if str == "Normal": return MessagePriority.Normal
    if str == "High": return MessagePriority.High


def get_MessagePriority_int(val):
    """
    Returns a string representation from an int
    """
    if val == MessagePriority.Low: return "Low"
    if val == MessagePriority.Normal: return "Normal"
    if val == MessagePriority.High: return "High"
    return MessagePriority.Low


