#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *


class WifiConnectionStatus(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 54
        self.SERIES_NAME = "VICS"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6217574784323026944
        self.SERIES_VERSION = 17

        #Define message fields
        self.LinkTime = 0   #uint32
        self.UavId = 0   #uint32
        self.EntityId = 0   #uint32
        self.WifiLinkConnected = False   #bool


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">I", self.LinkTime))
        buffer.append(struct.pack(">I", self.UavId))
        buffer.append(struct.pack(">I", self.EntityId))
        buffer.append(struct.pack(">B", self.WifiLinkConnected))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.LinkTime = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        self.UavId = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        self.EntityId = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        self.WifiLinkConnected = struct.unpack_from(">B", buffer, _pos)[0]
        _pos += 1
        return _pos


    def get_LinkTime(self):
        return self.LinkTime

    def set_LinkTime(self, value):
        self.LinkTime = int( value )

    def get_UavId(self):
        return self.UavId

    def set_UavId(self, value):
        self.UavId = int( value )

    def get_EntityId(self):
        return self.EntityId

    def set_EntityId(self, value):
        self.EntityId = int( value )

    def get_WifiLinkConnected(self):
        return self.WifiLinkConnected

    def set_WifiLinkConnected(self, value):
        self.WifiLinkConnected = bool( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From WifiConnectionStatus:\n"
        buf +=    "LinkTime = " + str( self.LinkTime ) + "\n" 
        buf +=    "UavId = " + str( self.UavId ) + "\n" 
        buf +=    "EntityId = " + str( self.EntityId ) + "\n" 
        buf +=    "WifiLinkConnected = " + str( self.WifiLinkConnected ) + "\n" 

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
        str = ws + "<WifiConnectionStatus>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</WifiConnectionStatus>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<LinkTime>" + str(self.LinkTime) + "</LinkTime>\n"
        buf += ws + "<UavId>" + str(self.UavId) + "</UavId>\n"
        buf += ws + "<EntityId>" + str(self.EntityId) + "</EntityId>\n"
        buf += ws + "<WifiLinkConnected>" + str(self.WifiLinkConnected) + "</WifiLinkConnected>\n"

        return buf
        
