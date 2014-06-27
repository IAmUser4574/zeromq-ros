#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *
from vics import VicsBase
from vics import FuzzyEdgeValue


class LikertNetworkUpdate(VicsBase.VicsBase):

    def __init__(self):
        VicsBase.VicsBase.__init__(self)
        self.LMCP_TYPE = 44
        self.SERIES_NAME = "VICS"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6217574784323026944
        self.SERIES_VERSION = 17

        #Define message fields
        self.AffectedEdgeIds = []   #uint32
        self.LikertValue = FuzzyEdgeValue.FuzzyEdgeValue.Neutral   #FuzzyEdgeValue


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(VicsBase.VicsBase.pack(self))
        buffer.append(struct.pack(">H", len(self.AffectedEdgeIds) ))
        for x in self.AffectedEdgeIds:
            buffer.append(struct.pack(">I", x ))
        buffer.append(struct.pack(">i", self.LikertValue))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = VicsBase.VicsBase.unpack(self, buffer, _pos)
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.AffectedEdgeIds = [None] * _arraylen
        _pos += 2
        if _arraylen > 0:
            self.AffectedEdgeIds = struct.unpack_from(">" + `_arraylen` + "I", buffer, _pos )
            _pos += 4 * _arraylen
        self.LikertValue = struct.unpack_from(">i", buffer, _pos)[0]
        _pos += 4
        return _pos


    def get_AffectedEdgeIds(self):
        return self.AffectedEdgeIds

    def get_LikertValue(self):
        return self.LikertValue

    def set_LikertValue(self, value):
        self.LikertValue = value 



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = VicsBase.VicsBase.toString(self)
        buf += "From LikertNetworkUpdate:\n"
        buf +=    "AffectedEdgeIds = " + str( self.AffectedEdgeIds ) + "\n" 
        buf +=    "LikertValue = " + str( self.LikertValue ) + "\n" 

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
        str = ws + "<LikertNetworkUpdate>\n";
        #str +=VicsBase.VicsBase.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</LikertNetworkUpdate>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += VicsBase.VicsBase.toXMLMembersStr(self, ws)
        buf += ws + "<AffectedEdgeIds>\n"
        for x in self.AffectedEdgeIds:
            buf += ws + "<uint32>" + str(x) + "</uint32>\n"
        buf += ws + "</AffectedEdgeIds>\n"
        buf += ws + "<LikertValue>" + FuzzyEdgeValue.get_FuzzyEdgeValue_int(self.LikertValue) + "</LikertValue>\n"

        return buf
        
