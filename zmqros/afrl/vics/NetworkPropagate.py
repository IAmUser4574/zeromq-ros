#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *
from vics import NetworkRegion


class NetworkPropagate(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 40
        self.SERIES_NAME = "VICS"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6217574784323026944
        self.SERIES_VERSION = 17

        #Define message fields
        self.InitialPDF = NetworkRegion.NetworkRegion()   #NetworkRegion
        self.TimeToPropagate = 0   #uint32


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack("B", self.InitialPDF != None ))
        if self.InitialPDF != None:
            buffer.append(struct.pack(">q", self.InitialPDF.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.InitialPDF.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.InitialPDF.SERIES_VERSION))
            buffer.append(self.InitialPDF.pack())
        buffer.append(struct.pack(">I", self.TimeToPropagate))

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
            self.InitialPDF = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.InitialPDF.unpack(buffer, _pos)
        else:
            self.InitialPDF = None
        self.TimeToPropagate = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        return _pos


    def get_InitialPDF(self):
        return self.InitialPDF

    def set_InitialPDF(self, value):
        self.InitialPDF = value 

    def get_TimeToPropagate(self):
        return self.TimeToPropagate

    def set_TimeToPropagate(self, value):
        self.TimeToPropagate = int( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From NetworkPropagate:\n"
        buf +=    "InitialPDF = " + str( self.InitialPDF ) + "\n" 
        buf +=    "TimeToPropagate = " + str( self.TimeToPropagate ) + "\n" 

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
        str = ws + "<NetworkPropagate>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</NetworkPropagate>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<InitialPDF>\n"
        if self.InitialPDF == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.InitialPDF.toXMLStr(ws + "    ") 
        buf += ws + "</InitialPDF>\n"
        buf += ws + "<TimeToPropagate>" + str(self.TimeToPropagate) + "</TimeToPropagate>\n"

        return buf
        
