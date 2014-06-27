from lmcp.LMCPObject import *

import VicsBase
import VicsAck
import PickupMessageTask
import DeliverMessageTask
import CommTransferTask
import PatrolTask
import UgsManagementTask
import SubTaskExecution
import MeetMeTask
import ImageAreaSearchTask
import ImageLineSearchTask
import ImagePointSearchTask
import StateTransition
import DismountMessage
import IntruderAlert
import UgsConfiguration
import UgsStatusRequest
import UgsStatusResponse
import RadarEnableMessage
import HeartbeatMessage
import HeartbeatResponse
import PayloadData
import QueryResponse
import GlobalMessageId
import MessageQuery
import MessageRequest
import LocationXY
import EdgePairProbability
import NetworkNode
import NetworkNodeXY
import NetworkNodeLatLon
import ValueFunction
import PiecewiseConstantUnitLength
import PiecewiseConstantFixedEndPoints
import NetworkEdge
import NetworkRegion
import InitializeEstimator
import NetworkLocation
import UgsReport
import NetworkPropagate
import NetworkUpdate
import CurrentNetworkStatus
import CurrentNetworkUpdate
import LikertNetworkUpdate
import FixedUGS
import UgsLaydown
import IsolationControllerInitialization
import ImmediatelyVisitUgsCommand
import LoiterVisitUgsCommand
import IsolationControllerTerminated
import PayloadPowerState
import ToggleRequest
import ToggleStatus
import WifiConnectionStatus
import AxisSnapshot
import AxisVideoRecord


SERIES_NAME = "VICS"
#Series Name turned into a long for quick comparisons.
SERIES_NAME_ID = 6217574784323026944
SERIES_VERSION = 17


