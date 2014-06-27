#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *
from vics import UgsReport


class NetworkUpdate(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 41
        self.SERIES_NAME = "VICS"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6217574784323026944
        self.SERIES_VERSION = 17

        #Define message fields
        self.RedMeasurement = UgsReport.UgsReport()   #UgsReport
        self.GreenMeasurements = []   #UgsReport


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack("B", self.RedMeasurement != None ))
        if self.RedMeasurement != None:
            buffer.append(struct.pack(">q", self.RedMeasurement.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.RedMeasurement.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.RedMeasurement.SERIES_VERSION))
            buffer.append(self.RedMeasurement.pack())
        buffer.append(struct.pack(">H", len(self.GreenMeasurements) ))
        for x in self.GreenMeasurements:
           buffer.append(struct.pack("B", x != None ))
           if x != None:
               buffer.append(struct.pack(">q", x.SERIES_NAME_ID))
               buffer.append(struct.pack(">I", x.LMCP_TYPE))
               buffer.append(struct.pack(">H", x.SERIES_VERSION))
               buffer.append(x.pack())

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
            self.RedMeasurement = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.RedMeasurement.unpack(buffer, _pos)
        else:
            self.RedMeasurement = None
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.GreenMeasurements = [None] * _arraylen
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
                self.GreenMeasurements[x] = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
                _pos = self.GreenMeasurements[x].unpack(buffer, _pos)
            else:
                self.GreenMeasurements[x] = None
        return _pos


    def get_RedMeasurement(self):
        return self.RedMeasurement

    def set_RedMeasurement(self, value):
        self.RedMeasurement = value 

    def get_GreenMeasurements(self):
        return self.GreenMeasurements



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From NetworkUpdate:\n"
        buf +=    "RedMeasurement = " + str( self.RedMeasurement ) + "\n" 
        buf +=    "GreenMeasurements = " + str( self.GreenMeasurements ) + "\n" 

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
        str = ws + "<NetworkUpdate>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</NetworkUpdate>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<RedMeasurement>\n"
        if self.RedMeasurement == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.RedMeasurement.toXMLStr(ws + "    ") 
        buf += ws + "</RedMeasurement>\n"
        buf += ws + "<GreenMeasurements>\n"
        for x in self.GreenMeasurements:
            if x == None:
                buf += ws + "    <null/>\n"
            else:
                buf += x.toXMLStr(ws + "    ") 
        buf += ws + "</GreenMeasurements>\n"

        return buf
        
