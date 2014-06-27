#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *
from vics import VicsBase
from cmasi import Location3D


class UgsStatusResponse(VicsBase.VicsBase):

    def __init__(self):
        VicsBase.VicsBase.__init__(self)
        self.LMCP_TYPE = 18
        self.SERIES_NAME = "VICS"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6217574784323026944
        self.SERIES_VERSION = 17

        #Define message fields
        self.DefaultRadarEnable = True   #bool
        self.HeadingAngle = 0   #real32
        self.ReportedLocation = Location3D.Location3D()   #Location3D
        self.CurrentTime = 0   #uint32


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(VicsBase.VicsBase.pack(self))
        buffer.append(struct.pack(">B", self.DefaultRadarEnable))
        buffer.append(struct.pack(">f", self.HeadingAngle))
        buffer.append(struct.pack("B", self.ReportedLocation != None ))
        if self.ReportedLocation != None:
            buffer.append(struct.pack(">q", self.ReportedLocation.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.ReportedLocation.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.ReportedLocation.SERIES_VERSION))
            buffer.append(self.ReportedLocation.pack())
        buffer.append(struct.pack(">I", self.CurrentTime))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = VicsBase.VicsBase.unpack(self, buffer, _pos)
        self.DefaultRadarEnable = struct.unpack_from(">B", buffer, _pos)[0]
        _pos += 1
        self.HeadingAngle = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
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
            self.ReportedLocation = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.ReportedLocation.unpack(buffer, _pos)
        else:
            self.ReportedLocation = None
        self.CurrentTime = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        return _pos


    def get_DefaultRadarEnable(self):
        return self.DefaultRadarEnable

    def set_DefaultRadarEnable(self, value):
        self.DefaultRadarEnable = bool( value )

    def get_HeadingAngle(self):
        return self.HeadingAngle

    def set_HeadingAngle(self, value):
        self.HeadingAngle = float( value )

    def get_ReportedLocation(self):
        return self.ReportedLocation

    def set_ReportedLocation(self, value):
        self.ReportedLocation = value 

    def get_CurrentTime(self):
        return self.CurrentTime

    def set_CurrentTime(self, value):
        self.CurrentTime = int( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = VicsBase.VicsBase.toString(self)
        buf += "From UgsStatusResponse:\n"
        buf +=    "DefaultRadarEnable = " + str( self.DefaultRadarEnable ) + "\n" 
        buf +=    "HeadingAngle = " + str( self.HeadingAngle ) + "\n" 
        buf +=    "ReportedLocation = " + str( self.ReportedLocation ) + "\n" 
        buf +=    "CurrentTime = " + str( self.CurrentTime ) + "\n" 

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
        str = ws + "<UgsStatusResponse>\n";
        #str +=VicsBase.VicsBase.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</UgsStatusResponse>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += VicsBase.VicsBase.toXMLMembersStr(self, ws)
        buf += ws + "<DefaultRadarEnable>" + str(self.DefaultRadarEnable) + "</DefaultRadarEnable>\n"
        buf += ws + "<HeadingAngle>" + str(self.HeadingAngle) + "</HeadingAngle>\n"
        buf += ws + "<ReportedLocation>\n"
        if self.ReportedLocation == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.ReportedLocation.toXMLStr(ws + "    ") 
        buf += ws + "</ReportedLocation>\n"
        buf += ws + "<CurrentTime>" + str(self.CurrentTime) + "</CurrentTime>\n"

        return buf
        
