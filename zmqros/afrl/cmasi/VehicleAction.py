#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *


class VehicleAction(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 39
        self.SERIES_NAME = "CMASI"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 4849604199710720000
        self.SERIES_VERSION = 2

        #Define message fields
        self.AssociatedTaskList = []   #uint32


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">H", len(self.AssociatedTaskList) ))
        for x in self.AssociatedTaskList:
            buffer.append(struct.pack(">I", x ))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.AssociatedTaskList = [None] * _arraylen
        _pos += 2
        if _arraylen > 0:
            self.AssociatedTaskList = struct.unpack_from(">" + `_arraylen` + "I", buffer, _pos )
            _pos += 4 * _arraylen
        return _pos


    def get_AssociatedTaskList(self):
        return self.AssociatedTaskList



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From VehicleAction:\n"
        buf +=    "AssociatedTaskList = " + str( self.AssociatedTaskList ) + "\n" 

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
        str = ws + "<VehicleAction>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</VehicleAction>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<AssociatedTaskList>\n"
        for x in self.AssociatedTaskList:
            buf += ws + "<uint32>" + str(x) + "</uint32>\n"
        buf += ws + "</AssociatedTaskList>\n"

        return buf
        
