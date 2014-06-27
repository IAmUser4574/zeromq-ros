#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *
from vics import VicsBase
from cmasi import Location3D


class HeartbeatMessage(VicsBase.VicsBase):

    def __init__(self):
        VicsBase.VicsBase.__init__(self)
        self.LMCP_TYPE = 20
        self.SERIES_NAME = "VICS"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6217574784323026944
        self.SERIES_VERSION = 17

        #Define message fields
        self.ServerIpAddress = ""   #string
        self.ServerPortNumber = 0   #uint32
        self.Location = Location3D.Location3D()   #Location3D


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(VicsBase.VicsBase.pack(self))
        buffer.append(struct.pack(">H", len(self.ServerIpAddress) ))
        if len(self.ServerIpAddress) > 0:
            buffer.append(struct.pack( `len(self.ServerIpAddress)` + "s", self.ServerIpAddress))
        buffer.append(struct.pack(">I", self.ServerPortNumber))
        buffer.append(struct.pack("B", self.Location != None ))
        if self.Location != None:
            buffer.append(struct.pack(">q", self.Location.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.Location.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.Location.SERIES_VERSION))
            buffer.append(self.Location.pack())

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = VicsBase.VicsBase.unpack(self, buffer, _pos)
        _strlen = struct.unpack_from(">H", buffer, _pos )[0]
        _pos += 2
        if _strlen > 0:
            self.ServerIpAddress = struct.unpack_from( `_strlen` + "s", buffer, _pos )[0]
            _pos += _strlen
        else:
             self.ServerIpAddress = ""
        self.ServerPortNumber = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
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
            self.Location = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.Location.unpack(buffer, _pos)
        else:
            self.Location = None
        return _pos


    def get_ServerIpAddress(self):
        return self.ServerIpAddress

    def set_ServerIpAddress(self, value):
        self.ServerIpAddress = str( value )

    def get_ServerPortNumber(self):
        return self.ServerPortNumber

    def set_ServerPortNumber(self, value):
        self.ServerPortNumber = int( value )

    def get_Location(self):
        return self.Location

    def set_Location(self, value):
        self.Location = value 



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = VicsBase.VicsBase.toString(self)
        buf += "From HeartbeatMessage:\n"
        buf +=    "ServerIpAddress = " + str( self.ServerIpAddress ) + "\n" 
        buf +=    "ServerPortNumber = " + str( self.ServerPortNumber ) + "\n" 
        buf +=    "Location = " + str( self.Location ) + "\n" 

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
        str = ws + "<HeartbeatMessage>\n";
        #str +=VicsBase.VicsBase.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</HeartbeatMessage>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += VicsBase.VicsBase.toXMLMembersStr(self, ws)
        buf += ws + "<ServerIpAddress>" + str(self.ServerIpAddress) + "</ServerIpAddress>\n"
        buf += ws + "<ServerPortNumber>" + str(self.ServerPortNumber) + "</ServerPortNumber>\n"
        buf += ws + "<Location>\n"
        if self.Location == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.Location.toXMLStr(ws + "    ") 
        buf += ws + "</Location>\n"

        return buf
        
