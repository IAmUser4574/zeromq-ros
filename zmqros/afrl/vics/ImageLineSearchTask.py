#! /usr/bin/python

import struct
from lmcp import LMCPObject
#import xml.dom.minidom

#from lmcp import *
from cmasi import LineSearchTask
from vics import LineSearchStrategy


class ImageLineSearchTask(LineSearchTask.LineSearchTask):

    def __init__(self):
        LineSearchTask.LineSearchTask.__init__(self)
        self.LMCP_TYPE = 11
        self.SERIES_NAME = "VICS"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6217574784323026944
        self.SERIES_VERSION = 17

        #Define message fields
        self.SearchStrategy = LineSearchStrategy.LineSearchStrategy.Straight   #LineSearchStrategy
        self.CaptureVideo = True   #bool
        self.UseWingCameraGroundOverlap = True   #bool
        self.WingCameraGroundOverlap = 0   #real32
        self.WingCameraSnapRate = 0   #real32
        self.UseVideoFrameGroundOverlap = True   #bool
        self.VideoFrameGroundOverlap = 0   #real32
        self.VideoFrameSnapRate = 0   #real32


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LineSearchTask.LineSearchTask.pack(self))
        buffer.append(struct.pack(">i", self.SearchStrategy))
        buffer.append(struct.pack(">B", self.CaptureVideo))
        buffer.append(struct.pack(">B", self.UseWingCameraGroundOverlap))
        buffer.append(struct.pack(">f", self.WingCameraGroundOverlap))
        buffer.append(struct.pack(">f", self.WingCameraSnapRate))
        buffer.append(struct.pack(">B", self.UseVideoFrameGroundOverlap))
        buffer.append(struct.pack(">f", self.VideoFrameGroundOverlap))
        buffer.append(struct.pack(">f", self.VideoFrameSnapRate))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LineSearchTask.LineSearchTask.unpack(self, buffer, _pos)
        self.SearchStrategy = struct.unpack_from(">i", buffer, _pos)[0]
        _pos += 4
        self.CaptureVideo = struct.unpack_from(">B", buffer, _pos)[0]
        _pos += 1
        self.UseWingCameraGroundOverlap = struct.unpack_from(">B", buffer, _pos)[0]
        _pos += 1
        self.WingCameraGroundOverlap = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.WingCameraSnapRate = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.UseVideoFrameGroundOverlap = struct.unpack_from(">B", buffer, _pos)[0]
        _pos += 1
        self.VideoFrameGroundOverlap = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.VideoFrameSnapRate = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        return _pos


    def get_SearchStrategy(self):
        return self.SearchStrategy

    def set_SearchStrategy(self, value):
        self.SearchStrategy = value 

    def get_CaptureVideo(self):
        return self.CaptureVideo

    def set_CaptureVideo(self, value):
        self.CaptureVideo = bool( value )

    def get_UseWingCameraGroundOverlap(self):
        return self.UseWingCameraGroundOverlap

    def set_UseWingCameraGroundOverlap(self, value):
        self.UseWingCameraGroundOverlap = bool( value )

    def get_WingCameraGroundOverlap(self):
        return self.WingCameraGroundOverlap

    def set_WingCameraGroundOverlap(self, value):
        self.WingCameraGroundOverlap = float( value )

    def get_WingCameraSnapRate(self):
        return self.WingCameraSnapRate

    def set_WingCameraSnapRate(self, value):
        self.WingCameraSnapRate = float( value )

    def get_UseVideoFrameGroundOverlap(self):
        return self.UseVideoFrameGroundOverlap

    def set_UseVideoFrameGroundOverlap(self, value):
        self.UseVideoFrameGroundOverlap = bool( value )

    def get_VideoFrameGroundOverlap(self):
        return self.VideoFrameGroundOverlap

    def set_VideoFrameGroundOverlap(self, value):
        self.VideoFrameGroundOverlap = float( value )

    def get_VideoFrameSnapRate(self):
        return self.VideoFrameSnapRate

    def set_VideoFrameSnapRate(self, value):
        self.VideoFrameSnapRate = float( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LineSearchTask.LineSearchTask.toString(self)
        buf += "From ImageLineSearchTask:\n"
        buf +=    "SearchStrategy = " + str( self.SearchStrategy ) + "\n" 
        buf +=    "CaptureVideo = " + str( self.CaptureVideo ) + "\n" 
        buf +=    "UseWingCameraGroundOverlap = " + str( self.UseWingCameraGroundOverlap ) + "\n" 
        buf +=    "WingCameraGroundOverlap = " + str( self.WingCameraGroundOverlap ) + "\n" 
        buf +=    "WingCameraSnapRate = " + str( self.WingCameraSnapRate ) + "\n" 
        buf +=    "UseVideoFrameGroundOverlap = " + str( self.UseVideoFrameGroundOverlap ) + "\n" 
        buf +=    "VideoFrameGroundOverlap = " + str( self.VideoFrameGroundOverlap ) + "\n" 
        buf +=    "VideoFrameSnapRate = " + str( self.VideoFrameSnapRate ) + "\n" 

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
        str = ws + "<ImageLineSearchTask>\n";
        #str +=LineSearchTask.LineSearchTask.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</ImageLineSearchTask>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LineSearchTask.LineSearchTask.toXMLMembersStr(self, ws)
        buf += ws + "<SearchStrategy>" + LineSearchStrategy.get_LineSearchStrategy_int(self.SearchStrategy) + "</SearchStrategy>\n"
        buf += ws + "<CaptureVideo>" + str(self.CaptureVideo) + "</CaptureVideo>\n"
        buf += ws + "<UseWingCameraGroundOverlap>" + str(self.UseWingCameraGroundOverlap) + "</UseWingCameraGroundOverlap>\n"
        buf += ws + "<WingCameraGroundOverlap>" + str(self.WingCameraGroundOverlap) + "</WingCameraGroundOverlap>\n"
        buf += ws + "<WingCameraSnapRate>" + str(self.WingCameraSnapRate) + "</WingCameraSnapRate>\n"
        buf += ws + "<UseVideoFrameGroundOverlap>" + str(self.UseVideoFrameGroundOverlap) + "</UseVideoFrameGroundOverlap>\n"
        buf += ws + "<VideoFrameGroundOverlap>" + str(self.VideoFrameGroundOverlap) + "</VideoFrameGroundOverlap>\n"
        buf += ws + "<VideoFrameSnapRate>" + str(self.VideoFrameSnapRate) + "</VideoFrameSnapRate>\n"

        return buf
        
