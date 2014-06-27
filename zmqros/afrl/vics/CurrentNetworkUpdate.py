#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *
from vics import IntruderAlert


class CurrentNetworkUpdate(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 43
        self.SERIES_NAME = "VICS"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6217574784323026944
        self.SERIES_VERSION = 17

        #Define message fields
        self.Alert = IntruderAlert.IntruderAlert()   #IntruderAlert


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack("B", self.Alert != None ))
        if self.Alert != None:
            buffer.append(struct.pack(">q", self.Alert.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.Alert.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.Alert.SERIES_VERSION))
            buffer.append(self.Alert.pack())

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
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
            self.Alert = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.Alert.unpack(buffer, _pos)
        else:
            self.Alert = None
        return _pos


    def get_Alert(self):
        return self.Alert

    def set_Alert(self, value):
        self.Alert = value 



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From CurrentNetworkUpdate:\n"
        buf +=    "Alert = " + str( self.Alert ) + "\n" 

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
        str = ws + "<CurrentNetworkUpdate>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</CurrentNetworkUpdate>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<Alert>\n"
        if self.Alert == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.Alert.toXMLStr(ws + "    ") 
        buf += ws + "</Alert>\n"

        return buf
        
