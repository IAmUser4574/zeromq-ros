#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *
from cmasi import LoiterTask


class MeetMeTask(LoiterTask.LoiterTask):

    def __init__(self):
        LoiterTask.LoiterTask.__init__(self)
        self.LMCP_TYPE = 9
        self.SERIES_NAME = "VICS"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6217574784323026944
        self.SERIES_VERSION = 17

        #Define message fields
        self.RendezvousTime = 0   #uint32


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LoiterTask.LoiterTask.pack(self))
        buffer.append(struct.pack(">I", self.RendezvousTime))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LoiterTask.LoiterTask.unpack(self, buffer, _pos)
        self.RendezvousTime = struct.unpack_from(">I", buffer, _pos)[0]
        _pos += 4
        return _pos


    def get_RendezvousTime(self):
        return self.RendezvousTime

    def set_RendezvousTime(self, value):
        self.RendezvousTime = int( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LoiterTask.LoiterTask.toString(self)
        buf += "From MeetMeTask:\n"
        buf +=    "RendezvousTime = " + str( self.RendezvousTime ) + "\n" 

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
        str = ws + "<MeetMeTask>\n";
        #str +=LoiterTask.LoiterTask.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</MeetMeTask>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LoiterTask.LoiterTask.toXMLMembersStr(self, ws)
        buf += ws + "<RendezvousTime>" + str(self.RendezvousTime) + "</RendezvousTime>\n"

        return buf
        
