#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *
from cmasi import Waypoint
from cmasi import CommandStatusType


class MissionCommand(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 24
        self.SERIES_NAME = "CMASI"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 4849604199710720000
        self.SERIES_VERSION = 2

        #Define message fields
        self.CommandID = 0   #uint32
        self.VehicleID = 0   #uint32
        self.WaypointList = []   #Waypoint
        self.FirstWaypoint = 0   #uint32
        self.Status = CommandStatusType.CommandStatusType.Pending   #CommandStatusType


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">I", self.CommandID))
        buffer.append(struct.pack(">I", self.VehicleID))
        buffer.append(struct.pack(">H", len(self.WaypointList) ))
        for x in self.WaypointList:
           buffer.append(struct.pack("B", x != None ))
           if x != None:
               buffer.append(struct.pack(">q", x.SERIES_NAME_ID))
               buffer.append(struct.pack(">I", x.LMCP_TYPE))
               buffer.append(struct.pack(">H", x.SERIES_VERSION))
               buffer.append(x.pack())
        buffer.append(struct.pack(">I", self.FirstWaypoint))
        buffer.append(struct.pack(">i", self.Status))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.CommandID = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        self.VehicleID = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.WaypointList = [None] * _arraylen
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
                self.WaypointList[x] = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
                _pos = self.WaypointList[x].unpack(buffer, _pos)
            else:
                self.WaypointList[x] = None
        self.FirstWaypoint = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        self.Status = struct.unpack_from(">i", buffer, _pos)[0]
        _pos += 4
        return _pos


    def get_CommandID(self):
        return self.CommandID

    def set_CommandID(self, value):
        self.CommandID = int( value )

    def get_VehicleID(self):
        return self.VehicleID

    def set_VehicleID(self, value):
        self.VehicleID = int( value )

    def get_WaypointList(self):
        return self.WaypointList

    def get_FirstWaypoint(self):
        return self.FirstWaypoint

    def set_FirstWaypoint(self, value):
        self.FirstWaypoint = int( value )

    def get_Status(self):
        return self.Status

    def set_Status(self, value):
        self.Status = value 



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From MissionCommand:\n"
        buf +=    "CommandID = " + str( self.CommandID ) + "\n" 
        buf +=    "VehicleID = " + str( self.VehicleID ) + "\n" 
        buf +=    "WaypointList = " + str( self.WaypointList ) + "\n" 
        buf +=    "FirstWaypoint = " + str( self.FirstWaypoint ) + "\n" 
        buf +=    "Status = " + str( self.Status ) + "\n" 

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
        str = ws + "<MissionCommand>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</MissionCommand>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<CommandID>" + str(self.CommandID) + "</CommandID>\n"
        buf += ws + "<VehicleID>" + str(self.VehicleID) + "</VehicleID>\n"
        buf += ws + "<WaypointList>\n"
        for x in self.WaypointList:
            if x == None:
                buf += ws + "    <null/>\n"
            else:
                buf += x.toXMLStr(ws + "    ") 
        buf += ws + "</WaypointList>\n"
        buf += ws + "<FirstWaypoint>" + str(self.FirstWaypoint) + "</FirstWaypoint>\n"
        buf += ws + "<Status>" + CommandStatusType.get_CommandStatusType_int(self.Status) + "</Status>\n"

        return buf
        
