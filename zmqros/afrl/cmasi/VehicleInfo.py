#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *
from cmasi import Waypoint
from cmasi import Location3D
from cmasi import Location2D


class VehicleInfo(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 41
        self.SERIES_NAME = "CMASI"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 4849604199710720000
        self.SERIES_VERSION = 2

        #Define message fields
        self.VehicleID = 0   #uint32
        self.TaskEligibility = []   #uint32
        self.UseTaskEligibility = False   #bool
        self.Airspeed = 0   #real32
        self.UseAirspeed = False   #bool
        self.MaxAltitude = 0   #real32
        self.MinAltitude = 0   #real32
        self.UseAltitude = False   #bool
        self.ContingencyPoint = None   #Waypoint
        self.WaypointLimit = 0   #uint32
        self.StartPoint = None   #Location3D
        self.EndPoint = None   #Location2D


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">I", self.VehicleID))
        buffer.append(struct.pack(">H", len(self.TaskEligibility) ))
        for x in self.TaskEligibility:
            buffer.append(struct.pack(">I", x ))
        buffer.append(struct.pack(">B", self.UseTaskEligibility))
        buffer.append(struct.pack(">f", self.Airspeed))
        buffer.append(struct.pack(">B", self.UseAirspeed))
        buffer.append(struct.pack(">f", self.MaxAltitude))
        buffer.append(struct.pack(">f", self.MinAltitude))
        buffer.append(struct.pack(">B", self.UseAltitude))
        buffer.append(struct.pack("B", self.ContingencyPoint != None ))
        if self.ContingencyPoint != None:
            buffer.append(struct.pack(">q", self.ContingencyPoint.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.ContingencyPoint.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.ContingencyPoint.SERIES_VERSION))
            buffer.append(self.ContingencyPoint.pack())
        buffer.append(struct.pack(">I", self.WaypointLimit))
        buffer.append(struct.pack("B", self.StartPoint != None ))
        if self.StartPoint != None:
            buffer.append(struct.pack(">q", self.StartPoint.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.StartPoint.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.StartPoint.SERIES_VERSION))
            buffer.append(self.StartPoint.pack())
        buffer.append(struct.pack("B", self.EndPoint != None ))
        if self.EndPoint != None:
            buffer.append(struct.pack(">q", self.EndPoint.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.EndPoint.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.EndPoint.SERIES_VERSION))
            buffer.append(self.EndPoint.pack())

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.VehicleID = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.TaskEligibility = [None] * _arraylen
        _pos += 2
        if _arraylen > 0:
            self.TaskEligibility = struct.unpack_from(">" + `_arraylen` + "I", buffer, _pos )
            _pos += 4 * _arraylen
        self.UseTaskEligibility = struct.unpack_from(">B", buffer, _pos)[0]
        _pos += 1
        self.Airspeed = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.UseAirspeed = struct.unpack_from(">B", buffer, _pos)[0]
        _pos += 1
        self.MaxAltitude = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.MinAltitude = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.UseAltitude = struct.unpack_from(">B", buffer, _pos)[0]
        _pos += 1
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
            self.ContingencyPoint = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.ContingencyPoint.unpack(buffer, _pos)
        else:
            self.ContingencyPoint = None
        self.WaypointLimit = struct.unpack_from(">I", buffer, _pos)[0]
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
            self.StartPoint = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.StartPoint.unpack(buffer, _pos)
        else:
            self.StartPoint = None
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
            self.EndPoint = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.EndPoint.unpack(buffer, _pos)
        else:
            self.EndPoint = None
        return _pos


    def get_VehicleID(self):
        return self.VehicleID

    def set_VehicleID(self, value):
        self.VehicleID = int( value )

    def get_TaskEligibility(self):
        return self.TaskEligibility

    def get_UseTaskEligibility(self):
        return self.UseTaskEligibility

    def set_UseTaskEligibility(self, value):
        self.UseTaskEligibility = bool( value )

    def get_Airspeed(self):
        return self.Airspeed

    def set_Airspeed(self, value):
        self.Airspeed = float( value )

    def get_UseAirspeed(self):
        return self.UseAirspeed

    def set_UseAirspeed(self, value):
        self.UseAirspeed = bool( value )

    def get_MaxAltitude(self):
        return self.MaxAltitude

    def set_MaxAltitude(self, value):
        self.MaxAltitude = float( value )

    def get_MinAltitude(self):
        return self.MinAltitude

    def set_MinAltitude(self, value):
        self.MinAltitude = float( value )

    def get_UseAltitude(self):
        return self.UseAltitude

    def set_UseAltitude(self, value):
        self.UseAltitude = bool( value )

    def get_ContingencyPoint(self):
        return self.ContingencyPoint

    def set_ContingencyPoint(self, value):
        self.ContingencyPoint = value 

    def get_WaypointLimit(self):
        return self.WaypointLimit

    def set_WaypointLimit(self, value):
        self.WaypointLimit = int( value )

    def get_StartPoint(self):
        return self.StartPoint

    def set_StartPoint(self, value):
        self.StartPoint = value 

    def get_EndPoint(self):
        return self.EndPoint

    def set_EndPoint(self, value):
        self.EndPoint = value 



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From VehicleInfo:\n"
        buf +=    "VehicleID = " + str( self.VehicleID ) + "\n" 
        buf +=    "TaskEligibility = " + str( self.TaskEligibility ) + "\n" 
        buf +=    "UseTaskEligibility = " + str( self.UseTaskEligibility ) + "\n" 
        buf +=    "Airspeed = " + str( self.Airspeed ) + "\n" 
        buf +=    "UseAirspeed = " + str( self.UseAirspeed ) + "\n" 
        buf +=    "MaxAltitude = " + str( self.MaxAltitude ) + "\n" 
        buf +=    "MinAltitude = " + str( self.MinAltitude ) + "\n" 
        buf +=    "UseAltitude = " + str( self.UseAltitude ) + "\n" 
        buf +=    "ContingencyPoint = " + str( self.ContingencyPoint ) + "\n" 
        buf +=    "WaypointLimit = " + str( self.WaypointLimit ) + "\n" 
        buf +=    "StartPoint = " + str( self.StartPoint ) + "\n" 
        buf +=    "EndPoint = " + str( self.EndPoint ) + "\n" 

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
        str = ws + "<VehicleInfo>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</VehicleInfo>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<VehicleID>" + str(self.VehicleID) + "</VehicleID>\n"
        buf += ws + "<TaskEligibility>\n"
        for x in self.TaskEligibility:
            buf += ws + "<uint32>" + str(x) + "</uint32>\n"
        buf += ws + "</TaskEligibility>\n"
        buf += ws + "<UseTaskEligibility>" + str(self.UseTaskEligibility) + "</UseTaskEligibility>\n"
        buf += ws + "<Airspeed>" + str(self.Airspeed) + "</Airspeed>\n"
        buf += ws + "<UseAirspeed>" + str(self.UseAirspeed) + "</UseAirspeed>\n"
        buf += ws + "<MaxAltitude>" + str(self.MaxAltitude) + "</MaxAltitude>\n"
        buf += ws + "<MinAltitude>" + str(self.MinAltitude) + "</MinAltitude>\n"
        buf += ws + "<UseAltitude>" + str(self.UseAltitude) + "</UseAltitude>\n"
        buf += ws + "<ContingencyPoint>\n"
        if self.ContingencyPoint == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.ContingencyPoint.toXMLStr(ws + "    ") 
        buf += ws + "</ContingencyPoint>\n"
        buf += ws + "<WaypointLimit>" + str(self.WaypointLimit) + "</WaypointLimit>\n"
        buf += ws + "<StartPoint>\n"
        if self.StartPoint == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.StartPoint.toXMLStr(ws + "    ") 
        buf += ws + "</StartPoint>\n"
        buf += ws + "<EndPoint>\n"
        if self.EndPoint == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.EndPoint.toXMLStr(ws + "    ") 
        buf += ws + "</EndPoint>\n"

        return buf
        
