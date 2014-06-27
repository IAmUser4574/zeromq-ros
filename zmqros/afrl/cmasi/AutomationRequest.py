#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *
from cmasi import VehicleInfo


class AutomationRequest(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 30
        self.SERIES_NAME = "CMASI"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 4849604199710720000
        self.SERIES_VERSION = 2

        #Define message fields
        self.VehicleList = []   #VehicleInfo
        self.TaskList = []   #uint32
        self.TaskRelationships = ""   #string
        self.KeepOutZoneList = []   #uint32
        self.KeepInZoneList = []   #uint32
        self.RedoAllTasks = False   #bool


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">H", len(self.VehicleList) ))
        for x in self.VehicleList:
           buffer.append(struct.pack("B", x != None ))
           if x != None:
               buffer.append(struct.pack(">q", x.SERIES_NAME_ID))
               buffer.append(struct.pack(">I", x.LMCP_TYPE))
               buffer.append(struct.pack(">H", x.SERIES_VERSION))
               buffer.append(x.pack())
        buffer.append(struct.pack(">H", len(self.TaskList) ))
        for x in self.TaskList:
            buffer.append(struct.pack(">I", x ))
        buffer.append(struct.pack(">H", len(self.TaskRelationships) ))
        if len(self.TaskRelationships) > 0:
            buffer.append(struct.pack( `len(self.TaskRelationships)` + "s", self.TaskRelationships))
        buffer.append(struct.pack(">H", len(self.KeepOutZoneList) ))
        for x in self.KeepOutZoneList:
            buffer.append(struct.pack(">I", x ))
        buffer.append(struct.pack(">H", len(self.KeepInZoneList) ))
        for x in self.KeepInZoneList:
            buffer.append(struct.pack(">I", x ))
        buffer.append(struct.pack(">B", self.RedoAllTasks))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.VehicleList = [None] * _arraylen
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
                self.VehicleList[x] = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
                _pos = self.VehicleList[x].unpack(buffer, _pos)
            else:
                self.VehicleList[x] = None
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.TaskList = [None] * _arraylen
        _pos += 2
        if _arraylen > 0:
            self.TaskList = struct.unpack_from(">" + `_arraylen` + "I", buffer, _pos )
            _pos += 4 * _arraylen
        _strlen = struct.unpack_from(">H", buffer, _pos )[0]
        _pos += 2
        if _strlen > 0:
            self.TaskRelationships = struct.unpack_from( `_strlen` + "s", buffer, _pos )[0]
            _pos += _strlen
        else:
             self.TaskRelationships = ""
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.KeepOutZoneList = [None] * _arraylen
        _pos += 2
        if _arraylen > 0:
            self.KeepOutZoneList = struct.unpack_from(">" + `_arraylen` + "I", buffer, _pos )
            _pos += 4 * _arraylen
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.KeepInZoneList = [None] * _arraylen
        _pos += 2
        if _arraylen > 0:
            self.KeepInZoneList = struct.unpack_from(">" + `_arraylen` + "I", buffer, _pos )
            _pos += 4 * _arraylen
        self.RedoAllTasks = struct.unpack_from(">B", buffer, _pos)[0]
        _pos += 1
        return _pos


    def get_VehicleList(self):
        return self.VehicleList

    def get_TaskList(self):
        return self.TaskList

    def get_TaskRelationships(self):
        return self.TaskRelationships

    def set_TaskRelationships(self, value):
        self.TaskRelationships = str( value )

    def get_KeepOutZoneList(self):
        return self.KeepOutZoneList

    def get_KeepInZoneList(self):
        return self.KeepInZoneList

    def get_RedoAllTasks(self):
        return self.RedoAllTasks

    def set_RedoAllTasks(self, value):
        self.RedoAllTasks = bool( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From AutomationRequest:\n"
        buf +=    "VehicleList = " + str( self.VehicleList ) + "\n" 
        buf +=    "TaskList = " + str( self.TaskList ) + "\n" 
        buf +=    "TaskRelationships = " + str( self.TaskRelationships ) + "\n" 
        buf +=    "KeepOutZoneList = " + str( self.KeepOutZoneList ) + "\n" 
        buf +=    "KeepInZoneList = " + str( self.KeepInZoneList ) + "\n" 
        buf +=    "RedoAllTasks = " + str( self.RedoAllTasks ) + "\n" 

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
        str = ws + "<AutomationRequest>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</AutomationRequest>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<VehicleList>\n"
        for x in self.VehicleList:
            if x == None:
                buf += ws + "    <null/>\n"
            else:
                buf += x.toXMLStr(ws + "    ") 
        buf += ws + "</VehicleList>\n"
        buf += ws + "<TaskList>\n"
        for x in self.TaskList:
            buf += ws + "<uint32>" + str(x) + "</uint32>\n"
        buf += ws + "</TaskList>\n"
        buf += ws + "<TaskRelationships>" + str(self.TaskRelationships) + "</TaskRelationships>\n"
        buf += ws + "<KeepOutZoneList>\n"
        for x in self.KeepOutZoneList:
            buf += ws + "<uint32>" + str(x) + "</uint32>\n"
        buf += ws + "</KeepOutZoneList>\n"
        buf += ws + "<KeepInZoneList>\n"
        for x in self.KeepInZoneList:
            buf += ws + "<uint32>" + str(x) + "</uint32>\n"
        buf += ws + "</KeepInZoneList>\n"
        buf += ws + "<RedoAllTasks>" + str(self.RedoAllTasks) + "</RedoAllTasks>\n"

        return buf
        
