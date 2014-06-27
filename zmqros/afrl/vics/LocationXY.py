#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *


class LocationXY(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 27
        self.SERIES_NAME = "VICS"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6217574784323026944
        self.SERIES_VERSION = 17

        #Define message fields
        self.x = 0   #real32
        self.y = 0   #real32


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">f", self.x))
        buffer.append(struct.pack(">f", self.y))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.x = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.y = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        return _pos


    def get_x(self):
        return self.x

    def set_x(self, value):
        self.x = float( value )

    def get_y(self):
        return self.y

    def set_y(self, value):
        self.y = float( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From LocationXY:\n"
        buf +=    "x = " + str( self.x ) + "\n" 
        buf +=    "y = " + str( self.y ) + "\n" 

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
        str = ws + "<LocationXY>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</LocationXY>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<x>" + str(self.x) + "</x>\n"
        buf += ws + "<y>" + str(self.y) + "</y>\n"

        return buf
        
