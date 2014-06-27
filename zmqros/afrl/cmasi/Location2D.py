#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *


class Location2D(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 20
        self.SERIES_NAME = "CMASI"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 4849604199710720000
        self.SERIES_VERSION = 2

        #Define message fields
        self.Latitude = 0   #real64
        self.Longitude = 0   #real64


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">d", self.Latitude))
        buffer.append(struct.pack(">d", self.Longitude))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.Latitude = struct.unpack_from(">d", buffer, _pos)[0]
        _pos += 8
        self.Longitude = struct.unpack_from(">d", buffer, _pos)[0]
        _pos += 8
        return _pos


    def get_Latitude(self):
        return self.Latitude

    def set_Latitude(self, value):
        self.Latitude = float( value )

    def get_Longitude(self):
        return self.Longitude

    def set_Longitude(self, value):
        self.Longitude = float( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From Location2D:\n"
        buf +=    "Latitude = " + str( self.Latitude ) + "\n" 
        buf +=    "Longitude = " + str( self.Longitude ) + "\n" 

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
        str = ws + "<Location2D>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</Location2D>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<Latitude>" + str(self.Latitude) + "</Latitude>\n"
        buf += ws + "<Longitude>" + str(self.Longitude) + "</Longitude>\n"

        return buf
        
