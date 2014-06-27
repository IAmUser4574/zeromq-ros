#! /usr/bin/python

class AreaSearchStrategy:

    ParallelSweep = 0
    ExpandingSquare = 1
    SectorSearch = 2



def get_AreaSearchStrategy_str(str):
    """
    Returns a numerical value from a string
    """
    if str == "ParallelSweep": return AreaSearchStrategy.ParallelSweep
    if str == "ExpandingSquare": return AreaSearchStrategy.ExpandingSquare
    if str == "SectorSearch": return AreaSearchStrategy.SectorSearch


def get_AreaSearchStrategy_int(val):
    """
    Returns a string representation from an int
    """
    if val == AreaSearchStrategy.ParallelSweep: return "ParallelSweep"
    if val == AreaSearchStrategy.ExpandingSquare: return "ExpandingSquare"
    if val == AreaSearchStrategy.SectorSearch: return "SectorSearch"
    return AreaSearchStrategy.ParallelSweep


