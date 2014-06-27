#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *
from vics import NetworkNode
from vics import NetworkEdge


class NetworkRegion(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 36
        self.SERIES_NAME = "VICS"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6217574784323026944
        self.SERIES_VERSION = 17

        #Define message fields
        self.RegionId = 0   #uint32
        self.NodeList = []   #NetworkNode
        self.EdgeList = []   #NetworkEdge
        self.ExitProbability = 0.0   #real32


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">I", self.RegionId))
        buffer.append(struct.pack(">H", len(self.NodeList) ))
        for x in self.NodeList:
           buffer.append(struct.pack("B", x != None ))
           if x != None:
               buffer.append(struct.pack(">q", x.SERIES_NAME_ID))
               buffer.append(struct.pack(">I", x.LMCP_TYPE))
               buffer.append(struct.pack(">H", x.SERIES_VERSION))
               buffer.append(x.pack())
        buffer.append(struct.pack(">H", len(self.EdgeList) ))
        for x in self.EdgeList:
           buffer.append(struct.pack("B", x != None ))
           if x != None:
               buffer.append(struct.pack(">q", x.SERIES_NAME_ID))
               buffer.append(struct.pack(">I", x.LMCP_TYPE))
               buffer.append(struct.pack(">H", x.SERIES_VERSION))
               buffer.append(x.pack())
        buffer.append(struct.pack(">f", self.ExitProbability))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.RegionId = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.NodeList = [None] * _arraylen
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
                self.NodeList[x] = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
                _pos = self.NodeList[x].unpack(buffer, _pos)
            else:
                self.NodeList[x] = None
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.EdgeList = [None] * _arraylen
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
                self.EdgeList[x] = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
                _pos = self.EdgeList[x].unpack(buffer, _pos)
            else:
                self.EdgeList[x] = None
        self.ExitProbability = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        return _pos


    def get_RegionId(self):
        return self.RegionId

    def set_RegionId(self, value):
        self.RegionId = int( value )

    def get_NodeList(self):
        return self.NodeList

    def get_EdgeList(self):
        return self.EdgeList

    def get_ExitProbability(self):
        return self.ExitProbability

    def set_ExitProbability(self, value):
        self.ExitProbability = float( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From NetworkRegion:\n"
        buf +=    "RegionId = " + str( self.RegionId ) + "\n" 
        buf +=    "NodeList = " + str( self.NodeList ) + "\n" 
        buf +=    "EdgeList = " + str( self.EdgeList ) + "\n" 
        buf +=    "ExitProbability = " + str( self.ExitProbability ) + "\n" 

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
        str = ws + "<NetworkRegion>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</NetworkRegion>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<RegionId>" + str(self.RegionId) + "</RegionId>\n"
        buf += ws + "<NodeList>\n"
        for x in self.NodeList:
            if x == None:
                buf += ws + "    <null/>\n"
            else:
                buf += x.toXMLStr(ws + "    ") 
        buf += ws + "</NodeList>\n"
        buf += ws + "<EdgeList>\n"
        for x in self.EdgeList:
            if x == None:
                buf += ws + "    <null/>\n"
            else:
                buf += x.toXMLStr(ws + "    ") 
        buf += ws + "</EdgeList>\n"
        buf += ws + "<ExitProbability>" + str(self.ExitProbability) + "</ExitProbability>\n"

        return buf
        
