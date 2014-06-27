#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *
from vics import PayloadPowerItem


class PayloadPowerState(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 51
        self.SERIES_NAME = "VICS"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6217574784323026944
        self.SERIES_VERSION = 17

        #Define message fields
        self.PayloadItem = PayloadPowerItem.PayloadPowerItem.WiFi   #PayloadPowerItem
        self.PowerState = bool(0)   #bool


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">i", self.PayloadItem))
        buffer.append(struct.pack(">B", self.PowerState))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.PayloadItem = struct.unpack_from(">i", buffer, _pos)[0]
        _pos += 4
        self.PowerState = struct.unpack_from(">B", buffer, _pos)[0]
        _pos += 1
        return _pos


    def get_PayloadItem(self):
        return self.PayloadItem

    def set_PayloadItem(self, value):
        self.PayloadItem = value 

    def get_PowerState(self):
        return self.PowerState

    def set_PowerState(self, value):
        self.PowerState = bool( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From PayloadPowerState:\n"
        buf +=    "PayloadItem = " + str( self.PayloadItem ) + "\n" 
        buf +=    "PowerState = " + str( self.PowerState ) + "\n" 

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
        str = ws + "<PayloadPowerState>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</PayloadPowerState>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<PayloadItem>" + PayloadPowerItem.get_PayloadPowerItem_int(self.PayloadItem) + "</PayloadItem>\n"
        buf += ws + "<PowerState>" + str(self.PowerState) + "</PowerState>\n"

        return buf
        
