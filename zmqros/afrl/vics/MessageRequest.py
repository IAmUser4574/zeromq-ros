#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *
from vics import MessageType


class MessageRequest(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 26
        self.SERIES_NAME = "VICS"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6217574784323026944
        self.SERIES_VERSION = 17

        #Define message fields
        self.RequestType = MessageType.MessageType.DismountMessage   #MessageType
        self.StartTime = 0   #uint32
        self.EndTime = 0   #uint32
        self.OriginatorId = 0   #uint32
        self.MessageId = 0   #uint32


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">i", self.RequestType))
        buffer.append(struct.pack(">I", self.StartTime))
        buffer.append(struct.pack(">I", self.EndTime))
        buffer.append(struct.pack(">I", self.OriginatorId))
        buffer.append(struct.pack(">I", self.MessageId))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.RequestType = struct.unpack_from(">i", buffer, _pos)[0]
        _pos += 4
        self.StartTime = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        self.EndTime = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        self.OriginatorId = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        self.MessageId = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        return _pos


    def get_RequestType(self):
        return self.RequestType

    def set_RequestType(self, value):
        self.RequestType = value 

    def get_StartTime(self):
        return self.StartTime

    def set_StartTime(self, value):
        self.StartTime = int( value )

    def get_EndTime(self):
        return self.EndTime

    def set_EndTime(self, value):
        self.EndTime = int( value )

    def get_OriginatorId(self):
        return self.OriginatorId

    def set_OriginatorId(self, value):
        self.OriginatorId = int( value )

    def get_MessageId(self):
        return self.MessageId

    def set_MessageId(self, value):
        self.MessageId = int( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From MessageRequest:\n"
        buf +=    "RequestType = " + str( self.RequestType ) + "\n" 
        buf +=    "StartTime = " + str( self.StartTime ) + "\n" 
        buf +=    "EndTime = " + str( self.EndTime ) + "\n" 
        buf +=    "OriginatorId = " + str( self.OriginatorId ) + "\n" 
        buf +=    "MessageId = " + str( self.MessageId ) + "\n" 

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
        str = ws + "<MessageRequest>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</MessageRequest>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<RequestType>" + MessageType.get_MessageType_int(self.RequestType) + "</RequestType>\n"
        buf += ws + "<StartTime>" + str(self.StartTime) + "</StartTime>\n"
        buf += ws + "<EndTime>" + str(self.EndTime) + "</EndTime>\n"
        buf += ws + "<OriginatorId>" + str(self.OriginatorId) + "</OriginatorId>\n"
        buf += ws + "<MessageId>" + str(self.MessageId) + "</MessageId>\n"

        return buf
        
