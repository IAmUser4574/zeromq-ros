#! /usr/bin/python

class PayloadPowerItem:

    WiFi = 0
    VideoTransmitter = 1
    ExternalCamera = 2
    AxisBox = 3



def get_PayloadPowerItem_str(str):
    """
    Returns a numerical value from a string
    """
    if str == "WiFi": return PayloadPowerItem.WiFi
    if str == "VideoTransmitter": return PayloadPowerItem.VideoTransmitter
    if str == "ExternalCamera": return PayloadPowerItem.ExternalCamera
    if str == "AxisBox": return PayloadPowerItem.AxisBox


def get_PayloadPowerItem_int(val):
    """
    Returns a string representation from an int
    """
    if val == PayloadPowerItem.WiFi: return "WiFi"
    if val == PayloadPowerItem.VideoTransmitter: return "VideoTransmitter"
    if val == PayloadPowerItem.ExternalCamera: return "ExternalCamera"
    if val == PayloadPowerItem.AxisBox: return "AxisBox"
    return PayloadPowerItem.WiFi


