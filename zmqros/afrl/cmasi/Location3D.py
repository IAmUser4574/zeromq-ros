#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *
from cmasi import Location2D


class Location3D(Location2D.Location2D):

    def __init__(self):
        Location2D.Location2D.__init__(self)
        self.LMCP_TYPE = 21
        self.SERIES_NAME = "CMASI"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 4849604199710720000
        self.SERIES_VERSION = 2

        #Define message fields
        self.Altitude = 0   #real32


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(Location2D.Location2D.pack(self))
        buffer.append(struct.pack(">f", self.Altitude))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = Location2D.Location2D.unpack(self, buffer, _pos)
        self.Altitude = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        return _pos


    def get_Altitude(self):
        return self.Altitude

    def set_Altitude(self, value):
        self.Altitude = float( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = Location2D.Location2D.toString(self)
        buf += "From Location3D:\n"
        buf +=    "Altitude = " + str( self.Altitude ) + "\n" 

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
        str = ws + "<Location3D>\n";
        #str +=Location2D.Location2D.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</Location3D>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += Location2D.Location2D.toXMLMembersStr(self, ws)
        buf += ws + "<Altitude>" + str(self.Altitude) + "</Altitude>\n"

        return buf
        
