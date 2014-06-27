from lmcp.LMCPObject import *

import AbstractGeometry
import AbstractZone
import AirVehicleConfiguration
import AirVehicleState
import AreaSearchTask
import CameraAction
import CameraConfiguration
import CameraState
import Circle
import FlightProfile
import GimbalAngleAction
import GimbalConfiguration
import GimbalScanAction
import GimbalStareAction
import GimbalState
import GoToWaypointAction
import KeepInZone
import KeepOutZone
import LineSearchTask
import Location2D
import Location3D
import LoiterAction
import LoiterTask
import MissionCommand
import MustFlyTask
import OperatorSignal
import PayloadAction
import PayloadConfiguration
import PayloadState
import AutomationRequest
import PointSearchTask
import Polygon
import Rectangle
import RemoveTasks
import SearchTask
import ServiceStatus
import SessionStatus
import Task
import VehicleAction
import VehicleActionCommand
import VehicleInfo
import VideoStreamAction
import VideoStreamConfiguration
import VideoStreamState
import Waypoint
import Wedge
import AutomationResponse
import RemoveZones
import RemoveAirVehicles
import FlightDirectorAction
import KeyValuePair
import WeatherReport


SERIES_NAME = "CMASI"
#Series Name turned into a long for quick comparisons.
SERIES_NAME_ID = 4849604199710720000
SERIES_VERSION = 2


