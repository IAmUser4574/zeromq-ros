#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *
from vics import VicsBase
from vics import PayloadData
from cmasi import Location3D


class DismountMessage(VicsBase.VicsBase):

    def __init__(self):
        VicsBase.VicsBase.__init__(self)
        self.LMCP_TYPE = 14
        self.SERIES_NAME = "VICS"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6217574784323026944
        self.SERIES_VERSION = 17

        #Define message fields
        self.Payload = PayloadData.PayloadData()   #PayloadData
        self.Description = ""   #string
        self.Location = None   #Location3D


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(VicsBase.VicsBase.pack(self))
        buffer.append(struct.pack("B", self.Payload != None ))
        if self.Payload != None:
            buffer.append(struct.pack(">q", self.Payload.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.Payload.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.Payload.SERIES_VERSION))
            buffer.append(self.Payload.pack())
        buffer.append(struct.pack(">H", len(self.Description) ))
        if len(self.Description) > 0:
            buffer.append(struct.pack( `len(self.Description)` + "s", self.Description))
        buffer.append(struct.pack("B", self.Location != None ))
        if self.Location != None:
            buffer.append(struct.pack(">q", self.Location.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.Location.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.Location.SERIES_VERSION))
            buffer.append(self.Location.pack())

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = VicsBase.VicsBase.unpack(self, buffer, _pos)
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
            self.Payload = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.Payload.unpack(buffer, _pos)
        else:
            self.Payload = None
        _strlen = struct.unpack_from(">H", buffer, _pos )[0]
        _pos += 2
        if _strlen > 0:
            self.Description = struct.unpack_from( `_strlen` + "s", buffer, _pos )[0]
            _pos += _strlen
        else:
             self.Description = ""
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
            self.Location = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.Location.unpack(buffer, _pos)
        else:
            self.Location = None
        return _pos


    def get_Payload(self):
        return self.Payload

    def set_Payload(self, value):
        self.Payload = value 

    def get_Description(self):
        return self.Description

    def set_Description(self, value):
        self.Description = str( value )

    def get_Location(self):
        return self.Location

    def set_Location(self, value):
        self.Location = value 



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = VicsBase.VicsBase.toString(self)
        buf += "From DismountMessage:\n"
        buf +=    "Payload = " + str( self.Payload ) + "\n" 
        buf +=    "Description = " + str( self.Description ) + "\n" 
        buf +=    "Location = " + str( self.Location ) + "\n" 

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
        str = ws + "<DismountMessage>\n";
        #str +=VicsBase.VicsBase.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</DismountMessage>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += VicsBase.VicsBase.toXMLMembersStr(self, ws)
        buf += ws + "<Payload>\n"
        if self.Payload == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.Payload.toXMLStr(ws + "    ") 
        buf += ws + "</Payload>\n"
        buf += ws + "<Description>" + str(self.Description) + "</Description>\n"
        buf += ws + "<Location>\n"
        if self.Location == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.Location.toXMLStr(ws + "    ") 
        buf += ws + "</Location>\n"

        return buf
        
