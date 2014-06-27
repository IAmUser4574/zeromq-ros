import socket
from lmcp import LMCPFactory

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from cmasi import AbstractGeometry
from cmasi import AbstractZone
from cmasi import AirVehicleConfiguration
from cmasi import AirVehicleState
from cmasi import AreaSearchTask
from cmasi import CameraAction
from cmasi import CameraConfiguration
from cmasi import CameraState
from cmasi import Circle
from cmasi import FlightProfile
from cmasi import GimbalAngleAction
from cmasi import GimbalConfiguration
from cmasi import GimbalScanAction
from cmasi import GimbalStareAction
from cmasi import GimbalState
from cmasi import GoToWaypointAction
from cmasi import KeepInZone
from cmasi import KeepOutZone
from cmasi import LineSearchTask
from cmasi import Location2D
from cmasi import Location3D
from cmasi import LoiterAction
from cmasi import LoiterTask
from cmasi import MissionCommand
from cmasi import MustFlyTask
from cmasi import OperatorSignal
from cmasi import PayloadAction
from cmasi import PayloadConfiguration
from cmasi import PayloadState
from cmasi import AutomationRequest
from cmasi import PointSearchTask
from cmasi import Polygon
from cmasi import Rectangle
from cmasi import RemoveTasks
from cmasi import SearchTask
from cmasi import ServiceStatus
from cmasi import SessionStatus
from cmasi import Task
from cmasi import VehicleAction
from cmasi import VehicleActionCommand
from cmasi import VehicleInfo
from cmasi import VideoStreamAction
from cmasi import VideoStreamConfiguration
from cmasi import VideoStreamState
from cmasi import Waypoint
from cmasi import Wedge
from cmasi import AutomationResponse
from cmasi import RemoveZones
from cmasi import RemoveAirVehicles
from cmasi import FlightDirectorAction
from cmasi import KeyValuePair
from cmasi import WeatherReport
from vics import VicsBase
from vics import VicsAck
from vics import PickupMessageTask
from vics import DeliverMessageTask
from vics import CommTransferTask
from vics import PatrolTask
from vics import UgsManagementTask
from vics import SubTaskExecution
from vics import MeetMeTask
from vics import ImageAreaSearchTask
from vics import ImageLineSearchTask
from vics import ImagePointSearchTask
from vics import StateTransition
from vics import DismountMessage
from vics import IntruderAlert
from vics import UgsConfiguration
from vics import UgsStatusRequest
from vics import UgsStatusResponse
from vics import RadarEnableMessage
from vics import HeartbeatMessage
from vics import HeartbeatResponse
from vics import PayloadData
from vics import QueryResponse
from vics import GlobalMessageId
from vics import MessageQuery
from vics import MessageRequest
from vics import LocationXY
from vics import EdgePairProbability
from vics import NetworkNode
from vics import NetworkNodeXY
from vics import NetworkNodeLatLon
from vics import ValueFunction
from vics import PiecewiseConstantUnitLength
from vics import PiecewiseConstantFixedEndPoints
from vics import NetworkEdge
from vics import NetworkRegion
from vics import InitializeEstimator
from vics import NetworkLocation
from vics import UgsReport
from vics import NetworkPropagate
from vics import NetworkUpdate
from vics import CurrentNetworkStatus
from vics import CurrentNetworkUpdate
from vics import LikertNetworkUpdate
from vics import FixedUGS
from vics import UgsLaydown
from vics import IsolationControllerInitialization
from vics import ImmediatelyVisitUgsCommand
from vics import LoiterVisitUgsCommand
from vics import IsolationControllerTerminated
from vics import PayloadPowerState
from vics import ToggleRequest
from vics import ToggleStatus
from vics import WifiConnectionStatus
from vics import AxisSnapshot
from vics import AxisVideoRecord


s = socket.socket()
host = socket.gethostname()
port = 11041
s.connect((host, port))
buf = []

