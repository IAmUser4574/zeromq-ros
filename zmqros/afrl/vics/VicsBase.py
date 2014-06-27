#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *
from vics import VicsEntityType
from vics import MessagePriority


class VicsBase(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 1
        self.SERIES_NAME = "VICS"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6217574784323026944
        self.SERIES_VERSION = 17

        #Define message fields
        self.MessageId = 0   #uint32
        self.OriginatorId = 0   #uint32
        self.SenderId = 0   #uint32
        self.GroupId = 0   #uint32
        self.OriginatorType = VicsEntityType.VicsEntityType.Unknown   #VicsEntityType
        self.TimeStamp = 0   #uint32
        self.Priority = MessagePriority.MessagePriority.Normal   #MessagePriority


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">I", self.MessageId))
        buffer.append(struct.pack(">I", self.OriginatorId))
        buffer.append(struct.pack(">I", self.SenderId))
        buffer.append(struct.pack(">I", self.GroupId))
        buffer.append(struct.pack(">i", self.OriginatorType))
        buffer.append(struct.pack(">I", self.TimeStamp))
        buffer.append(struct.pack(">i", self.Priority))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.MessageId = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        self.OriginatorId = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        self.SenderId = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        self.GroupId = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        self.OriginatorType = struct.unpack_from(">i", buffer, _pos)[0]
        _pos += 4
        self.TimeStamp = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        self.Priority = struct.unpack_from(">i", buffer, _pos)[0]
        _pos += 4
        return _pos


    def get_MessageId(self):
        return self.MessageId

    def set_MessageId(self, value):
        self.MessageId = int( value )

    def get_OriginatorId(self):
        return self.OriginatorId

    def set_OriginatorId(self, value):
        self.OriginatorId = int( value )

    def get_SenderId(self):
        return self.SenderId

    def set_SenderId(self, value):
        self.SenderId = int( value )

    def get_GroupId(self):
        return self.GroupId

    def set_GroupId(self, value):
        self.GroupId = int( value )

    def get_OriginatorType(self):
        return self.OriginatorType

    def set_OriginatorType(self, value):
        self.OriginatorType = value 

    def get_TimeStamp(self):
        return self.TimeStamp

    def set_TimeStamp(self, value):
        self.TimeStamp = int( value )

    def get_Priority(self):
        return self.Priority

    def set_Priority(self, value):
        self.Priority = value 



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From VicsBase:\n"
        buf +=    "MessageId = " + str( self.MessageId ) + "\n" 
        buf +=    "OriginatorId = " + str( self.OriginatorId ) + "\n" 
        buf +=    "SenderId = " + str( self.SenderId ) + "\n" 
        buf +=    "GroupId = " + str( self.GroupId ) + "\n" 
        buf +=    "OriginatorType = " + str( self.OriginatorType ) + "\n" 
        buf +=    "TimeStamp = " + str( self.TimeStamp ) + "\n" 
        buf +=    "Priority = " + str( self.Priority ) + "\n" 

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
        str = ws + "<VicsBase>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</VicsBase>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<MessageId>" + str(self.MessageId) + "</MessageId>\n"
        buf += ws + "<OriginatorId>" + str(self.OriginatorId) + "</OriginatorId>\n"
        buf += ws + "<SenderId>" + str(self.SenderId) + "</SenderId>\n"
        buf += ws + "<GroupId>" + str(self.GroupId) + "</GroupId>\n"
        buf += ws + "<OriginatorType>" + VicsEntityType.get_VicsEntityType_int(self.OriginatorType) + "</OriginatorType>\n"
        buf += ws + "<TimeStamp>" + str(self.TimeStamp) + "</TimeStamp>\n"
        buf += ws + "<Priority>" + MessagePriority.get_MessagePriority_int(self.Priority) + "</Priority>\n"

        return buf
        
