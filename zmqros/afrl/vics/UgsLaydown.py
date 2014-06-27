#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *
from vics import NetworkRegion
from vics import FixedUGS
from cmasi import Location3D


class UgsLaydown(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 46
        self.SERIES_NAME = "VICS"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6217574784323026944
        self.SERIES_VERSION = 17

        #Define message fields
        self.RoadNetwork = NetworkRegion.NetworkRegion()   #NetworkRegion
        self.UgsList = []   #FixedUGS
        self.DeliveryLocation = Location3D.Location3D()   #Location3D


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack("B", self.RoadNetwork != None ))
        if self.RoadNetwork != None:
            buffer.append(struct.pack(">q", self.RoadNetwork.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.RoadNetwork.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.RoadNetwork.SERIES_VERSION))
            buffer.append(self.RoadNetwork.pack())
        buffer.append(struct.pack(">H", len(self.UgsList) ))
        for x in self.UgsList:
           buffer.append(struct.pack("B", x != None ))
           if x != None:
               buffer.append(struct.pack(">q", x.SERIES_NAME_ID))
               buffer.append(struct.pack(">I", x.LMCP_TYPE))
               buffer.append(struct.pack(">H", x.SERIES_VERSION))
               buffer.append(x.pack())
        buffer.append(struct.pack("B", self.DeliveryLocation != None ))
        if self.DeliveryLocation != None:
            buffer.append(struct.pack(">q", self.DeliveryLocation.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.DeliveryLocation.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.DeliveryLocation.SERIES_VERSION))
            buffer.append(self.DeliveryLocation.pack())

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
            self.RoadNetwork = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.RoadNetwork.unpack(buffer, _pos)
        else:
            self.RoadNetwork = None
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.UgsList = [None] * _arraylen
        _pos += 2
        for x in range(_arraylen):
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
                self.UgsList[x] = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
                _pos = self.UgsList[x].unpack(buffer, _pos)
            else:
                self.UgsList[x] = None
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
            self.DeliveryLocation = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.DeliveryLocation.unpack(buffer, _pos)
        else:
            self.DeliveryLocation = None
        return _pos


    def get_RoadNetwork(self):
        return self.RoadNetwork

    def set_RoadNetwork(self, value):
        self.RoadNetwork = value 

    def get_UgsList(self):
        return self.UgsList

    def get_DeliveryLocation(self):
        return self.DeliveryLocation

    def set_DeliveryLocation(self, value):
        self.DeliveryLocation = value 



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From UgsLaydown:\n"
        buf +=    "RoadNetwork = " + str( self.RoadNetwork ) + "\n" 
        buf +=    "UgsList = " + str( self.UgsList ) + "\n" 
        buf +=    "DeliveryLocation = " + str( self.DeliveryLocation ) + "\n" 

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
        str = ws + "<UgsLaydown>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</UgsLaydown>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<RoadNetwork>\n"
        if self.RoadNetwork == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.RoadNetwork.toXMLStr(ws + "    ") 
        buf += ws + "</RoadNetwork>\n"
        buf += ws + "<UgsList>\n"
        for x in self.UgsList:
            if x == None:
                buf += ws + "    <null/>\n"
            else:
                buf += x.toXMLStr(ws + "    ") 
        buf += ws + "</UgsList>\n"
        buf += ws + "<DeliveryLocation>\n"
        if self.DeliveryLocation == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.DeliveryLocation.toXMLStr(ws + "    ") 
        buf += ws + "</DeliveryLocation>\n"

        return buf
        