class SeriesEnum:

    def getName(self, type):
        if(type ==  1): return "AbstractGeometry"
        if(type ==  2): return "AbstractZone"
        if(type ==  3): return "AirVehicleConfiguration"
        if(type ==  4): return "AirVehicleState"
        if(type ==  5): return "AreaSearchTask"
        if(type ==  6): return "CameraAction"
        if(type ==  7): return "CameraConfiguration"
        if(type ==  8): return "CameraState"
        if(type ==  9): return "Circle"
        if(type ==  10): return "FlightProfile"
        if(type ==  11): return "GimbalAngleAction"
        if(type ==  12): return "GimbalConfiguration"
        if(type ==  13): return "GimbalScanAction"
        if(type ==  14): return "GimbalStareAction"
        if(type ==  15): return "GimbalState"
        if(type ==  16): return "GoToWaypointAction"
        if(type ==  17): return "KeepInZone"
        if(type ==  18): return "KeepOutZone"
        if(type ==  19): return "LineSearchTask"
        if(type ==  20): return "Location2D"
        if(type ==  21): return "Location3D"
        if(type ==  22): return "LoiterAction"
        if(type ==  23): return "LoiterTask"
        if(type ==  24): return "MissionCommand"
        if(type ==  25): return "MustFlyTask"
        if(type ==  26): return "OperatorSignal"
        if(type ==  27): return "PayloadAction"
        if(type ==  28): return "PayloadConfiguration"
        if(type ==  29): return "PayloadState"
        if(type ==  30): return "AutomationRequest"
        if(type ==  31): return "PointSearchTask"
        if(type ==  32): return "Polygon"
        if(type ==  33): return "Rectangle"
        if(type ==  34): return "RemoveTasks"
        if(type ==  35): return "SearchTask"
        if(type ==  36): return "ServiceStatus"
        if(type ==  37): return "SessionStatus"
        if(type ==  38): return "Task"
        if(type ==  39): return "VehicleAction"
        if(type ==  40): return "VehicleActionCommand"
        if(type ==  41): return "VehicleInfo"
        if(type ==  42): return "VideoStreamAction"
        if(type ==  43): return "VideoStreamConfiguration"
        if(type ==  44): return "VideoStreamState"
        if(type ==  45): return "Waypoint"
        if(type ==  46): return "Wedge"
        if(type ==  47): return "AutomationResponse"
        if(type ==  48): return "RemoveZones"
        if(type ==  49): return "RemoveAirVehicles"
        if(type ==  50): return "FlightDirectorAction"
        if(type ==  51): return "KeyValuePair"
        if(type ==  52): return "WeatherReport"


    def getType(self, name):
        if ( name == "AbstractGeometry"): return 1
        if ( name == "AbstractZone"): return 2
        if ( name == "AirVehicleConfiguration"): return 3
        if ( name == "AirVehicleState"): return 4
        if ( name == "AreaSearchTask"): return 5
        if ( name == "CameraAction"): return 6
        if ( name == "CameraConfiguration"): return 7
        if ( name == "CameraState"): return 8
        if ( name == "Circle"): return 9
        if ( name == "FlightProfile"): return 10
        if ( name == "GimbalAngleAction"): return 11
        if ( name == "GimbalConfiguration"): return 12
        if ( name == "GimbalScanAction"): return 13
        if ( name == "GimbalStareAction"): return 14
        if ( name == "GimbalState"): return 15
        if ( name == "GoToWaypointAction"): return 16
        if ( name == "KeepInZone"): return 17
        if ( name == "KeepOutZone"): return 18
        if ( name == "LineSearchTask"): return 19
        if ( name == "Location2D"): return 20
        if ( name == "Location3D"): return 21
        if ( name == "LoiterAction"): return 22
        if ( name == "LoiterTask"): return 23
        if ( name == "MissionCommand"): return 24
        if ( name == "MustFlyTask"): return 25
        if ( name == "OperatorSignal"): return 26
        if ( name == "PayloadAction"): return 27
        if ( name == "PayloadConfiguration"): return 28
        if ( name == "PayloadState"): return 29
        if ( name == "AutomationRequest"): return 30
        if ( name == "PointSearchTask"): return 31
        if ( name == "Polygon"): return 32
        if ( name == "Rectangle"): return 33
        if ( name == "RemoveTasks"): return 34
        if ( name == "SearchTask"): return 35
        if ( name == "ServiceStatus"): return 36
        if ( name == "SessionStatus"): return 37
        if ( name == "Task"): return 38
        if ( name == "VehicleAction"): return 39
        if ( name == "VehicleActionCommand"): return 40
        if ( name == "VehicleInfo"): return 41
        if ( name == "VideoStreamAction"): return 42
        if ( name == "VideoStreamConfiguration"): return 43
        if ( name == "VideoStreamState"): return 44
        if ( name == "Waypoint"): return 45
        if ( name == "Wedge"): return 46
        if ( name == "AutomationResponse"): return 47
        if ( name == "RemoveZones"): return 48
        if ( name == "RemoveAirVehicles"): return 49
        if ( name == "FlightDirectorAction"): return 50
        if ( name == "KeyValuePair"): return 51
        if ( name == "WeatherReport"): return 52

        return -1

    def getInstance(self, type):
        if(type ==  1): return AbstractGeometry.AbstractGeometry()
        if(type ==  2): return AbstractZone.AbstractZone()
        if(type ==  3): return AirVehicleConfiguration.AirVehicleConfiguration()
        if(type ==  4): return AirVehicleState.AirVehicleState()
        if(type ==  5): return AreaSearchTask.AreaSearchTask()
        if(type ==  6): return CameraAction.CameraAction()
        if(type ==  7): return CameraConfiguration.CameraConfiguration()
        if(type ==  8): return CameraState.CameraState()
        if(type ==  9): return Circle.Circle()
        if(type ==  10): return FlightProfile.FlightProfile()
        if(type ==  11): return GimbalAngleAction.GimbalAngleAction()
        if(type ==  12): return GimbalConfiguration.GimbalConfiguration()
        if(type ==  13): return GimbalScanAction.GimbalScanAction()
        if(type ==  14): return GimbalStareAction.GimbalStareAction()
        if(type ==  15): return GimbalState.GimbalState()
        if(type ==  16): return GoToWaypointAction.GoToWaypointAction()
        if(type ==  17): return KeepInZone.KeepInZone()
        if(type ==  18): return KeepOutZone.KeepOutZone()
        if(type ==  19): return LineSearchTask.LineSearchTask()
        if(type ==  20): return Location2D.Location2D()
        if(type ==  21): return Location3D.Location3D()
        if(type ==  22): return LoiterAction.LoiterAction()
        if(type ==  23): return LoiterTask.LoiterTask()
        if(type ==  24): return MissionCommand.MissionCommand()
        if(type ==  25): return MustFlyTask.MustFlyTask()
        if(type ==  26): return OperatorSignal.OperatorSignal()
        if(type ==  27): return PayloadAction.PayloadAction()
        if(type ==  28): return PayloadConfiguration.PayloadConfiguration()
        if(type ==  29): return PayloadState.PayloadState()
        if(type ==  30): return AutomationRequest.AutomationRequest()
        if(type ==  31): return PointSearchTask.PointSearchTask()
        if(type ==  32): return Polygon.Polygon()
        if(type ==  33): return Rectangle.Rectangle()
        if(type ==  34): return RemoveTasks.RemoveTasks()
        if(type ==  35): return SearchTask.SearchTask()
        if(type ==  36): return ServiceStatus.ServiceStatus()
        if(type ==  37): return SessionStatus.SessionStatus()
        if(type ==  38): return Task.Task()
        if(type ==  39): return VehicleAction.VehicleAction()
        if(type ==  40): return VehicleActionCommand.VehicleActionCommand()
        if(type ==  41): return VehicleInfo.VehicleInfo()
        if(type ==  42): return VideoStreamAction.VideoStreamAction()
        if(type ==  43): return VideoStreamConfiguration.VideoStreamConfiguration()
        if(type ==  44): return VideoStreamState.VideoStreamState()
        if(type ==  45): return Waypoint.Waypoint()
        if(type ==  46): return Wedge.Wedge()
        if(type ==  47): return AutomationResponse.AutomationResponse()
        if(type ==  48): return RemoveZones.RemoveZones()
        if(type ==  49): return RemoveAirVehicles.RemoveAirVehicles()
        if(type ==  50): return FlightDirectorAction.FlightDirectorAction()
        if(type ==  51): return KeyValuePair.KeyValuePair()
        if(type ==  52): return WeatherReport.WeatherReport()

        return None
