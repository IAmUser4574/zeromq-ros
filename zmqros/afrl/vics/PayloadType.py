#! /usr/bin/python

class PayloadType:

    NoPayload = 0
    Unknown = 1
    Text = 2
    Image = 3
    Video = 4
    Audio = 5



def get_PayloadType_str(str):
    """
    Returns a numerical value from a string
    """
    if str == "NoPayload": return PayloadType.NoPayload
    if str == "Unknown": return PayloadType.Unknown
    if str == "Text": return PayloadType.Text
    if str == "Image": return PayloadType.Image
    if str == "Video": return PayloadType.Video
    if str == "Audio": return PayloadType.Audio


def get_PayloadType_int(val):
    """
    Returns a string representation from an int
    """
    if val == PayloadType.NoPayload: return "NoPayload"
    if val == PayloadType.Unknown: return "Unknown"
    if val == PayloadType.Text: return "Text"
    if val == PayloadType.Image: return "Image"
    if val == PayloadType.Video: return "Video"
    if val == PayloadType.Audio: return "Audio"
    return PayloadType.NoPayload


