#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *
from vics import UgsLaydown


class IsolationControllerInitialization(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 47
        self.SERIES_NAME = "VICS"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6217574784323026944
        self.SERIES_VERSION = 17

        #Define message fields
        self.UgsPlacement = UgsLaydown.UgsLaydown()   #UgsLaydown
        self.IntruderSpeed = 0   #real32


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack("B", self.UgsPlacement != None ))
        if self.UgsPlacement != None:
            buffer.append(struct.pack(">q", self.UgsPlacement.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.UgsPlacement.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.UgsPlacement.SERIES_VERSION))
            buffer.append(self.UgsPlacement.pack())
        buffer.append(struct.pack(">f", self.IntruderSpeed))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        _valid = struct.unpack_from("B", buffer, _pos )[0]
        _pos += 1
        if _valid:
            _series = struct.unpack_from(">q", buffer, _pos)[0]
            _pos += 8
            _type = struct.unpack_from(">I", buffer, _pos)[0]
            _pos += 4
            _version = struct.unpack_from(">H", buffer, _pos)[0]
            _pos += 2
            from lmcp import LMCPFactory
            self.UgsPlacement = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.UgsPlacement.unpack(buffer, _pos)
        else:
            self.UgsPlacement = None
        self.IntruderSpeed = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        return _pos


    def get_UgsPlacement(self):
        return self.UgsPlacement

    def set_UgsPlacement(self, value):
        self.UgsPlacement = value 

    def get_IntruderSpeed(self):
        return self.IntruderSpeed

    def set_IntruderSpeed(self, value):
        self.IntruderSpeed = float( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From IsolationControllerInitialization:\n"
        buf +=    "UgsPlacement = " + str( self.UgsPlacement ) + "\n" 
        buf +=    "IntruderSpeed = " + str( self.IntruderSpeed ) + "\n" 

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
        str = ws + "<IsolationControllerInitialization>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</IsolationControllerInitialization>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<UgsPlacement>\n"
        if self.UgsPlacement == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.UgsPlacement.toXMLStr(ws + "    ") 
        buf += ws + "</UgsPlacement>\n"
        buf += ws + "<IntruderSpeed>" + str(self.IntruderSpeed) + "</IntruderSpeed>\n"

        return buf
        
