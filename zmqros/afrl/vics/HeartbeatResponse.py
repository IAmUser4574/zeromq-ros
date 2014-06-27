#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *
from vics import VicsBase


class HeartbeatResponse(VicsBase.VicsBase):

    def __init__(self):
        VicsBase.VicsBase.__init__(self)
        self.LMCP_TYPE = 21
        self.SERIES_NAME = "VICS"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6217574784323026944
        self.SERIES_VERSION = 17

        #Define message fields
        self.ClientIpAddress = ""   #string


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(VicsBase.VicsBase.pack(self))
        buffer.append(struct.pack(">H", len(self.ClientIpAddress) ))
        if len(self.ClientIpAddress) > 0:
            buffer.append(struct.pack( `len(self.ClientIpAddress)` + "s", self.ClientIpAddress))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = VicsBase.VicsBase.unpack(self, buffer, _pos)
        _strlen = struct.unpack_from(">H", buffer, _pos )[0]
        _pos += 2
        if _strlen > 0:
            self.ClientIpAddress = struct.unpack_from( `_strlen` + "s", buffer, _pos )[0]
            _pos += _strlen
        else:
             self.ClientIpAddress = ""
        return _pos


    def get_ClientIpAddress(self):
        return self.ClientIpAddress

    def set_ClientIpAddress(self, value):
        self.ClientIpAddress = str( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = VicsBase.VicsBase.toString(self)
        buf += "From HeartbeatResponse:\n"
        buf +=    "ClientIpAddress = " + str( self.ClientIpAddress ) + "\n" 

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
        str = ws + "<HeartbeatResponse>\n";
        #str +=VicsBase.VicsBase.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</HeartbeatResponse>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += VicsBase.VicsBase.toXMLMembersStr(self, ws)
        buf += ws + "<ClientIpAddress>" + str(self.ClientIpAddress) + "</ClientIpAddress>\n"

        return buf
        
