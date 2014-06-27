#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *
from vics import ValueFunction


class PiecewiseConstantFixedEndPoints(ValueFunction.ValueFunction):

    def __init__(self):
        ValueFunction.ValueFunction.__init__(self)
        self.LMCP_TYPE = 34
        self.SERIES_NAME = "VICS"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6217574784323026944
        self.SERIES_VERSION = 17

        #Define message fields
        self.StartPoint = 0.0   #real32
        self.EndPoint = 0.0   #real32
        self.DomainDiscretization = []   #real32
        self.Value = []   #real32


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(ValueFunction.ValueFunction.pack(self))
        buffer.append(struct.pack(">f", self.StartPoint))
        buffer.append(struct.pack(">f", self.EndPoint))
        buffer.append(struct.pack(">H", len(self.DomainDiscretization) ))
        for x in self.DomainDiscretization:
            buffer.append(struct.pack(">f", x ))
        buffer.append(struct.pack(">H", len(self.Value) ))
        for x in self.Value:
            buffer.append(struct.pack(">f", x ))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = ValueFunction.ValueFunction.unpack(self, buffer, _pos)
        self.StartPoint = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.EndPoint = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.DomainDiscretization = [None] * _arraylen
        _pos += 2
        if _arraylen > 0:
            self.DomainDiscretization = struct.unpack_from(">" + `_arraylen` + "f", buffer, _pos )
            _pos += 4 * _arraylen
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.Value = [None] * _arraylen
        _pos += 2
        if _arraylen > 0:
            self.Value = struct.unpack_from(">" + `_arraylen` + "f", buffer, _pos )
            _pos += 4 * _arraylen
        return _pos


    def get_StartPoint(self):
        return self.StartPoint

    def set_StartPoint(self, value):
        self.StartPoint = float( value )

    def get_EndPoint(self):
        return self.EndPoint

    def set_EndPoint(self, value):
        self.EndPoint = float( value )

    def get_DomainDiscretization(self):
        return self.DomainDiscretization

    def get_Value(self):
        return self.Value



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = ValueFunction.ValueFunction.toString(self)
        buf += "From PiecewiseConstantFixedEndPoints:\n"
        buf +=    "StartPoint = " + str( self.StartPoint ) + "\n" 
        buf +=    "EndPoint = " + str( self.EndPoint ) + "\n" 
        buf +=    "DomainDiscretization = " + str( self.DomainDiscretization ) + "\n" 
        buf +=    "Value = " + str( self.Value ) + "\n" 

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
        str = ws + "<PiecewiseConstantFixedEndPoints>\n";
        #str +=ValueFunction.ValueFunction.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</PiecewiseConstantFixedEndPoints>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += ValueFunction.ValueFunction.toXMLMembersStr(self, ws)
        buf += ws + "<StartPoint>" + str(self.StartPoint) + "</StartPoint>\n"
        buf += ws + "<EndPoint>" + str(self.EndPoint) + "</EndPoint>\n"
        buf += ws + "<DomainDiscretization>\n"
        for x in self.DomainDiscretization:
            buf += ws + "<real32>" + str(x) + "</real32>\n"
        buf += ws + "</DomainDiscretization>\n"
        buf += ws + "<Value>\n"
        for x in self.Value:
            buf += ws + "<real32>" + str(x) + "</real32>\n"
        buf += ws + "</Value>\n"

        return buf
        
