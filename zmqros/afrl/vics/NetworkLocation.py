#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *


class NetworkLocation(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 38
        self.SERIES_NAME = "VICS"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6217574784323026944
        self.SERIES_VERSION = 17

        #Define message fields
        self.NetworkId = 0   #uint32
        self.NetworkEdge = 0   #uint32
        self.EdgeLocation = 0   #real32


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">I", self.NetworkId))
        buffer.append(struct.pack(">I", self.NetworkEdge))
        buffer.append(struct.pack(">f", self.EdgeLocation))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.NetworkId = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        self.NetworkEdge = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        self.EdgeLocation = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        return _pos


    def get_NetworkId(self):
        return self.NetworkId

    def set_NetworkId(self, value):
        self.NetworkId = int( value )

    def get_NetworkEdge(self):
        return self.NetworkEdge

    def set_NetworkEdge(self, value):
        self.NetworkEdge = int( value )

    def get_EdgeLocation(self):
        return self.EdgeLocation

    def set_EdgeLocation(self, value):
        self.EdgeLocation = float( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From NetworkLocation:\n"
        buf +=    "NetworkId = " + str( self.NetworkId ) + "\n" 
        buf +=    "NetworkEdge = " + str( self.NetworkEdge ) + "\n" 
        buf +=    "EdgeLocation = " + str( self.EdgeLocation ) + "\n" 

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
        str = ws + "<NetworkLocation>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</NetworkLocation>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<NetworkId>" + str(self.NetworkId) + "</NetworkId>\n"
        buf += ws + "<NetworkEdge>" + str(self.NetworkEdge) + "</NetworkEdge>\n"
        buf += ws + "<EdgeLocation>" + str(self.EdgeLocation) + "</EdgeLocation>\n"

        return buf
        
