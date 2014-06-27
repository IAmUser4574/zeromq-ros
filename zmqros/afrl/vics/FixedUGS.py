#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *
from cmasi import Location3D
from vics import NetworkLocation


class FixedUGS(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 45
        self.SERIES_NAME = "VICS"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6217574784323026944
        self.SERIES_VERSION = 17

        #Define message fields
        self.UgsId = 0   #uint32
        self.UgsLocation = Location3D.Location3D()   #Location3D
        self.UgsNetworkLocation = NetworkLocation.NetworkLocation()   #NetworkLocation


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">I", self.UgsId))
        buffer.append(struct.pack("B", self.UgsLocation != None ))
        if self.UgsLocation != None:
            buffer.append(struct.pack(">q", self.UgsLocation.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.UgsLocation.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.UgsLocation.SERIES_VERSION))
            buffer.append(self.UgsLocation.pack())
        buffer.append(struct.pack("B", self.UgsNetworkLocation != None ))
        if self.UgsNetworkLocation != None:
            buffer.append(struct.pack(">q", self.UgsNetworkLocation.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.UgsNetworkLocation.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.UgsNetworkLocation.SERIES_VERSION))
            buffer.append(self.UgsNetworkLocation.pack())

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.UgsId = struct.unpack_from(">I", buffer, _pos)[0]
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
            self.UgsLocation = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.UgsLocation.unpack(buffer, _pos)
        else:
            self.UgsLocation = None
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
            self.UgsNetworkLocation = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.UgsNetworkLocation.unpack(buffer, _pos)
        else:
            self.UgsNetworkLocation = None
        return _pos


    def get_UgsId(self):
        return self.UgsId

    def set_UgsId(self, value):
        self.UgsId = int( value )

    def get_UgsLocation(self):
        return self.UgsLocation

    def set_UgsLocation(self, value):
        self.UgsLocation = value 

    def get_UgsNetworkLocation(self):
        return self.UgsNetworkLocation

    def set_UgsNetworkLocation(self, value):
        self.UgsNetworkLocation = value 



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From FixedUGS:\n"
        buf +=    "UgsId = " + str( self.UgsId ) + "\n" 
        buf +=    "UgsLocation = " + str( self.UgsLocation ) + "\n" 
        buf +=    "UgsNetworkLocation = " + str( self.UgsNetworkLocation ) + "\n" 

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
        str = ws + "<FixedUGS>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</FixedUGS>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<UgsId>" + str(self.UgsId) + "</UgsId>\n"
        buf += ws + "<UgsLocation>\n"
        if self.UgsLocation == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.UgsLocation.toXMLStr(ws + "    ") 
        buf += ws + "</UgsLocation>\n"
        buf += ws + "<UgsNetworkLocation>\n"
        if self.UgsNetworkLocation == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.UgsNetworkLocation.toXMLStr(ws + "    ") 
        buf += ws + "</UgsNetworkLocation>\n"

        return buf
        
