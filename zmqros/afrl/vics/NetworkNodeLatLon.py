#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *
from vics import NetworkNode
from cmasi import Location3D


class NetworkNodeLatLon(NetworkNode.NetworkNode):

    def __init__(self):
        NetworkNode.NetworkNode.__init__(self)
        self.LMCP_TYPE = 31
        self.SERIES_NAME = "VICS"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6217574784323026944
        self.SERIES_VERSION = 17

        #Define message fields
        self.Coordinates = Location3D.Location3D()   #Location3D


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(NetworkNode.NetworkNode.pack(self))
        buffer.append(struct.pack("B", self.Coordinates != None ))
        if self.Coordinates != None:
            buffer.append(struct.pack(">q", self.Coordinates.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.Coordinates.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.Coordinates.SERIES_VERSION))
            buffer.append(self.Coordinates.pack())

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = NetworkNode.NetworkNode.unpack(self, buffer, _pos)
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
            self.Coordinates = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.Coordinates.unpack(buffer, _pos)
        else:
            self.Coordinates = None
        return _pos


    def get_Coordinates(self):
        return self.Coordinates

    def set_Coordinates(self, value):
        self.Coordinates = value 



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = NetworkNode.NetworkNode.toString(self)
        buf += "From NetworkNodeLatLon:\n"
        buf +=    "Coordinates = " + str( self.Coordinates ) + "\n" 

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
        str = ws + "<NetworkNodeLatLon>\n";
        #str +=NetworkNode.NetworkNode.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</NetworkNodeLatLon>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += NetworkNode.NetworkNode.toXMLMembersStr(self, ws)
        buf += ws + "<Coordinates>\n"
        if self.Coordinates == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.Coordinates.toXMLStr(ws + "    ") 
        buf += ws + "</Coordinates>\n"

        return buf
        
