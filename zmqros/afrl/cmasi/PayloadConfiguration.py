#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *


class PayloadConfiguration(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 28
        self.SERIES_NAME = "CMASI"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 4849604199710720000
        self.SERIES_VERSION = 2

        #Define message fields
        self.PayloadID = 0   #uint32
        self.PayloadKind = ""   #string


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">I", self.PayloadID))
        buffer.append(struct.pack(">H", len(self.PayloadKind) ))
        if len(self.PayloadKind) > 0:
            buffer.append(struct.pack( `len(self.PayloadKind)` + "s", self.PayloadKind))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.PayloadID = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        _strlen = struct.unpack_from(">H", buffer, _pos )[0]
        _pos += 2
        if _strlen > 0:
            self.PayloadKind = struct.unpack_from( `_strlen` + "s", buffer, _pos )[0]
            _pos += _strlen
        else:
             self.PayloadKind = ""
        return _pos


    def get_PayloadID(self):
        return self.PayloadID

    def set_PayloadID(self, value):
        self.PayloadID = int( value )

    def get_PayloadKind(self):
        return self.PayloadKind

    def set_PayloadKind(self, value):
        self.PayloadKind = str( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From PayloadConfiguration:\n"
        buf +=    "PayloadID = " + str( self.PayloadID ) + "\n" 
        buf +=    "PayloadKind = " + str( self.PayloadKind ) + "\n" 

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
        str = ws + "<PayloadConfiguration>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</PayloadConfiguration>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<PayloadID>" + str(self.PayloadID) + "</PayloadID>\n"
        buf += ws + "<PayloadKind>" + str(self.PayloadKind) + "</PayloadKind>\n"

        return buf
        
