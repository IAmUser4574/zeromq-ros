#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *
from cmasi import Task
from vics import UgsLaydown


class UgsManagementTask(Task.Task):

    def __init__(self):
        Task.Task.__init__(self)
        self.LMCP_TYPE = 7
        self.SERIES_NAME = "VICS"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6217574784323026944
        self.SERIES_VERSION = 17

        #Define message fields
        self.UgsPlacement = UgsLaydown.UgsLaydown()   #UgsLaydown
        self.UavId = []   #uint32


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(Task.Task.pack(self))
        buffer.append(struct.pack("B", self.UgsPlacement != None ))
        if self.UgsPlacement != None:
            buffer.append(struct.pack(">q", self.UgsPlacement.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.UgsPlacement.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.UgsPlacement.SERIES_VERSION))
            buffer.append(self.UgsPlacement.pack())
        buffer.append(struct.pack(">H", len(self.UavId) ))
        for x in self.UavId:
            buffer.append(struct.pack(">I", x ))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = Task.Task.unpack(self, buffer, _pos)
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
            self.UgsPlacement = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.UgsPlacement.unpack(buffer, _pos)
        else:
            self.UgsPlacement = None
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.UavId = [None] * _arraylen
        _pos += 2
        if _arraylen > 0:
            self.UavId = struct.unpack_from(">" + `_arraylen` + "I", buffer, _pos )
            _pos += 4 * _arraylen
        return _pos


    def get_UgsPlacement(self):
        return self.UgsPlacement

    def set_UgsPlacement(self, value):
        self.UgsPlacement = value 

    def get_UavId(self):
        return self.UavId



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = Task.Task.toString(self)
        buf += "From UgsManagementTask:\n"
        buf +=    "UgsPlacement = " + str( self.UgsPlacement ) + "\n" 
        buf +=    "UavId = " + str( self.UavId ) + "\n" 

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
        str = ws + "<UgsManagementTask>\n";
        #str +=Task.Task.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</UgsManagementTask>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += Task.Task.toXMLMembersStr(self, ws)
        buf += ws + "<UgsPlacement>\n"
        if self.UgsPlacement == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.UgsPlacement.toXMLStr(ws + "    ") 
        buf += ws + "</UgsPlacement>\n"
        buf += ws + "<UavId>\n"
        for x in self.UavId:
            buf += ws + "<uint32>" + str(x) + "</uint32>\n"
        buf += ws + "</UavId>\n"

        return buf
        