class SeriesEnum:

    def getName(self, type):
        if(type ==  1): return "VicsBase"
        if(type ==  2): return "VicsAck"
        if(type ==  3): return "PickupMessageTask"
        if(type ==  4): return "DeliverMessageTask"
        if(type ==  5): return "CommTransferTask"
        if(type ==  6): return "PatrolTask"
        if(type ==  7): return "UgsManagementTask"
        if(type ==  8): return "SubTaskExecution"
        if(type ==  9): return "MeetMeTask"
        if(type ==  10): return "ImageAreaSearchTask"
        if(type ==  11): return "ImageLineSearchTask"
        if(type ==  12): return "ImagePointSearchTask"
        if(type ==  13): return "StateTransition"
        if(type ==  14): return "DismountMessage"
        if(type ==  15): return "IntruderAlert"
        if(type ==  16): return "UgsConfiguration"
        if(type ==  17): return "UgsStatusRequest"
        if(type ==  18): return "UgsStatusResponse"
        if(type ==  19): return "RadarEnableMessage"
        if(type ==  20): return "HeartbeatMessage"
        if(type ==  21): return "HeartbeatResponse"
        if(type ==  22): return "PayloadData"
        if(type ==  23): return "QueryResponse"
        if(type ==  24): return "GlobalMessageId"
        if(type ==  25): return "MessageQuery"
        if(type ==  26): return "MessageRequest"
        if(type ==  27): return "LocationXY"
        if(type ==  28): return "EdgePairProbability"
        if(type ==  29): return "NetworkNode"
        if(type ==  30): return "NetworkNodeXY"
        if(type ==  31): return "NetworkNodeLatLon"
        if(type ==  32): return "ValueFunction"
        if(type ==  33): return "PiecewiseConstantUnitLength"
        if(type ==  34): return "PiecewiseConstantFixedEndPoints"
        if(type ==  35): return "NetworkEdge"
        if(type ==  36): return "NetworkRegion"
        if(type ==  37): return "InitializeEstimator"
        if(type ==  38): return "NetworkLocation"
        if(type ==  39): return "UgsReport"
        if(type ==  40): return "NetworkPropagate"
        if(type ==  41): return "NetworkUpdate"
        if(type ==  42): return "CurrentNetworkStatus"
        if(type ==  43): return "CurrentNetworkUpdate"
        if(type ==  44): return "LikertNetworkUpdate"
        if(type ==  45): return "FixedUGS"
        if(type ==  46): return "UgsLaydown"
        if(type ==  47): return "IsolationControllerInitialization"
        if(type ==  48): return "ImmediatelyVisitUgsCommand"
        if(type ==  49): return "LoiterVisitUgsCommand"
        if(type ==  50): return "IsolationControllerTerminated"
        if(type ==  51): return "PayloadPowerState"
        if(type ==  52): return "ToggleRequest"
        if(type ==  53): return "ToggleStatus"
        if(type ==  54): return "WifiConnectionStatus"
        if(type ==  55): return "AxisSnapshot"
        if(type ==  56): return "AxisVideoRecord"


    def getType(self, name):
        if ( name == "VicsBase"): return 1
        if ( name == "VicsAck"): return 2
        if ( name == "PickupMessageTask"): return 3
        if ( name == "DeliverMessageTask"): return 4
        if ( name == "CommTransferTask"): return 5
        if ( name == "PatrolTask"): return 6
        if ( name == "UgsManagementTask"): return 7
        if ( name == "SubTaskExecution"): return 8
        if ( name == "MeetMeTask"): return 9
        if ( name == "ImageAreaSearchTask"): return 10
        if ( name == "ImageLineSearchTask"): return 11
        if ( name == "ImagePointSearchTask"): return 12
        if ( name == "StateTransition"): return 13
        if ( name == "DismountMessage"): return 14
        if ( name == "IntruderAlert"): return 15
        if ( name == "UgsConfiguration"): return 16
        if ( name == "UgsStatusRequest"): return 17
        if ( name == "UgsStatusResponse"): return 18
        if ( name == "RadarEnableMessage"): return 19
        if ( name == "HeartbeatMessage"): return 20
        if ( name == "HeartbeatResponse"): return 21
        if ( name == "PayloadData"): return 22
        if ( name == "QueryResponse"): return 23
        if ( name == "GlobalMessageId"): return 24
        if ( name == "MessageQuery"): return 25
        if ( name == "MessageRequest"): return 26
        if ( name == "LocationXY"): return 27
        if ( name == "EdgePairProbability"): return 28
        if ( name == "NetworkNode"): return 29
        if ( name == "NetworkNodeXY"): return 30
        if ( name == "NetworkNodeLatLon"): return 31
        if ( name == "ValueFunction"): return 32
        if ( name == "PiecewiseConstantUnitLength"): return 33
        if ( name == "PiecewiseConstantFixedEndPoints"): return 34
        if ( name == "NetworkEdge"): return 35
        if ( name == "NetworkRegion"): return 36
        if ( name == "InitializeEstimator"): return 37
        if ( name == "NetworkLocation"): return 38
        if ( name == "UgsReport"): return 39
        if ( name == "NetworkPropagate"): return 40
        if ( name == "NetworkUpdate"): return 41
        if ( name == "CurrentNetworkStatus"): return 42
        if ( name == "CurrentNetworkUpdate"): return 43
        if ( name == "LikertNetworkUpdate"): return 44
        if ( name == "FixedUGS"): return 45
        if ( name == "UgsLaydown"): return 46
        if ( name == "IsolationControllerInitialization"): return 47
        if ( name == "ImmediatelyVisitUgsCommand"): return 48
        if ( name == "LoiterVisitUgsCommand"): return 49
        if ( name == "IsolationControllerTerminated"): return 50
        if ( name == "PayloadPowerState"): return 51
        if ( name == "ToggleRequest"): return 52
        if ( name == "ToggleStatus"): return 53
        if ( name == "WifiConnectionStatus"): return 54
        if ( name == "AxisSnapshot"): return 55
        if ( name == "AxisVideoRecord"): return 56

        return -1

    def getInstance(self, type):
        if(type ==  1): return VicsBase.VicsBase()
        if(type ==  2): return VicsAck.VicsAck()
        if(type ==  3): return PickupMessageTask.PickupMessageTask()
        if(type ==  4): return DeliverMessageTask.DeliverMessageTask()
        if(type ==  5): return CommTransferTask.CommTransferTask()
        if(type ==  6): return PatrolTask.PatrolTask()
        if(type ==  7): return UgsManagementTask.UgsManagementTask()
        if(type ==  8): return SubTaskExecution.SubTaskExecution()
        if(type ==  9): return MeetMeTask.MeetMeTask()
        if(type ==  10): return ImageAreaSearchTask.ImageAreaSearchTask()
        if(type ==  11): return ImageLineSearchTask.ImageLineSearchTask()
        if(type ==  12): return ImagePointSearchTask.ImagePointSearchTask()
        if(type ==  13): return StateTransition.StateTransition()
        if(type ==  14): return DismountMessage.DismountMessage()
        if(type ==  15): return IntruderAlert.IntruderAlert()
        if(type ==  16): return UgsConfiguration.UgsConfiguration()
        if(type ==  17): return UgsStatusRequest.UgsStatusRequest()
        if(type ==  18): return UgsStatusResponse.UgsStatusResponse()
        if(type ==  19): return RadarEnableMessage.RadarEnableMessage()
        if(type ==  20): return HeartbeatMessage.HeartbeatMessage()
        if(type ==  21): return HeartbeatResponse.HeartbeatResponse()
        if(type ==  22): return PayloadData.PayloadData()
        if(type ==  23): return QueryResponse.QueryResponse()
        if(type ==  24): return GlobalMessageId.GlobalMessageId()
        if(type ==  25): return MessageQuery.MessageQuery()
        if(type ==  26): return MessageRequest.MessageRequest()
        if(type ==  27): return LocationXY.LocationXY()
        if(type ==  28): return EdgePairProbability.EdgePairProbability()
        if(type ==  29): return NetworkNode.NetworkNode()
        if(type ==  30): return NetworkNodeXY.NetworkNodeXY()
        if(type ==  31): return NetworkNodeLatLon.NetworkNodeLatLon()
        if(type ==  32): return ValueFunction.ValueFunction()
        if(type ==  33): return PiecewiseConstantUnitLength.PiecewiseConstantUnitLength()
        if(type ==  34): return PiecewiseConstantFixedEndPoints.PiecewiseConstantFixedEndPoints()
        if(type ==  35): return NetworkEdge.NetworkEdge()
        if(type ==  36): return NetworkRegion.NetworkRegion()
        if(type ==  37): return InitializeEstimator.InitializeEstimator()
        if(type ==  38): return NetworkLocation.NetworkLocation()
        if(type ==  39): return UgsReport.UgsReport()
        if(type ==  40): return NetworkPropagate.NetworkPropagate()
        if(type ==  41): return NetworkUpdate.NetworkUpdate()
        if(type ==  42): return CurrentNetworkStatus.CurrentNetworkStatus()
        if(type ==  43): return CurrentNetworkUpdate.CurrentNetworkUpdate()
        if(type ==  44): return LikertNetworkUpdate.LikertNetworkUpdate()
        if(type ==  45): return FixedUGS.FixedUGS()
        if(type ==  46): return UgsLaydown.UgsLaydown()
        if(type ==  47): return IsolationControllerInitialization.IsolationControllerInitialization()
        if(type ==  48): return ImmediatelyVisitUgsCommand.ImmediatelyVisitUgsCommand()
        if(type ==  49): return LoiterVisitUgsCommand.LoiterVisitUgsCommand()
        if(type ==  50): return IsolationControllerTerminated.IsolationControllerTerminated()
        if(type ==  51): return PayloadPowerState.PayloadPowerState()
        if(type ==  52): return ToggleRequest.ToggleRequest()
        if(type ==  53): return ToggleStatus.ToggleStatus()
        if(type ==  54): return WifiConnectionStatus.WifiConnectionStatus()
        if(type ==  55): return AxisSnapshot.AxisSnapshot()
        if(type ==  56): return AxisVideoRecord.AxisVideoRecord()

        return None
