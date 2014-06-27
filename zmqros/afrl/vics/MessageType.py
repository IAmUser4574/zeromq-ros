#! /usr/bin/python

class MessageType:

    DismountMessage = 0
    StateTransition = 1
    IntruderAlert = 2



def get_MessageType_str(str):
    """
    Returns a numerical value from a string
    """
    if str == "DismountMessage": return MessageType.DismountMessage
    if str == "StateTransition": return MessageType.StateTransition
    if str == "IntruderAlert": return MessageType.IntruderAlert


def get_MessageType_int(val):
    """
    Returns a string representation from an int
    """
    if val == MessageType.DismountMessage: return "DismountMessage"
    if val == MessageType.StateTransition: return "StateTransition"
    if val == MessageType.IntruderAlert: return "IntruderAlert"
    return MessageType.DismountMessage


