#! /usr/bin/python

class FuzzyEdgeValue:

    VeryUnlikely = 0
    SomewhatUnlikely = 1
    Neutral = 2
    SomewhatLikely = 3
    VeryLikely = 4



def get_FuzzyEdgeValue_str(str):
    """
    Returns a numerical value from a string
    """
    if str == "VeryUnlikely": return FuzzyEdgeValue.VeryUnlikely
    if str == "SomewhatUnlikely": return FuzzyEdgeValue.SomewhatUnlikely
    if str == "Neutral": return FuzzyEdgeValue.Neutral
    if str == "SomewhatLikely": return FuzzyEdgeValue.SomewhatLikely
    if str == "VeryLikely": return FuzzyEdgeValue.VeryLikely


def get_FuzzyEdgeValue_int(val):
    """
    Returns a string representation from an int
    """
    if val == FuzzyEdgeValue.VeryUnlikely: return "VeryUnlikely"
    if val == FuzzyEdgeValue.SomewhatUnlikely: return "SomewhatUnlikely"
    if val == FuzzyEdgeValue.Neutral: return "Neutral"
    if val == FuzzyEdgeValue.SomewhatLikely: return "SomewhatLikely"
    if val == FuzzyEdgeValue.VeryLikely: return "VeryLikely"
    return FuzzyEdgeValue.VeryUnlikely


