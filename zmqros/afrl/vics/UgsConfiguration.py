#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *


class UgsConfiguration(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 16
        self.SERIES_NAME = "VICS"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6217574784323026944
        self.SERIES_VERSION = 17

        #Define message fields
        self.UgsId = 0   #uint32
        self.DefaultRadarEnable = True   #bool
        self.HeadingAngle = 0   #real32


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">I", self.UgsId))
        buffer.append(struct.pack(">B", self.DefaultRadarEnable))
        buffer.append(struct.pack(">f", self.HeadingAngle))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.UgsId = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        self.DefaultRadarEnable = struct.unpack_from(">B", buffer, _pos)[0]
        _pos += 1
        self.HeadingAngle = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        return _pos


    def get_UgsId(self):
        return self.UgsId

    def set_UgsId(self, value):
        self.UgsId = int( value )

    def get_DefaultRadarEnable(self):
        return self.DefaultRadarEnable

    def set_DefaultRadarEnable(self, value):
        self.DefaultRadarEnable = bool( value )

    def get_HeadingAngle(self):
        return self.HeadingAngle

    def set_HeadingAngle(self, value):
        self.HeadingAngle = float( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From UgsConfiguration:\n"
        buf +=    "UgsId = " + str( self.UgsId ) + "\n" 
        buf +=    "DefaultRadarEnable = " + str( self.DefaultRadarEnable ) + "\n" 
        buf +=    "HeadingAngle = " + str( self.HeadingAngle ) + "\n" 

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
        str = ws + "<UgsConfiguration>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</UgsConfiguration>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<UgsId>" + str(self.UgsId) + "</UgsId>\n"
        buf += ws + "<DefaultRadarEnable>" + str(self.DefaultRadarEnable) + "</DefaultRadarEnable>\n"
        buf += ws + "<HeadingAngle>" + str(self.HeadingAngle) + "</HeadingAngle>\n"

        return buf
        
