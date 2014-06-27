#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *
from vics import VicsBase
from cmasi import Location3D
from vics import IntruderType
from vics import PayloadData


class IntruderAlert(VicsBase.VicsBase):

    def __init__(self):
        VicsBase.VicsBase.__init__(self)
        self.LMCP_TYPE = 15
        self.SERIES_NAME = "VICS"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6217574784323026944
        self.SERIES_VERSION = 17

        #Define message fields
        self.DetectionLocation = Location3D.Location3D()   #Location3D
        self.UgsId = 0   #uint32
        self.Intruder = IntruderType.IntruderType.NoDetection   #IntruderType
        self.ObjectSpeed = 0   #real32
        self.ObjectDirection = 0   #real32
        self.PayloadDescription = ""   #string
        self.Payload = PayloadData.PayloadData()   #PayloadData


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(VicsBase.VicsBase.pack(self))
        buffer.append(struct.pack("B", self.DetectionLocation != None ))
        if self.DetectionLocation != None:
            buffer.append(struct.pack(">q", self.DetectionLocation.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.DetectionLocation.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.DetectionLocation.SERIES_VERSION))
            buffer.append(self.DetectionLocation.pack())
        buffer.append(struct.pack(">I", self.UgsId))
        buffer.append(struct.pack(">i", self.Intruder))
        buffer.append(struct.pack(">f", self.ObjectSpeed))
        buffer.append(struct.pack(">f", self.ObjectDirection))
        buffer.append(struct.pack(">H", len(self.PayloadDescription) ))
        if len(self.PayloadDescription) > 0:
            buffer.append(struct.pack( `len(self.PayloadDescription)` + "s", self.PayloadDescription))
        buffer.append(struct.pack("B", self.Payload != None ))
        if self.Payload != None:
            buffer.append(struct.pack(">q", self.Payload.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.Payload.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.Payload.SERIES_VERSION))
            buffer.append(self.Payload.pack())

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
            self.DetectionLocation = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.DetectionLocation.unpack(buffer, _pos)
        else:
            self.DetectionLocation = None
        self.UgsId = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        self.Intruder = struct.unpack_from(">i", buffer, _pos)[0]
        _pos += 4
        self.ObjectSpeed = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.ObjectDirection = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        _strlen = struct.unpack_from(">H", buffer, _pos )[0]
        _pos += 2
        if _strlen > 0:
            self.PayloadDescription = struct.unpack_from( `_strlen` + "s", buffer, _pos )[0]
            _pos += _strlen
        else:
             self.PayloadDescription = ""
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
        return _pos


    def get_DetectionLocation(self):
        return self.DetectionLocation

    def set_DetectionLocation(self, value):
        self.DetectionLocation = value 

    def get_UgsId(self):
        return self.UgsId

    def set_UgsId(self, value):
        self.UgsId = int( value )

    def get_Intruder(self):
        return self.Intruder

    def set_Intruder(self, value):
        self.Intruder = value 

    def get_ObjectSpeed(self):
        return self.ObjectSpeed

    def set_ObjectSpeed(self, value):
        self.ObjectSpeed = float( value )

    def get_ObjectDirection(self):
        return self.ObjectDirection

    def set_ObjectDirection(self, value):
        self.ObjectDirection = float( value )

    def get_PayloadDescription(self):
        return self.PayloadDescription

    def set_PayloadDescription(self, value):
        self.PayloadDescription = str( value )

    def get_Payload(self):
        return self.Payload

    def set_Payload(self, value):
        self.Payload = value 



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = VicsBase.VicsBase.toString(self)
        buf += "From IntruderAlert:\n"
        buf +=    "DetectionLocation = " + str( self.DetectionLocation ) + "\n" 
        buf +=    "UgsId = " + str( self.UgsId ) + "\n" 
        buf +=    "Intruder = " + str( self.Intruder ) + "\n" 
        buf +=    "ObjectSpeed = " + str( self.ObjectSpeed ) + "\n" 
        buf +=    "ObjectDirection = " + str( self.ObjectDirection ) + "\n" 
        buf +=    "PayloadDescription = " + str( self.PayloadDescription ) + "\n" 
        buf +=    "Payload = " + str( self.Payload ) + "\n" 

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
        str = ws + "<IntruderAlert>\n";
        #str +=VicsBase.VicsBase.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</IntruderAlert>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += VicsBase.VicsBase.toXMLMembersStr(self, ws)
        buf += ws + "<DetectionLocation>\n"
        if self.DetectionLocation == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.DetectionLocation.toXMLStr(ws + "    ") 
        buf += ws + "</DetectionLocation>\n"
        buf += ws + "<UgsId>" + str(self.UgsId) + "</UgsId>\n"
        buf += ws + "<Intruder>" + IntruderType.get_IntruderType_int(self.Intruder) + "</Intruder>\n"
        buf += ws + "<ObjectSpeed>" + str(self.ObjectSpeed) + "</ObjectSpeed>\n"
        buf += ws + "<ObjectDirection>" + str(self.ObjectDirection) + "</ObjectDirection>\n"
        buf += ws + "<PayloadDescription>" + str(self.PayloadDescription) + "</PayloadDescription>\n"
        buf += ws + "<Payload>\n"
        if self.Payload == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.Payload.toXMLStr(ws + "    ") 
        buf += ws + "</Payload>\n"

        return buf
        
