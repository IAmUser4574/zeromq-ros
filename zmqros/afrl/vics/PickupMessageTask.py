#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *
from cmasi import Task
from cmasi import Location3D
from vics import MessageRequest


class PickupMessageTask(Task.Task):

    def __init__(self):
        Task.Task.__init__(self)
        self.LMCP_TYPE = 3
        self.SERIES_NAME = "VICS"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6217574784323026944
        self.SERIES_VERSION = 17

        #Define message fields
        self.PickupLocation = Location3D.Location3D()   #Location3D
        self.Timeout = 0   #uint32
        self.PickupRequests = []   #MessageRequest


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(Task.Task.pack(self))
        buffer.append(struct.pack("B", self.PickupLocation != None ))
        if self.PickupLocation != None:
            buffer.append(struct.pack(">q", self.PickupLocation.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.PickupLocation.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.PickupLocation.SERIES_VERSION))
            buffer.append(self.PickupLocation.pack())
        buffer.append(struct.pack(">I", self.Timeout))
        buffer.append(struct.pack(">H", len(self.PickupRequests) ))
        for x in self.PickupRequests:
           buffer.append(struct.pack("B", x != None ))
           if x != None:
               buffer.append(struct.pack(">q", x.SERIES_NAME_ID))
               buffer.append(struct.pack(">I", x.LMCP_TYPE))
               buffer.append(struct.pack(">H", x.SERIES_VERSION))
               buffer.append(x.pack())

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
            self.PickupLocation = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.PickupLocation.unpack(buffer, _pos)
        else:
            self.PickupLocation = None
        self.Timeout = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.PickupRequests = [None] * _arraylen
        _pos += 2
        for x in range(_arraylen):
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
                self.PickupRequests[x] = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
                _pos = self.PickupRequests[x].unpack(buffer, _pos)
            else:
                self.PickupRequests[x] = None
        return _pos


    def get_PickupLocation(self):
        return self.PickupLocation

    def set_PickupLocation(self, value):
        self.PickupLocation = value 

    def get_Timeout(self):
        return self.Timeout

    def set_Timeout(self, value):
        self.Timeout = int( value )

    def get_PickupRequests(self):
        return self.PickupRequests



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = Task.Task.toString(self)
        buf += "From PickupMessageTask:\n"
        buf +=    "PickupLocation = " + str( self.PickupLocation ) + "\n" 
        buf +=    "Timeout = " + str( self.Timeout ) + "\n" 
        buf +=    "PickupRequests = " + str( self.PickupRequests ) + "\n" 

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
        str = ws + "<PickupMessageTask>\n";
        #str +=Task.Task.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</PickupMessageTask>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += Task.Task.toXMLMembersStr(self, ws)
        buf += ws + "<PickupLocation>\n"
        if self.PickupLocation == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.PickupLocation.toXMLStr(ws + "    ") 
        buf += ws + "</PickupLocation>\n"
        buf += ws + "<Timeout>" + str(self.Timeout) + "</Timeout>\n"
        buf += ws + "<PickupRequests>\n"
        for x in self.PickupRequests:
            if x == None:
                buf += ws + "    <null/>\n"
            else:
                buf += x.toXMLStr(ws + "    ") 
        buf += ws + "</PickupRequests>\n"

        return buf
        
