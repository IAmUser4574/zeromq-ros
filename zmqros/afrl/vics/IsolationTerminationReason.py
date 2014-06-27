#! /usr/bin/python

class IsolationTerminationReason:

    FalseAlarm = 0
    IntruderEscape = 1
    IntruderCapture = 2



def get_IsolationTerminationReason_str(str):
    """
    Returns a numerical value from a string
    """
    if str == "FalseAlarm": return IsolationTerminationReason.FalseAlarm
    if str == "IntruderEscape": return IsolationTerminationReason.IntruderEscape
    if str == "IntruderCapture": return IsolationTerminationReason.IntruderCapture


def get_IsolationTerminationReason_int(val):
    """
    Returns a string representation from an int
    """
    if val == IsolationTerminationReason.FalseAlarm: return "FalseAlarm"
    if val == IsolationTerminationReason.IntruderEscape: return "IntruderEscape"
    if val == IsolationTerminationReason.IntruderCapture: return "IntruderCapture"
    return IsolationTerminationReason.FalseAlarm


