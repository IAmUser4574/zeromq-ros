#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *
from cmasi import VehicleAction
from cmasi import SpeedType


class FlightDirectorAction(VehicleAction.VehicleAction):

    def __init__(self):
        VehicleAction.VehicleAction.__init__(self)
        self.LMCP_TYPE = 50
        self.SERIES_NAME = "CMASI"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 4849604199710720000
        self.SERIES_VERSION = 2

        #Define message fields
        self.Speed = 0   #real32
        self.SpeedType = SpeedType.SpeedType.Airspeed   #SpeedType
        self.Heading = 0   #real32
        self.Altitude = 0   #real32
        self.ClimbRate = 0   #real32


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(VehicleAction.VehicleAction.pack(self))
        buffer.append(struct.pack(">f", self.Speed))
        buffer.append(struct.pack(">i", self.SpeedType))
        buffer.append(struct.pack(">f", self.Heading))
        buffer.append(struct.pack(">f", self.Altitude))
        buffer.append(struct.pack(">f", self.ClimbRate))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = VehicleAction.VehicleAction.unpack(self, buffer, _pos)
        self.Speed = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.SpeedType = struct.unpack_from(">i", buffer, _pos)[0]
        _pos += 4
        self.Heading = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.Altitude = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.ClimbRate = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        return _pos


    def get_Speed(self):
        return self.Speed

    def set_Speed(self, value):
        self.Speed = float( value )

    def get_SpeedType(self):
        return self.SpeedType

    def set_SpeedType(self, value):
        self.SpeedType = value 

    def get_Heading(self):
        return self.Heading

    def set_Heading(self, value):
        self.Heading = float( value )

    def get_Altitude(self):
        return self.Altitude

    def set_Altitude(self, value):
        self.Altitude = float( value )

    def get_ClimbRate(self):
        return self.ClimbRate

    def set_ClimbRate(self, value):
        self.ClimbRate = float( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = VehicleAction.VehicleAction.toString(self)
        buf += "From FlightDirectorAction:\n"
        buf +=    "Speed = " + str( self.Speed ) + "\n" 
        buf +=    "SpeedType = " + str( self.SpeedType ) + "\n" 
        buf +=    "Heading = " + str( self.Heading ) + "\n" 
        buf +=    "Altitude = " + str( self.Altitude ) + "\n" 
        buf +=    "ClimbRate = " + str( self.ClimbRate ) + "\n" 

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
        str = ws + "<FlightDirectorAction>\n";
        #str +=VehicleAction.VehicleAction.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</FlightDirectorAction>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += VehicleAction.VehicleAction.toXMLMembersStr(self, ws)
        buf += ws + "<Speed>" + str(self.Speed) + "</Speed>\n"
        buf += ws + "<SpeedType>" + SpeedType.get_SpeedType_int(self.SpeedType) + "</SpeedType>\n"
        buf += ws + "<Heading>" + str(self.Heading) + "</Heading>\n"
        buf += ws + "<Altitude>" + str(self.Altitude) + "</Altitude>\n"
        buf += ws + "<ClimbRate>" + str(self.ClimbRate) + "</ClimbRate>\n"

        return buf
        
