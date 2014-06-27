#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *
from vics import IsolationTerminationReason


class IsolationControllerTerminated(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 50
        self.SERIES_NAME = "VICS"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6217574784323026944
        self.SERIES_VERSION = 17

        #Define message fields
        self.Reason = IsolationTerminationReason.IsolationTerminationReason.FalseAlarm   #IsolationTerminationReason


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">i", self.Reason))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.Reason = struct.unpack_from(">i", buffer, _pos)[0]
        _pos += 4
        return _pos


    def get_Reason(self):
        return self.Reason

    def set_Reason(self, value):
        self.Reason = value 



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From IsolationControllerTerminated:\n"
        buf +=    "Reason = " + str( self.Reason ) + "\n" 

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
        str = ws + "<IsolationControllerTerminated>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</IsolationControllerTerminated>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<Reason>" + IsolationTerminationReason.get_IsolationTerminationReason_int(self.Reason) + "</Reason>\n"

        return buf
        
