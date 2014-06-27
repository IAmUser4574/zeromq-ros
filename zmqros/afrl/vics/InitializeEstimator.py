#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *
from vics import NetworkRegion


class InitializeEstimator(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 37
        self.SERIES_NAME = "VICS"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6217574784323026944
        self.SERIES_VERSION = 17

        #Define message fields
        self.InitialTime = 0   #uint32
        self.Region = NetworkRegion.NetworkRegion()   #NetworkRegion
        self.ProbabilityUTurn = 0.05   #real32
        self.ProbabilityExit = 0.0   #real32
        self.CellLength = 60.0   #real32
        self.DefaultMinIntruderSpeed = 7.0   #real32
        self.DefaultMaxIntruderSpeed = 13.0   #real32
        self.DefaultSpeedStepSize = 2.0   #real32


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">I", self.InitialTime))
        buffer.append(struct.pack("B", self.Region != None ))
        if self.Region != None:
            buffer.append(struct.pack(">q", self.Region.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.Region.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.Region.SERIES_VERSION))
            buffer.append(self.Region.pack())
        buffer.append(struct.pack(">f", self.ProbabilityUTurn))
        buffer.append(struct.pack(">f", self.ProbabilityExit))
        buffer.append(struct.pack(">f", self.CellLength))
        buffer.append(struct.pack(">f", self.DefaultMinIntruderSpeed))
        buffer.append(struct.pack(">f", self.DefaultMaxIntruderSpeed))
        buffer.append(struct.pack(">f", self.DefaultSpeedStepSize))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.InitialTime = struct.unpack_from(">I", buffer, _pos)[0]
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
            self.Region = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.Region.unpack(buffer, _pos)
        else:
            self.Region = None
        self.ProbabilityUTurn = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.ProbabilityExit = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.CellLength = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.DefaultMinIntruderSpeed = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.DefaultMaxIntruderSpeed = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.DefaultSpeedStepSize = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        return _pos


    def get_InitialTime(self):
        return self.InitialTime

    def set_InitialTime(self, value):
        self.InitialTime = int( value )

    def get_Region(self):
        return self.Region

    def set_Region(self, value):
        self.Region = value 

    def get_ProbabilityUTurn(self):
        return self.ProbabilityUTurn

    def set_ProbabilityUTurn(self, value):
        self.ProbabilityUTurn = float( value )

    def get_ProbabilityExit(self):
        return self.ProbabilityExit

    def set_ProbabilityExit(self, value):
        self.ProbabilityExit = float( value )

    def get_CellLength(self):
        return self.CellLength

    def set_CellLength(self, value):
        self.CellLength = float( value )

    def get_DefaultMinIntruderSpeed(self):
        return self.DefaultMinIntruderSpeed

    def set_DefaultMinIntruderSpeed(self, value):
        self.DefaultMinIntruderSpeed = float( value )

    def get_DefaultMaxIntruderSpeed(self):
        return self.DefaultMaxIntruderSpeed

    def set_DefaultMaxIntruderSpeed(self, value):
        self.DefaultMaxIntruderSpeed = float( value )

    def get_DefaultSpeedStepSize(self):
        return self.DefaultSpeedStepSize

    def set_DefaultSpeedStepSize(self, value):
        self.DefaultSpeedStepSize = float( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From InitializeEstimator:\n"
        buf +=    "InitialTime = " + str( self.InitialTime ) + "\n" 
        buf +=    "Region = " + str( self.Region ) + "\n" 
        buf +=    "ProbabilityUTurn = " + str( self.ProbabilityUTurn ) + "\n" 
        buf +=    "ProbabilityExit = " + str( self.ProbabilityExit ) + "\n" 
        buf +=    "CellLength = " + str( self.CellLength ) + "\n" 
        buf +=    "DefaultMinIntruderSpeed = " + str( self.DefaultMinIntruderSpeed ) + "\n" 
        buf +=    "DefaultMaxIntruderSpeed = " + str( self.DefaultMaxIntruderSpeed ) + "\n" 
        buf +=    "DefaultSpeedStepSize = " + str( self.DefaultSpeedStepSize ) + "\n" 

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
        str = ws + "<InitializeEstimator>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</InitializeEstimator>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<InitialTime>" + str(self.InitialTime) + "</InitialTime>\n"
        buf += ws + "<Region>\n"
        if self.Region == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.Region.toXMLStr(ws + "    ") 
        buf += ws + "</Region>\n"
        buf += ws + "<ProbabilityUTurn>" + str(self.ProbabilityUTurn) + "</ProbabilityUTurn>\n"
        buf += ws + "<ProbabilityExit>" + str(self.ProbabilityExit) + "</ProbabilityExit>\n"
        buf += ws + "<CellLength>" + str(self.CellLength) + "</CellLength>\n"
        buf += ws + "<DefaultMinIntruderSpeed>" + str(self.DefaultMinIntruderSpeed) + "</DefaultMinIntruderSpeed>\n"
        buf += ws + "<DefaultMaxIntruderSpeed>" + str(self.DefaultMaxIntruderSpeed) + "</DefaultMaxIntruderSpeed>\n"
        buf += ws + "<DefaultSpeedStepSize>" + str(self.DefaultSpeedStepSize) + "</DefaultSpeedStepSize>\n"

        return buf
        
