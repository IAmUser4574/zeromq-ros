#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *


class VicsAck(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 2
        self.SERIES_NAME = "VICS"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6217574784323026944
        self.SERIES_VERSION = 17

        #Define message fields
        self.ReceivedMessageId = 0   #uint32
        self.ReceivedOriginatorId = 0   #uint32
        self.ReceivedNumberOfBytes = 0   #uint32


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">I", self.ReceivedMessageId))
        buffer.append(struct.pack(">I", self.ReceivedOriginatorId))
        buffer.append(struct.pack(">I", self.ReceivedNumberOfBytes))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.ReceivedMessageId = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        self.ReceivedOriginatorId = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        self.ReceivedNumberOfBytes = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        return _pos


    def get_ReceivedMessageId(self):
        return self.ReceivedMessageId

    def set_ReceivedMessageId(self, value):
        self.ReceivedMessageId = int( value )

    def get_ReceivedOriginatorId(self):
        return self.ReceivedOriginatorId

    def set_ReceivedOriginatorId(self, value):
        self.ReceivedOriginatorId = int( value )

    def get_ReceivedNumberOfBytes(self):
        return self.ReceivedNumberOfBytes

    def set_ReceivedNumberOfBytes(self, value):
        self.ReceivedNumberOfBytes = int( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From VicsAck:\n"
        buf +=    "ReceivedMessageId = " + str( self.ReceivedMessageId ) + "\n" 
        buf +=    "ReceivedOriginatorId = " + str( self.ReceivedOriginatorId ) + "\n" 
        buf +=    "ReceivedNumberOfBytes = " + str( self.ReceivedNumberOfBytes ) + "\n" 

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
        str = ws + "<VicsAck>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</VicsAck>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<ReceivedMessageId>" + str(self.ReceivedMessageId) + "</ReceivedMessageId>\n"
        buf += ws + "<ReceivedOriginatorId>" + str(self.ReceivedOriginatorId) + "</ReceivedOriginatorId>\n"
        buf += ws + "<ReceivedNumberOfBytes>" + str(self.ReceivedNumberOfBytes) + "</ReceivedNumberOfBytes>\n"

        return buf
        
