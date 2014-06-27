#! /usr/bin/python

class State:

    NoState = 0
    Unknown = 1
    Patrol = 2
    Isolate = 3
    Capture = 4
    Deliver = 5
    Response = 6



def get_State_str(str):
    """
    Returns a numerical value from a string
    """
    if str == "NoState": return State.NoState
    if str == "Unknown": return State.Unknown
    if str == "Patrol": return State.Patrol
    if str == "Isolate": return State.Isolate
    if str == "Capture": return State.Capture
    if str == "Deliver": return State.Deliver
    if str == "Response": return State.Response


def get_State_int(val):
    """
    Returns a string representation from an int
    """
    if val == State.NoState: return "NoState"
    if val == State.Unknown: return "Unknown"
    if val == State.Patrol: return "Patrol"
    if val == State.Isolate: return "Isolate"
    if val == State.Capture: return "Capture"
    if val == State.Deliver: return "Deliver"
    if val == State.Response: return "Response"
    return State.NoState


