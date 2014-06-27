#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *


class LoiterVisitUgsCommand(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 49
        self.SERIES_NAME = "VICS"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6217574784323026944
        self.SERIES_VERSION = 17

        #Define message fields
        self.LoiterTime = 0   #real32
        self.UgsId = 0   #uint32


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">f", self.LoiterTime))
        buffer.append(struct.pack(">I", self.UgsId))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.LoiterTime = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.UgsId = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        return _pos


    def get_LoiterTime(self):
        return self.LoiterTime

    def set_LoiterTime(self, value):
        self.LoiterTime = float( value )

    def get_UgsId(self):
        return self.UgsId

    def set_UgsId(self, value):
        self.UgsId = int( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From LoiterVisitUgsCommand:\n"
        buf +=    "LoiterTime = " + str( self.LoiterTime ) + "\n" 
        buf +=    "UgsId = " + str( self.UgsId ) + "\n" 

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
        str = ws + "<LoiterVisitUgsCommand>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</LoiterVisitUgsCommand>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<LoiterTime>" + str(self.LoiterTime) + "</LoiterTime>\n"
        buf += ws + "<UgsId>" + str(self.UgsId) + "</UgsId>\n"

        return buf
        
