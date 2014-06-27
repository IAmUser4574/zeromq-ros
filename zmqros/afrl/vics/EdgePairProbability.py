#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *


class EdgePairProbability(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 28
        self.SERIES_NAME = "VICS"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6217574784323026944
        self.SERIES_VERSION = 17

        #Define message fields
        self.EntryEdgeId = 0   #uint32
        self.ExitEdgeId = 0   #uint32
        self.TransitionProbability = 0   #real32


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">I", self.EntryEdgeId))
        buffer.append(struct.pack(">I", self.ExitEdgeId))
        buffer.append(struct.pack(">f", self.TransitionProbability))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.EntryEdgeId = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        self.ExitEdgeId = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        self.TransitionProbability = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        return _pos


    def get_EntryEdgeId(self):
        return self.EntryEdgeId

    def set_EntryEdgeId(self, value):
        self.EntryEdgeId = int( value )

    def get_ExitEdgeId(self):
        return self.ExitEdgeId

    def set_ExitEdgeId(self, value):
        self.ExitEdgeId = int( value )

    def get_TransitionProbability(self):
        return self.TransitionProbability

    def set_TransitionProbability(self, value):
        self.TransitionProbability = float( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From EdgePairProbability:\n"
        buf +=    "EntryEdgeId = " + str( self.EntryEdgeId ) + "\n" 
        buf +=    "ExitEdgeId = " + str( self.ExitEdgeId ) + "\n" 
        buf +=    "TransitionProbability = " + str( self.TransitionProbability ) + "\n" 

        return buf;

    def getLMCPType(self):
        return self.LMCP_TYPE

    def getSeriesName(self):
        return self.SERIES_NAME

    def getSeriesNameID(self):
        return self.SERIES_NAME_ID

    def getSeriesVersion(self):
        return self.SERIES_VERSION

    def toXMLStr(self, ws):
        str = ws + "<EdgePairProbability>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</EdgePairProbability>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<EntryEdgeId>" + str(self.EntryEdgeId) + "</EntryEdgeId>\n"
        buf += ws + "<ExitEdgeId>" + str(self.ExitEdgeId) + "</ExitEdgeId>\n"
        buf += ws + "<TransitionProbability>" + str(self.TransitionProbability) + "</TransitionProbability>\n"

        return buf
        
