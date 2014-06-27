#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *


class RadarEnableMessage(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 19
        self.SERIES_NAME = "VICS"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6217574784323026944
        self.SERIES_VERSION = 17

        #Define message fields
        self.EnableRadar = True   #bool
        self.TimeOut = 0   #real32


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">B", self.EnableRadar))
        buffer.append(struct.pack(">f", self.TimeOut))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.EnableRadar = struct.unpack_from(">B", buffer, _pos)[0]
        _pos += 1
        self.TimeOut = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        return _pos


    def get_EnableRadar(self):
        return self.EnableRadar

    def set_EnableRadar(self, value):
        self.EnableRadar = bool( value )

    def get_TimeOut(self):
        return self.TimeOut

    def set_TimeOut(self, value):
        self.TimeOut = float( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From RadarEnableMessage:\n"
        buf +=    "EnableRadar = " + str( self.EnableRadar ) + "\n" 
        buf +=    "TimeOut = " + str( self.TimeOut ) + "\n" 

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
        str = ws + "<RadarEnableMessage>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</RadarEnableMessage>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<EnableRadar>" + str(self.EnableRadar) + "</EnableRadar>\n"
        buf += ws + "<TimeOut>" + str(self.TimeOut) + "</TimeOut>\n"

        return buf
        
