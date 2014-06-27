#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *
from vics import EdgePairProbability


class NetworkNode(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 29
        self.SERIES_NAME = "VICS"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6217574784323026944
        self.SERIES_VERSION = 17

        #Define message fields
        self.NodeId = 0   #uint32
        self.InboundEdges = []   #uint32
        self.OutboundEdges = []   #uint32
        self.TurnProbabilities = []   #EdgePairProbability


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">I", self.NodeId))
        buffer.append(struct.pack(">H", len(self.InboundEdges) ))
        for x in self.InboundEdges:
            buffer.append(struct.pack(">I", x ))
        buffer.append(struct.pack(">H", len(self.OutboundEdges) ))
        for x in self.OutboundEdges:
            buffer.append(struct.pack(">I", x ))
        buffer.append(struct.pack(">H", len(self.TurnProbabilities) ))
        for x in self.TurnProbabilities:
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
        self.NodeId = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.InboundEdges = [None] * _arraylen
        _pos += 2
        if _arraylen > 0:
            self.InboundEdges = struct.unpack_from(">" + `_arraylen` + "I", buffer, _pos )
            _pos += 4 * _arraylen
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.OutboundEdges = [None] * _arraylen
        _pos += 2
        if _arraylen > 0:
            self.OutboundEdges = struct.unpack_from(">" + `_arraylen` + "I", buffer, _pos )
            _pos += 4 * _arraylen
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.TurnProbabilities = [None] * _arraylen
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
                self.TurnProbabilities[x] = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
                _pos = self.TurnProbabilities[x].unpack(buffer, _pos)
            else:
                self.TurnProbabilities[x] = None
        return _pos


    def get_NodeId(self):
        return self.NodeId

    def set_NodeId(self, value):
        self.NodeId = int( value )

    def get_InboundEdges(self):
        return self.InboundEdges

    def get_OutboundEdges(self):
        return self.OutboundEdges

    def get_TurnProbabilities(self):
        return self.TurnProbabilities



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From NetworkNode:\n"
        buf +=    "NodeId = " + str( self.NodeId ) + "\n" 
        buf +=    "InboundEdges = " + str( self.InboundEdges ) + "\n" 
        buf +=    "OutboundEdges = " + str( self.OutboundEdges ) + "\n" 
        buf +=    "TurnProbabilities = " + str( self.TurnProbabilities ) + "\n" 

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
        str = ws + "<NetworkNode>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</NetworkNode>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<NodeId>" + str(self.NodeId) + "</NodeId>\n"
        buf += ws + "<InboundEdges>\n"
        for x in self.InboundEdges:
            buf += ws + "<uint32>" + str(x) + "</uint32>\n"
        buf += ws + "</InboundEdges>\n"
        buf += ws + "<OutboundEdges>\n"
        for x in self.OutboundEdges:
            buf += ws + "<uint32>" + str(x) + "</uint32>\n"
        buf += ws + "</OutboundEdges>\n"
        buf += ws + "<TurnProbabilities>\n"
        for x in self.TurnProbabilities:
            if x == None:
                buf += ws + "    <null/>\n"
            else:
                buf += x.toXMLStr(ws + "    ") 
        buf += ws + "</TurnProbabilities>\n"

        return buf
        
