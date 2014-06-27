#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *
from cmasi import Task
from cmasi import Location3D
from vics import MessageRequest


class DeliverMessageTask(Task.Task):

    def __init__(self):
        Task.Task.__init__(self)
        self.LMCP_TYPE = 4
        self.SERIES_NAME = "VICS"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6217574784323026944
        self.SERIES_VERSION = 17

        #Define message fields
        self.DeliverLocation = Location3D.Location3D()   #Location3D
        self.Timeout = 0   #uint32
        self.DeliveryMessages = []   #MessageRequest


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(Task.Task.pack(self))
        buffer.append(struct.pack("B", self.DeliverLocation != None ))
        if self.DeliverLocation != None:
            buffer.append(struct.pack(">q", self.DeliverLocation.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.DeliverLocation.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.DeliverLocation.SERIES_VERSION))
            buffer.append(self.DeliverLocation.pack())
        buffer.append(struct.pack(">I", self.Timeout))
        buffer.append(struct.pack(">H", len(self.DeliveryMessages) ))
        for x in self.DeliveryMessages:
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
            self.DeliverLocation = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.DeliverLocation.unpack(buffer, _pos)
        else:
            self.DeliverLocation = None
        self.Timeout = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.DeliveryMessages = [None] * _arraylen
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
                self.DeliveryMessages[x] = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
                _pos = self.DeliveryMessages[x].unpack(buffer, _pos)
            else:
                self.DeliveryMessages[x] = None
        return _pos


    def get_DeliverLocation(self):
        return self.DeliverLocation

    def set_DeliverLocation(self, value):
        self.DeliverLocation = value 

    def get_Timeout(self):
        return self.Timeout

    def set_Timeout(self, value):
        self.Timeout = int( value )

    def get_DeliveryMessages(self):
        return self.DeliveryMessages



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = Task.Task.toString(self)
        buf += "From DeliverMessageTask:\n"
        buf +=    "DeliverLocation = " + str( self.DeliverLocation ) + "\n" 
        buf +=    "Timeout = " + str( self.Timeout ) + "\n" 
        buf +=    "DeliveryMessages = " + str( self.DeliveryMessages ) + "\n" 

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
        str = ws + "<DeliverMessageTask>\n";
        #str +=Task.Task.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</DeliverMessageTask>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += Task.Task.toXMLMembersStr(self, ws)
        buf += ws + "<DeliverLocation>\n"
        if self.DeliverLocation == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.DeliverLocation.toXMLStr(ws + "    ") 
        buf += ws + "</DeliverLocation>\n"
        buf += ws + "<Timeout>" + str(self.Timeout) + "</Timeout>\n"
        buf += ws + "<DeliveryMessages>\n"
        for x in self.DeliveryMessages:
            if x == None:
                buf += ws + "    <null/>\n"
            else:
                buf += x.toXMLStr(ws + "    ") 
        buf += ws + "</DeliveryMessages>\n"

        return buf
        
