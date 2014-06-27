#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *
from vics import PayloadType


class PayloadData(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 22
        self.SERIES_NAME = "VICS"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6217574784323026944
        self.SERIES_VERSION = 17

        #Define message fields
        self.Data = []   #byte
        self.PayloadType = PayloadType.PayloadType.NoPayload   #PayloadType
        self.ExpectedPayloadSize = 0   #uint32


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">I", len(self.Data) ))
        for x in self.Data:
            buffer.append(struct.pack(">B", x ))
        buffer.append(struct.pack(">i", self.PayloadType))
        buffer.append(struct.pack(">I", self.ExpectedPayloadSize))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        _arraylen = struct.unpack_from(">I", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.Data = [None] * _arraylen
        _pos += 2
        if _arraylen > 0:
            self.Data = struct.unpack_from(">" + `_arraylen` + "B", buffer, _pos )
            _pos += 1 * _arraylen
        self.PayloadType = struct.unpack_from(">i", buffer, _pos)[0]
        _pos += 4
        self.ExpectedPayloadSize = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        return _pos


    def get_Data(self):
        return self.Data

    def get_PayloadType(self):
        return self.PayloadType

    def set_PayloadType(self, value):
        self.PayloadType = value 

    def get_ExpectedPayloadSize(self):
        return self.ExpectedPayloadSize

    def set_ExpectedPayloadSize(self, value):
        self.ExpectedPayloadSize = int( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From PayloadData:\n"
        buf +=    "Data = " + str( self.Data ) + "\n" 
        buf +=    "PayloadType = " + str( self.PayloadType ) + "\n" 
        buf +=    "ExpectedPayloadSize = " + str( self.ExpectedPayloadSize ) + "\n" 

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
        str = ws + "<PayloadData>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</PayloadData>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<Data>\n"
        for x in self.Data:
            buf += ws + "<byte>" + str(x) + "</byte>\n"
        buf += ws + "</Data>\n"
        buf += ws + "<PayloadType>" + PayloadType.get_PayloadType_int(self.PayloadType) + "</PayloadType>\n"
        buf += ws + "<ExpectedPayloadSize>" + str(self.ExpectedPayloadSize) + "</ExpectedPayloadSize>\n"

        return buf
        
