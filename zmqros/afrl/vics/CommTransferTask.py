#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *
from cmasi import Task
from cmasi import Location3D


class CommTransferTask(Task.Task):

    def __init__(self):
        Task.Task.__init__(self)
        self.LMCP_TYPE = 5
        self.SERIES_NAME = "VICS"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6217574784323026944
        self.SERIES_VERSION = 17

        #Define message fields
        self.CommLocation = Location3D.Location3D()   #Location3D
        self.Timeout = 0   #uint32


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(Task.Task.pack(self))
        buffer.append(struct.pack("B", self.CommLocation != None ))
        if self.CommLocation != None:
            buffer.append(struct.pack(">q", self.CommLocation.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.CommLocation.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.CommLocation.SERIES_VERSION))
            buffer.append(self.CommLocation.pack())
        buffer.append(struct.pack(">I", self.Timeout))

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
            self.CommLocation = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.CommLocation.unpack(buffer, _pos)
        else:
            self.CommLocation = None
        self.Timeout = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        return _pos


    def get_CommLocation(self):
        return self.CommLocation

    def set_CommLocation(self, value):
        self.CommLocation = value 

    def get_Timeout(self):
        return self.Timeout

    def set_Timeout(self, value):
        self.Timeout = int( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = Task.Task.toString(self)
        buf += "From CommTransferTask:\n"
        buf +=    "CommLocation = " + str( self.CommLocation ) + "\n" 
        buf +=    "Timeout = " + str( self.Timeout ) + "\n" 

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
        str = ws + "<CommTransferTask>\n";
        #str +=Task.Task.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</CommTransferTask>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += Task.Task.toXMLMembersStr(self, ws)
        buf += ws + "<CommLocation>\n"
        if self.CommLocation == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.CommLocation.toXMLStr(ws + "    ") 
        buf += ws + "</CommLocation>\n"
        buf += ws + "<Timeout>" + str(self.Timeout) + "</Timeout>\n"

        return buf
        
