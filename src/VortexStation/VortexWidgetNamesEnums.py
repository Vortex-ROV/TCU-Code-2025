from enum import Enum

class CircularGauge(Enum):
    FourThrusters = 1
    UpDownThrusters = 2
    Servo = 3

class CircularGaugesLabels(Enum):
    FourThrustersForwards = 1
    FourThrustersBackwards = 2
    FourThrustersRight = 3
    FourThrustersLeft = 4
    FourThrustersCW = 5
    FourThrustersCCW = 6
    FourThrustersNone = 7
    UpDownThrustersUP = 8
    UpDownThrustersDOWN = 9
    UpDownThrustersNone = 10
    ServoCW = 11
    ServoCCW = 12
    ServoNone = 13
    
class Indicators(Enum):
    Led = 1
    RightGripper = 2
    LeftGripper = 3
    FluidSuction = 4
    FloatingDebris = 5
    AltitudeHold = 6
    Stabalize = 7

class VortexPilotAction(Enum):
    Led = 1
    RightGripper = 2
    LeftGripper = 3
    FluidSuction = 4
    FloatingDebris = 5
    AltitudeHold = 6
    Stabilize = 7
    CameraSwitch = 8
    Gain = 9
    Heave = 10
    Pitch = 11
    Roll = 12
    Servo = 13
    Surge = 14
    Sway = 15
    Yaw = 17

class JoystickButtons(Enum):
    A = 0 
    B = 1
    X = 2
    Y = 3
    LB = 4
    RB = 5
    BACK = 6
    START = 7
    LEFTPAD = 8
    RIGHTPAD = 9
    HOME = 10


class JoystickAxis(Enum):
    LEFTHORIZONTALAXIS = 0
    LEFTVERTICALAXIS = 1
    RIGHTHORIZONTALAXIS = 2
    RIGHTVERTICALAXIS = 3
    LT = 4
    RT = 5

class Readings(Enum):
    Gain = 0
    PH = 1
    Heading = 2
    Depth = 3

class CameraLabels:
    MainTopLeft = 0
    MainTopRight = 1
    MainBottomLeft = 2
    MainBottomRight = 3
    SecondaryTopLeft = 4
    SecondaryTopRight = 5
    SecondaryBottomLeft = 6
    SecondaryBottomRight = 7