#Pack AbstractGeometry
obj = AbstractGeometry.AbstractGeometry()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack AbstractZone
obj = AbstractZone.AbstractZone()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack AirVehicleConfiguration
obj = AirVehicleConfiguration.AirVehicleConfiguration()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack AirVehicleState
obj = AirVehicleState.AirVehicleState()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack AreaSearchTask
obj = AreaSearchTask.AreaSearchTask()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack CameraAction
obj = CameraAction.CameraAction()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack CameraConfiguration
obj = CameraConfiguration.CameraConfiguration()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack CameraState
obj = CameraState.CameraState()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack Circle
obj = Circle.Circle()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack FlightProfile
obj = FlightProfile.FlightProfile()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack GimbalAngleAction
obj = GimbalAngleAction.GimbalAngleAction()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack GimbalConfiguration
obj = GimbalConfiguration.GimbalConfiguration()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack GimbalScanAction
obj = GimbalScanAction.GimbalScanAction()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack GimbalStareAction
obj = GimbalStareAction.GimbalStareAction()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack GimbalState
obj = GimbalState.GimbalState()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack GoToWaypointAction
obj = GoToWaypointAction.GoToWaypointAction()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack KeepInZone
obj = KeepInZone.KeepInZone()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack KeepOutZone
obj = KeepOutZone.KeepOutZone()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack LineSearchTask
obj = LineSearchTask.LineSearchTask()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack Location2D
obj = Location2D.Location2D()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack Location3D
obj = Location3D.Location3D()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack LoiterAction
obj = LoiterAction.LoiterAction()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack LoiterTask
obj = LoiterTask.LoiterTask()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack MissionCommand
obj = MissionCommand.MissionCommand()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack MustFlyTask
obj = MustFlyTask.MustFlyTask()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack OperatorSignal
obj = OperatorSignal.OperatorSignal()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack PayloadAction
obj = PayloadAction.PayloadAction()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack PayloadConfiguration
obj = PayloadConfiguration.PayloadConfiguration()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack PayloadState
obj = PayloadState.PayloadState()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack AutomationRequest
obj = AutomationRequest.AutomationRequest()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack PointSearchTask
obj = PointSearchTask.PointSearchTask()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack Polygon
obj = Polygon.Polygon()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack Rectangle
obj = Rectangle.Rectangle()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack RemoveTasks
obj = RemoveTasks.RemoveTasks()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack SearchTask
obj = SearchTask.SearchTask()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack ServiceStatus
obj = ServiceStatus.ServiceStatus()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack SessionStatus
obj = SessionStatus.SessionStatus()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack Task
obj = Task.Task()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack VehicleAction
obj = VehicleAction.VehicleAction()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack VehicleActionCommand
obj = VehicleActionCommand.VehicleActionCommand()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack VehicleInfo
obj = VehicleInfo.VehicleInfo()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack VideoStreamAction
obj = VideoStreamAction.VideoStreamAction()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack VideoStreamConfiguration
obj = VideoStreamConfiguration.VideoStreamConfiguration()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack VideoStreamState
obj = VideoStreamState.VideoStreamState()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack Waypoint
obj = Waypoint.Waypoint()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack Wedge
obj = Wedge.Wedge()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack AutomationResponse
obj = AutomationResponse.AutomationResponse()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack RemoveZones
obj = RemoveZones.RemoveZones()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack RemoveAirVehicles
obj = RemoveAirVehicles.RemoveAirVehicles()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack FlightDirectorAction
obj = FlightDirectorAction.FlightDirectorAction()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack KeyValuePair
obj = KeyValuePair.KeyValuePair()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack WeatherReport
obj = WeatherReport.WeatherReport()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack VicsBase
obj = VicsBase.VicsBase()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack VicsAck
obj = VicsAck.VicsAck()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack PickupMessageTask
obj = PickupMessageTask.PickupMessageTask()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack DeliverMessageTask
obj = DeliverMessageTask.DeliverMessageTask()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack CommTransferTask
obj = CommTransferTask.CommTransferTask()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack PatrolTask
obj = PatrolTask.PatrolTask()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack UgsManagementTask
obj = UgsManagementTask.UgsManagementTask()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack SubTaskExecution
obj = SubTaskExecution.SubTaskExecution()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack MeetMeTask
obj = MeetMeTask.MeetMeTask()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack ImageAreaSearchTask
obj = ImageAreaSearchTask.ImageAreaSearchTask()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack ImageLineSearchTask
obj = ImageLineSearchTask.ImageLineSearchTask()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack ImagePointSearchTask
obj = ImagePointSearchTask.ImagePointSearchTask()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack StateTransition
obj = StateTransition.StateTransition()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack DismountMessage
obj = DismountMessage.DismountMessage()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack IntruderAlert
obj = IntruderAlert.IntruderAlert()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack UgsConfiguration
obj = UgsConfiguration.UgsConfiguration()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack UgsStatusRequest
obj = UgsStatusRequest.UgsStatusRequest()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack UgsStatusResponse
obj = UgsStatusResponse.UgsStatusResponse()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack RadarEnableMessage
obj = RadarEnableMessage.RadarEnableMessage()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack HeartbeatMessage
obj = HeartbeatMessage.HeartbeatMessage()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack HeartbeatResponse
obj = HeartbeatResponse.HeartbeatResponse()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack PayloadData
obj = PayloadData.PayloadData()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack QueryResponse
obj = QueryResponse.QueryResponse()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack GlobalMessageId
obj = GlobalMessageId.GlobalMessageId()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack MessageQuery
obj = MessageQuery.MessageQuery()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack MessageRequest
obj = MessageRequest.MessageRequest()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack LocationXY
obj = LocationXY.LocationXY()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack EdgePairProbability
obj = EdgePairProbability.EdgePairProbability()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack NetworkNode
obj = NetworkNode.NetworkNode()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack NetworkNodeXY
obj = NetworkNodeXY.NetworkNodeXY()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack NetworkNodeLatLon
obj = NetworkNodeLatLon.NetworkNodeLatLon()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack ValueFunction
obj = ValueFunction.ValueFunction()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack PiecewiseConstantUnitLength
obj = PiecewiseConstantUnitLength.PiecewiseConstantUnitLength()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack PiecewiseConstantFixedEndPoints
obj = PiecewiseConstantFixedEndPoints.PiecewiseConstantFixedEndPoints()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack NetworkEdge
obj = NetworkEdge.NetworkEdge()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack NetworkRegion
obj = NetworkRegion.NetworkRegion()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack InitializeEstimator
obj = InitializeEstimator.InitializeEstimator()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack NetworkLocation
obj = NetworkLocation.NetworkLocation()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack UgsReport
obj = UgsReport.UgsReport()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack NetworkPropagate
obj = NetworkPropagate.NetworkPropagate()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack NetworkUpdate
obj = NetworkUpdate.NetworkUpdate()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack CurrentNetworkStatus
obj = CurrentNetworkStatus.CurrentNetworkStatus()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack CurrentNetworkUpdate
obj = CurrentNetworkUpdate.CurrentNetworkUpdate()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack LikertNetworkUpdate
obj = LikertNetworkUpdate.LikertNetworkUpdate()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack FixedUGS
obj = FixedUGS.FixedUGS()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack UgsLaydown
obj = UgsLaydown.UgsLaydown()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack IsolationControllerInitialization
obj = IsolationControllerInitialization.IsolationControllerInitialization()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack ImmediatelyVisitUgsCommand
obj = ImmediatelyVisitUgsCommand.ImmediatelyVisitUgsCommand()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack LoiterVisitUgsCommand
obj = LoiterVisitUgsCommand.LoiterVisitUgsCommand()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack IsolationControllerTerminated
obj = IsolationControllerTerminated.IsolationControllerTerminated()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack PayloadPowerState
obj = PayloadPowerState.PayloadPowerState()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack ToggleRequest
obj = ToggleRequest.ToggleRequest()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack ToggleStatus
obj = ToggleStatus.ToggleStatus()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack WifiConnectionStatus
obj = WifiConnectionStatus.WifiConnectionStatus()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack AxisSnapshot
obj = AxisSnapshot.AxisSnapshot()
buf.append(LMCPFactory.packMessage(obj, True))
#Pack AxisVideoRecord
obj = AxisVideoRecord.AxisVideoRecord()
buf.append(LMCPFactory.packMessage(obj, True))


s.send("".join(buf))


