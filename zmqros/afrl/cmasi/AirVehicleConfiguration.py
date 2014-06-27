#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *
from cmasi import FlightProfile
from cmasi import PayloadConfiguration
from cmasi import LoiterType
from cmasi import TurnType


class AirVehicleConfiguration(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 3
        self.SERIES_NAME = "CMASI"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 4849604199710720000
        self.SERIES_VERSION = 2

        #Define message fields
        self.VehicleID = 0   #uint32
        self.Label = ""   #string
        self.MinimumSpeed = 0   #real32
        self.MaximumSpeed = 0   #real32
        self.NominalFlightProfile = FlightProfile.FlightProfile()   #FlightProfile
        self.AlternateFlightProfiles = []   #FlightProfile
        self.PayloadConfigurationList = []   #PayloadConfiguration
        self.AvailableLoiterTypes = []   #LoiterType
        self.AvailableTurnTypes = []   #TurnType
        self.MinimumAltitude = 0   #real32
        self.MaximumAltitude = 1000000   #real32
        self.MinAltAboveGround = 0   #real32


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">I", self.VehicleID))
        buffer.append(struct.pack(">H", len(self.Label) ))
        if len(self.Label) > 0:
            buffer.append(struct.pack( `len(self.Label)` + "s", self.Label))
        buffer.append(struct.pack(">f", self.MinimumSpeed))
        buffer.append(struct.pack(">f", self.MaximumSpeed))
        buffer.append(struct.pack("B", self.NominalFlightProfile != None ))
        if self.NominalFlightProfile != None:
            buffer.append(struct.pack(">q", self.NominalFlightProfile.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.NominalFlightProfile.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.NominalFlightProfile.SERIES_VERSION))
            buffer.append(self.NominalFlightProfile.pack())
        buffer.append(struct.pack(">H", len(self.AlternateFlightProfiles) ))
        for x in self.AlternateFlightProfiles:
           buffer.append(struct.pack("B", x != None ))
           if x != None:
               buffer.append(struct.pack(">q", x.SERIES_NAME_ID))
               buffer.append(struct.pack(">I", x.LMCP_TYPE))
               buffer.append(struct.pack(">H", x.SERIES_VERSION))
               buffer.append(x.pack())
        buffer.append(struct.pack(">H", len(self.PayloadConfigurationList) ))
        for x in self.PayloadConfigurationList:
           buffer.append(struct.pack("B", x != None ))
           if x != None:
               buffer.append(struct.pack(">q", x.SERIES_NAME_ID))
               buffer.append(struct.pack(">I", x.LMCP_TYPE))
               buffer.append(struct.pack(">H", x.SERIES_VERSION))
               buffer.append(x.pack())
        buffer.append(struct.pack(">H", len(self.AvailableLoiterTypes) ))
        for x in self.AvailableLoiterTypes:
            buffer.append(struct.pack(">i", x ))
        buffer.append(struct.pack(">H", len(self.AvailableTurnTypes) ))
        for x in self.AvailableTurnTypes:
            buffer.append(struct.pack(">i", x ))
        buffer.append(struct.pack(">f", self.MinimumAltitude))
        buffer.append(struct.pack(">f", self.MaximumAltitude))
        buffer.append(struct.pack(">f", self.MinAltAboveGround))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.VehicleID = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        _strlen = struct.unpack_from(">H", buffer, _pos )[0]
        _pos += 2
        if _strlen > 0:
            self.Label = struct.unpack_from( `_strlen` + "s", buffer, _pos )[0]
            _pos += _strlen
        else:
             self.Label = ""
        self.MinimumSpeed = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.MaximumSpeed = struct.unpack_from(">f", buffer, _pos)[0]
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
            self.NominalFlightProfile = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.NominalFlightProfile.unpack(buffer, _pos)
        else:
            self.NominalFlightProfile = None
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.AlternateFlightProfiles = [None] * _arraylen
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
                self.AlternateFlightProfiles[x] = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
                _pos = self.AlternateFlightProfiles[x].unpack(buffer, _pos)
            else:
                self.AlternateFlightProfiles[x] = None
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.PayloadConfigurationList = [None] * _arraylen
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
                self.PayloadConfigurationList[x] = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
                _pos = self.PayloadConfigurationList[x].unpack(buffer, _pos)
            else:
                self.PayloadConfigurationList[x] = None
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.AvailableLoiterTypes = [None] * _arraylen
        _pos += 2
        if _arraylen > 0:
            self.AvailableLoiterTypes = struct.unpack_from(">" + `_arraylen` + "i", buffer, _pos )
            _pos += 4 * _arraylen
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.AvailableTurnTypes = [None] * _arraylen
        _pos += 2
        if _arraylen > 0:
            self.AvailableTurnTypes = struct.unpack_from(">" + `_arraylen` + "i", buffer, _pos )
            _pos += 4 * _arraylen
        self.MinimumAltitude = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.MaximumAltitude = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.MinAltAboveGround = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        return _pos


    def get_VehicleID(self):
        return self.VehicleID

    def set_VehicleID(self, value):
        self.VehicleID = int( value )

    def get_Label(self):
        return self.Label

    def set_Label(self, value):
        self.Label = str( value )

    def get_MinimumSpeed(self):
        return self.MinimumSpeed

    def set_MinimumSpeed(self, value):
        self.MinimumSpeed = float( value )

    def get_MaximumSpeed(self):
        return self.MaximumSpeed

    def set_MaximumSpeed(self, value):
        self.MaximumSpeed = float( value )

    def get_NominalFlightProfile(self):
        return self.NominalFlightProfile

    def set_NominalFlightProfile(self, value):
        self.NominalFlightProfile = value 

    def get_AlternateFlightProfiles(self):
        return self.AlternateFlightProfiles

    def get_PayloadConfigurationList(self):
        return self.PayloadConfigurationList

    def get_AvailableLoiterTypes(self):
        return self.AvailableLoiterTypes

    def get_AvailableTurnTypes(self):
        return self.AvailableTurnTypes

    def get_MinimumAltitude(self):
        return self.MinimumAltitude

    def set_MinimumAltitude(self, value):
        self.MinimumAltitude = float( value )

    def get_MaximumAltitude(self):
        return self.MaximumAltitude

    def set_MaximumAltitude(self, value):
        self.MaximumAltitude = float( value )

    def get_MinAltAboveGround(self):
        return self.MinAltAboveGround

    def set_MinAltAboveGround(self, value):
        self.MinAltAboveGround = float( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From AirVehicleConfiguration:\n"
        buf +=    "VehicleID = " + str( self.VehicleID ) + "\n" 
        buf +=    "Label = " + str( self.Label ) + "\n" 
        buf +=    "MinimumSpeed = " + str( self.MinimumSpeed ) + "\n" 
        buf +=    "MaximumSpeed = " + str( self.MaximumSpeed ) + "\n" 
        buf +=    "NominalFlightProfile = " + str( self.NominalFlightProfile ) + "\n" 
        buf +=    "AlternateFlightProfiles = " + str( self.AlternateFlightProfiles ) + "\n" 
        buf +=    "PayloadConfigurationList = " + str( self.PayloadConfigurationList ) + "\n" 
        buf +=    "AvailableLoiterTypes = " + str( self.AvailableLoiterTypes ) + "\n" 
        buf +=    "AvailableTurnTypes = " + str( self.AvailableTurnTypes ) + "\n" 
        buf +=    "MinimumAltitude = " + str( self.MinimumAltitude ) + "\n" 
        buf +=    "MaximumAltitude = " + str( self.MaximumAltitude ) + "\n" 
        buf +=    "MinAltAboveGround = " + str( self.MinAltAboveGround ) + "\n" 

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
        str = ws + "<AirVehicleConfiguration>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</AirVehicleConfiguration>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<VehicleID>" + str(self.VehicleID) + "</VehicleID>\n"
        buf += ws + "<Label>" + str(self.Label) + "</Label>\n"
        buf += ws + "<MinimumSpeed>" + str(self.MinimumSpeed) + "</MinimumSpeed>\n"
        buf += ws + "<MaximumSpeed>" + str(self.MaximumSpeed) + "</MaximumSpeed>\n"
        buf += ws + "<NominalFlightProfile>\n"
        if self.NominalFlightProfile == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.NominalFlightProfile.toXMLStr(ws + "    ") 
        buf += ws + "</NominalFlightProfile>\n"
        buf += ws + "<AlternateFlightProfiles>\n"
        for x in self.AlternateFlightProfiles:
            if x == None:
                buf += ws + "    <null/>\n"
            else:
                buf += x.toXMLStr(ws + "    ") 
        buf += ws + "</AlternateFlightProfiles>\n"
        buf += ws + "<PayloadConfigurationList>\n"
        for x in self.PayloadConfigurationList:
            if x == None:
                buf += ws + "    <null/>\n"
            else:
                buf += x.toXMLStr(ws + "    ") 
        buf += ws + "</PayloadConfigurationList>\n"
        buf += ws + "<AvailableLoiterTypes>\n"
        for x in self.AvailableLoiterTypes:
            buf += ws + "<LoiterType>" + LoiterType.get_LoiterType_int(x) + "</LoiterType>\n"
        buf += ws + "</AvailableLoiterTypes>\n"
        buf += ws + "<AvailableTurnTypes>\n"
        for x in self.AvailableTurnTypes:
            buf += ws + "<TurnType>" + TurnType.get_TurnType_int(x) + "</TurnType>\n"
        buf += ws + "</AvailableTurnTypes>\n"
        buf += ws + "<MinimumAltitude>" + str(self.MinimumAltitude) + "</MinimumAltitude>\n"
        buf += ws + "<MaximumAltitude>" + str(self.MaximumAltitude) + "</MaximumAltitude>\n"
        buf += ws + "<MinAltAboveGround>" + str(self.MinAltAboveGround) + "</MinAltAboveGround>\n"

        return buf
        
