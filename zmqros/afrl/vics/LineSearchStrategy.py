#! /usr/bin/python

class LineSearchStrategy:

    Straight = 0
    TrackCrawl = 1
    CreepingLine = 2



def get_LineSearchStrategy_str(str):
    """
    Returns a numerical value from a string
    """
    if str == "Straight": return LineSearchStrategy.Straight
    if str == "TrackCrawl": return LineSearchStrategy.TrackCrawl
    if str == "CreepingLine": return LineSearchStrategy.CreepingLine


def get_LineSearchStrategy_int(val):
    """
    Returns a string representation from an int
    """
    if val == LineSearchStrategy.Straight: return "Straight"
    if val == LineSearchStrategy.TrackCrawl: return "TrackCrawl"
    if val == LineSearchStrategy.CreepingLine: return "CreepingLine"
    return LineSearchStrategy.Straight


