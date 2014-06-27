#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *
from cmasi import Location3D
from cmasi import PayloadState
from cmasi import NavigationMode


class AirVehicleState(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 4
        self.SERIES_NAME = "CMASI"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 4849604199710720000
        self.SERIES_VERSION = 2

        #Define message fields
        self.VehicleID = 0   #uint32
        self.Position = Location3D.Location3D()   #Location3D
        self.u = 0   #real32
        self.v = 0   #real32
        self.w = 0   #real32
        self.udot = 0   #real32
        self.vdot = 0   #real32
        self.wdot = 0   #real32
        self.Heading = 0   #real32
        self.Pitch = 0   #real32
        self.Roll = 0   #real32
        self.p = 0   #real32
        self.q = 0   #real32
        self.r = 0   #real32
        self.Airspeed = 0   #real32
        self.VerticalSpeed = 0   #real32
        self.ActualEnergyRate = 0   #real32
        self.EnergyAvailable = 0   #real32
        self.WindSpeed = 0   #real32
        self.WindDirection = 0   #real32
        self.GroundSpeed = 0   #real32
        self.GroundTrack = 0   #real32
        self.PayloadStateList = []   #PayloadState
        self.CurrentWaypoint = 0   #uint32
        self.CurrentCommand = 0   #uint32
        self.Mode = NavigationMode.NavigationMode.Waypoint   #NavigationMode
        self.AssociatedTasks = []   #uint32
        self.Time = 0   #real64


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">I", self.VehicleID))
        buffer.append(struct.pack("B", self.Position != None ))
        if self.Position != None:
            buffer.append(struct.pack(">q", self.Position.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.Position.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.Position.SERIES_VERSION))
            buffer.append(self.Position.pack())
        buffer.append(struct.pack(">f", self.u))
        buffer.append(struct.pack(">f", self.v))
        buffer.append(struct.pack(">f", self.w))
        buffer.append(struct.pack(">f", self.udot))
        buffer.append(struct.pack(">f", self.vdot))
        buffer.append(struct.pack(">f", self.wdot))
        buffer.append(struct.pack(">f", self.Heading))
        buffer.append(struct.pack(">f", self.Pitch))
        buffer.append(struct.pack(">f", self.Roll))
        buffer.append(struct.pack(">f", self.p))
        buffer.append(struct.pack(">f", self.q))
        buffer.append(struct.pack(">f", self.r))
        buffer.append(struct.pack(">f", self.Airspeed))
        buffer.append(struct.pack(">f", self.VerticalSpeed))
        buffer.append(struct.pack(">f", self.ActualEnergyRate))
        buffer.append(struct.pack(">f", self.EnergyAvailable))
        buffer.append(struct.pack(">f", self.WindSpeed))
        buffer.append(struct.pack(">f", self.WindDirection))
        buffer.append(struct.pack(">f", self.GroundSpeed))
        buffer.append(struct.pack(">f", self.GroundTrack))
        buffer.append(struct.pack(">H", len(self.PayloadStateList) ))
        for x in self.PayloadStateList:
           buffer.append(struct.pack("B", x != None ))
           if x != None:
               buffer.append(struct.pack(">q", x.SERIES_NAME_ID))
               buffer.append(struct.pack(">I", x.LMCP_TYPE))
               buffer.append(struct.pack(">H", x.SERIES_VERSION))
               buffer.append(x.pack())
        buffer.append(struct.pack(">I", self.CurrentWaypoint))
        buffer.append(struct.pack(">I", self.CurrentCommand))
        buffer.append(struct.pack(">i", self.Mode))
        buffer.append(struct.pack(">H", len(self.AssociatedTasks) ))
        for x in self.AssociatedTasks:
            buffer.append(struct.pack(">I", x ))
        buffer.append(struct.pack(">d", self.Time))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.VehicleID = struct.unpack_from(">I", buffer, _pos)[0]
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
            self.Position = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.Position.unpack(buffer, _pos)
        else:
            self.Position = None
        self.u = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.v = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.w = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.udot = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.vdot = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.wdot = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.Heading = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.Pitch = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.Roll = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.p = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.q = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.r = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.Airspeed = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.VerticalSpeed = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.ActualEnergyRate = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.EnergyAvailable = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.WindSpeed = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.WindDirection = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.GroundSpeed = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.GroundTrack = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.PayloadStateList = [None] * _arraylen
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
                self.PayloadStateList[x] = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
                _pos = self.PayloadStateList[x].unpack(buffer, _pos)
            else:
                self.PayloadStateList[x] = None
        self.CurrentWaypoint = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        self.CurrentCommand = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        self.Mode = struct.unpack_from(">i", buffer, _pos)[0]
        _pos += 4
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.AssociatedTasks = [None] * _arraylen
        _pos += 2
        if _arraylen > 0:
            self.AssociatedTasks = struct.unpack_from(">" + `_arraylen` + "I", buffer, _pos )
            _pos += 4 * _arraylen
        self.Time = struct.unpack_from(">d", buffer, _pos)[0]
        _pos += 8
        return _pos


    def get_VehicleID(self):
        return self.VehicleID

    def set_VehicleID(self, value):
        self.VehicleID = int( value )

    def get_Position(self):
        return self.Position

    def set_Position(self, value):
        self.Position = value 

    def get_u(self):
        return self.u

    def set_u(self, value):
        self.u = float( value )

    def get_v(self):
        return self.v

    def set_v(self, value):
        self.v = float( value )

    def get_w(self):
        return self.w

    def set_w(self, value):
        self.w = float( value )

    def get_udot(self):
        return self.udot

    def set_udot(self, value):
        self.udot = float( value )

    def get_vdot(self):
        return self.vdot

    def set_vdot(self, value):
        self.vdot = float( value )

    def get_wdot(self):
        return self.wdot

    def set_wdot(self, value):
        self.wdot = float( value )

    def get_Heading(self):
        return self.Heading

    def set_Heading(self, value):
        self.Heading = float( value )

    def get_Pitch(self):
        return self.Pitch

    def set_Pitch(self, value):
        self.Pitch = float( value )

    def get_Roll(self):
        return self.Roll

    def set_Roll(self, value):
        self.Roll = float( value )

    def get_p(self):
        return self.p

    def set_p(self, value):
        self.p = float( value )

    def get_q(self):
        return self.q

    def set_q(self, value):
        self.q = float( value )

    def get_r(self):
        return self.r

    def set_r(self, value):
        self.r = float( value )

    def get_Airspeed(self):
        return self.Airspeed

    def set_Airspeed(self, value):
        self.Airspeed = float( value )

    def get_VerticalSpeed(self):
        return self.VerticalSpeed

    def set_VerticalSpeed(self, value):
        self.VerticalSpeed = float( value )

    def get_ActualEnergyRate(self):
        return self.ActualEnergyRate

    def set_ActualEnergyRate(self, value):
        self.ActualEnergyRate = float( value )

    def get_EnergyAvailable(self):
        return self.EnergyAvailable

    def set_EnergyAvailable(self, value):
        self.EnergyAvailable = float( value )

    def get_WindSpeed(self):
        return self.WindSpeed

    def set_WindSpeed(self, value):
        self.WindSpeed = float( value )

    def get_WindDirection(self):
        return self.WindDirection

    def set_WindDirection(self, value):
        self.WindDirection = float( value )

    def get_GroundSpeed(self):
        return self.GroundSpeed

    def set_GroundSpeed(self, value):
        self.GroundSpeed = float( value )

    def get_GroundTrack(self):
        return self.GroundTrack

    def set_GroundTrack(self, value):
        self.GroundTrack = float( value )

    def get_PayloadStateList(self):
        return self.PayloadStateList

    def get_CurrentWaypoint(self):
        return self.CurrentWaypoint

    def set_CurrentWaypoint(self, value):
        self.CurrentWaypoint = int( value )

    def get_CurrentCommand(self):
        return self.CurrentCommand

    def set_CurrentCommand(self, value):
        self.CurrentCommand = int( value )

    def get_Mode(self):
        return self.Mode

    def set_Mode(self, value):
        self.Mode = value 

    def get_AssociatedTasks(self):
        return self.AssociatedTasks

    def get_Time(self):
        return self.Time

    def set_Time(self, value):
        self.Time = float( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From AirVehicleState:\n"
        buf +=    "VehicleID = " + str( self.VehicleID ) + "\n" 
        buf +=    "Position = " + str( self.Position ) + "\n" 
        buf +=    "u = " + str( self.u ) + "\n" 
        buf +=    "v = " + str( self.v ) + "\n" 
        buf +=    "w = " + str( self.w ) + "\n" 
        buf +=    "udot = " + str( self.udot ) + "\n" 
        buf +=    "vdot = " + str( self.vdot ) + "\n" 
        buf +=    "wdot = " + str( self.wdot ) + "\n" 
        buf +=    "Heading = " + str( self.Heading ) + "\n" 
        buf +=    "Pitch = " + str( self.Pitch ) + "\n" 
        buf +=    "Roll = " + str( self.Roll ) + "\n" 
        buf +=    "p = " + str( self.p ) + "\n" 
        buf +=    "q = " + str( self.q ) + "\n" 
        buf +=    "r = " + str( self.r ) + "\n" 
        buf +=    "Airspeed = " + str( self.Airspeed ) + "\n" 
        buf +=    "VerticalSpeed = " + str( self.VerticalSpeed ) + "\n" 
        buf +=    "ActualEnergyRate = " + str( self.ActualEnergyRate ) + "\n" 
        buf +=    "EnergyAvailable = " + str( self.EnergyAvailable ) + "\n" 
        buf +=    "WindSpeed = " + str( self.WindSpeed ) + "\n" 
        buf +=    "WindDirection = " + str( self.WindDirection ) + "\n" 
        buf +=    "GroundSpeed = " + str( self.GroundSpeed ) + "\n" 
        buf +=    "GroundTrack = " + str( self.GroundTrack ) + "\n" 
        buf +=    "PayloadStateList = " + str( self.PayloadStateList ) + "\n" 
        buf +=    "CurrentWaypoint = " + str( self.CurrentWaypoint ) + "\n" 
        buf +=    "CurrentCommand = " + str( self.CurrentCommand ) + "\n" 
        buf +=    "Mode = " + str( self.Mode ) + "\n" 
        buf +=    "AssociatedTasks = " + str( self.AssociatedTasks ) + "\n" 
        buf +=    "Time = " + str( self.Time ) + "\n" 

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
        str = ws + "<AirVehicleState>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</AirVehicleState>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<VehicleID>" + str(self.VehicleID) + "</VehicleID>\n"
        buf += ws + "<Position>\n"
        if self.Position == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.Position.toXMLStr(ws + "    ") 
        buf += ws + "</Position>\n"
        buf += ws + "<u>" + str(self.u) + "</u>\n"
        buf += ws + "<v>" + str(self.v) + "</v>\n"
        buf += ws + "<w>" + str(self.w) + "</w>\n"
        buf += ws + "<udot>" + str(self.udot) + "</udot>\n"
        buf += ws + "<vdot>" + str(self.vdot) + "</vdot>\n"
        buf += ws + "<wdot>" + str(self.wdot) + "</wdot>\n"
        buf += ws + "<Heading>" + str(self.Heading) + "</Heading>\n"
        buf += ws + "<Pitch>" + str(self.Pitch) + "</Pitch>\n"
        buf += ws + "<Roll>" + str(self.Roll) + "</Roll>\n"
        buf += ws + "<p>" + str(self.p) + "</p>\n"
        buf += ws + "<q>" + str(self.q) + "</q>\n"
        buf += ws + "<r>" + str(self.r) + "</r>\n"
        buf += ws + "<Airspeed>" + str(self.Airspeed) + "</Airspeed>\n"
        buf += ws + "<VerticalSpeed>" + str(self.VerticalSpeed) + "</VerticalSpeed>\n"
        buf += ws + "<ActualEnergyRate>" + str(self.ActualEnergyRate) + "</ActualEnergyRate>\n"
        buf += ws + "<EnergyAvailable>" + str(self.EnergyAvailable) + "</EnergyAvailable>\n"
        buf += ws + "<WindSpeed>" + str(self.WindSpeed) + "</WindSpeed>\n"
        buf += ws + "<WindDirection>" + str(self.WindDirection) + "</WindDirection>\n"
        buf += ws + "<GroundSpeed>" + str(self.GroundSpeed) + "</GroundSpeed>\n"
        buf += ws + "<GroundTrack>" + str(self.GroundTrack) + "</GroundTrack>\n"
        buf += ws + "<PayloadStateList>\n"
        for x in self.PayloadStateList:
            if x == None:
                buf += ws + "    <null/>\n"
            else:
                buf += x.toXMLStr(ws + "    ") 
        buf += ws + "</PayloadStateList>\n"
        buf += ws + "<CurrentWaypoint>" + str(self.CurrentWaypoint) + "</CurrentWaypoint>\n"
        buf += ws + "<CurrentCommand>" + str(self.CurrentCommand) + "</CurrentCommand>\n"
        buf += ws + "<Mode>" + NavigationMode.get_NavigationMode_int(self.Mode) + "</Mode>\n"
        buf += ws + "<AssociatedTasks>\n"
        for x in self.AssociatedTasks:
            buf += ws + "<uint32>" + str(x) + "</uint32>\n"
        buf += ws + "</AssociatedTasks>\n"
        buf += ws + "<Time>" + str(self.Time) + "</Time>\n"

        return buf
        
