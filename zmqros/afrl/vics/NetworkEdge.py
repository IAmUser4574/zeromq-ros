#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *
from vics import ValueFunction
from cmasi import Location3D
from vics import LocationXY


class NetworkEdge(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 35
        self.SERIES_NAME = "VICS"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6217574784323026944
        self.SERIES_VERSION = 17

        #Define message fields
        self.EdgeId = 0   #uint32
        self.ReverseEdgeId = 0   #uint32
        self.StartNode = 0   #uint32
        self.EndNode = 0   #uint32
        self.PositionProbability = ValueFunction.ValueFunction()   #ValueFunction
        self.VelocityProfile = ValueFunction.ValueFunction()   #ValueFunction
        self.EdgeLength = 0   #real32
        self.Waypoints = []   #Location3D
        self.WaypointsXY = []   #LocationXY


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">I", self.EdgeId))
        buffer.append(struct.pack(">I", self.ReverseEdgeId))
        buffer.append(struct.pack(">I", self.StartNode))
        buffer.append(struct.pack(">I", self.EndNode))
        buffer.append(struct.pack("B", self.PositionProbability != None ))
        if self.PositionProbability != None:
            buffer.append(struct.pack(">q", self.PositionProbability.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.PositionProbability.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.PositionProbability.SERIES_VERSION))
            buffer.append(self.PositionProbability.pack())
        buffer.append(struct.pack("B", self.VelocityProfile != None ))
        if self.VelocityProfile != None:
            buffer.append(struct.pack(">q", self.VelocityProfile.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.VelocityProfile.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.VelocityProfile.SERIES_VERSION))
            buffer.append(self.VelocityProfile.pack())
        buffer.append(struct.pack(">f", self.EdgeLength))
        buffer.append(struct.pack(">H", len(self.Waypoints) ))
        for x in self.Waypoints:
           buffer.append(struct.pack("B", x != None ))
           if x != None:
               buffer.append(struct.pack(">q", x.SERIES_NAME_ID))
               buffer.append(struct.pack(">I", x.LMCP_TYPE))
               buffer.append(struct.pack(">H", x.SERIES_VERSION))
               buffer.append(x.pack())
        buffer.append(struct.pack(">H", len(self.WaypointsXY) ))
        for x in self.WaypointsXY:
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
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.EdgeId = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        self.ReverseEdgeId = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        self.StartNode = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        self.EndNode = struct.unpack_from(">I", buffer, _pos)[0]
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
            self.PositionProbability = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.PositionProbability.unpack(buffer, _pos)
        else:
            self.PositionProbability = None
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
            self.VelocityProfile = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.VelocityProfile.unpack(buffer, _pos)
        else:
            self.VelocityProfile = None
        self.EdgeLength = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.Waypoints = [None] * _arraylen
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
                self.Waypoints[x] = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
                _pos = self.Waypoints[x].unpack(buffer, _pos)
            else:
                self.Waypoints[x] = None
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.WaypointsXY = [None] * _arraylen
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
                self.WaypointsXY[x] = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
                _pos = self.WaypointsXY[x].unpack(buffer, _pos)
            else:
                self.WaypointsXY[x] = None
        return _pos


    def get_EdgeId(self):
        return self.EdgeId

    def set_EdgeId(self, value):
        self.EdgeId = int( value )

    def get_ReverseEdgeId(self):
        return self.ReverseEdgeId

    def set_ReverseEdgeId(self, value):
        self.ReverseEdgeId = int( value )

    def get_StartNode(self):
        return self.StartNode

    def set_StartNode(self, value):
        self.StartNode = int( value )

    def get_EndNode(self):
        return self.EndNode

    def set_EndNode(self, value):
        self.EndNode = int( value )

    def get_PositionProbability(self):
        return self.PositionProbability

    def set_PositionProbability(self, value):
        self.PositionProbability = value 

    def get_VelocityProfile(self):
        return self.VelocityProfile

    def set_VelocityProfile(self, value):
        self.VelocityProfile = value 

    def get_EdgeLength(self):
        return self.EdgeLength

    def set_EdgeLength(self, value):
        self.EdgeLength = float( value )

    def get_Waypoints(self):
        return self.Waypoints

    def get_WaypointsXY(self):
        return self.WaypointsXY



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From NetworkEdge:\n"
        buf +=    "EdgeId = " + str( self.EdgeId ) + "\n" 
        buf +=    "ReverseEdgeId = " + str( self.ReverseEdgeId ) + "\n" 
        buf +=    "StartNode = " + str( self.StartNode ) + "\n" 
        buf +=    "EndNode = " + str( self.EndNode ) + "\n" 
        buf +=    "PositionProbability = " + str( self.PositionProbability ) + "\n" 
        buf +=    "VelocityProfile = " + str( self.VelocityProfile ) + "\n" 
        buf +=    "EdgeLength = " + str( self.EdgeLength ) + "\n" 
        buf +=    "Waypoints = " + str( self.Waypoints ) + "\n" 
        buf +=    "WaypointsXY = " + str( self.WaypointsXY ) + "\n" 

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
        str = ws + "<NetworkEdge>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</NetworkEdge>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<EdgeId>" + str(self.EdgeId) + "</EdgeId>\n"
        buf += ws + "<ReverseEdgeId>" + str(self.ReverseEdgeId) + "</ReverseEdgeId>\n"
        buf += ws + "<StartNode>" + str(self.StartNode) + "</StartNode>\n"
        buf += ws + "<EndNode>" + str(self.EndNode) + "</EndNode>\n"
        buf += ws + "<PositionProbability>\n"
        if self.PositionProbability == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.PositionProbability.toXMLStr(ws + "    ") 
        buf += ws + "</PositionProbability>\n"
        buf += ws + "<VelocityProfile>\n"
        if self.VelocityProfile == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.VelocityProfile.toXMLStr(ws + "    ") 
        buf += ws + "</VelocityProfile>\n"
        buf += ws + "<EdgeLength>" + str(self.EdgeLength) + "</EdgeLength>\n"
        buf += ws + "<Waypoints>\n"
        for x in self.Waypoints:
            if x == None:
                buf += ws + "    <null/>\n"
            else:
                buf += x.toXMLStr(ws + "    ") 
        buf += ws + "</Waypoints>\n"
        buf += ws + "<WaypointsXY>\n"
        for x in self.WaypointsXY:
            if x == None:
                buf += ws + "    <null/>\n"
            else:
                buf += x.toXMLStr(ws + "    ") 
        buf += ws + "</WaypointsXY>\n"

        return buf
        
