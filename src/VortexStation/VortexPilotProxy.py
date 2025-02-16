from VortexInterfaces import VortexPilotingInterfaces
from VortexPilot import VortexPilot
from VortexStation.VortexWidgetNamesEnums import CircularGauge, Indicators, VortexPilotAction, CircularGaugesLabels, Readings
from VortexStation.VortexStationUtils import adjustPwm

class VortexPilotProxy(VortexPilotingInterfaces):
    def __init__(self, vortexPilot:VortexPilot, circularGaugePainter, indicatorsPainter, cameraSwitcher, circularGaugesPixmap, readingsLabelUpdater):
        self.actions = {
            VortexPilotAction.RightGripper: self.rightGripper,
            VortexPilotAction.LeftGripper: self.leftGripper,
            VortexPilotAction.Led: self.led,
            VortexPilotAction.FluidSuction: self.fluidSuction,
            VortexPilotAction.FloatingDebris: self.floatingDebris,
            VortexPilotAction.Stabilize: self.stabilize,
            VortexPilotAction.AltitudeHold: self.altitudeHold,
            VortexPilotAction.CameraSwitch: self.cameraSwitch,
            VortexPilotAction.Gain : self.gain,
            VortexPilotAction.Surge: self.surge,
            VortexPilotAction.Heave: self.heave,
            VortexPilotAction.Sway: self.sway,
            VortexPilotAction.Yaw: self.yaw,
            VortexPilotAction.Roll: self.roll,
            VortexPilotAction.Pitch: self.pitch,
            VortexPilotAction.Servo: self.servo
        }

        # interfacing with vortex pilot
        self.vortexPilot = vortexPilot
        
        # interfacing with widgets
        self.indicatorsPainter = indicatorsPainter
        self.circularGaugePainter = circularGaugePainter
        self.cameraSwitcher = cameraSwitcher
        self.circularGaugesPixmap = circularGaugesPixmap
        self.readingsLabelUpdater = readingsLabelUpdater

        # attributes
        self.cameraSwitchEvent = "JOYBUTTONDOWN"
        self.gainUpdateEvent = "JOYBUTTONDOWN"
        self.gainValues = [25, 50, 75, 100]
        self.gainIndex = 3

    def pilotActionsExecutor(self, key, *args):
        """Execute the corresponding action based on action name."""
        action = self.actions.get(key)
        if action:
            action(*args)
        else:
            print(f"Action '{key}' not found.")

    def rightGripper(self, buttonEvent: str):
        self.vortexPilot.rightGripper(buttonEvent=buttonEvent)
        if buttonEvent == "JOYBUTTONDOWN":
            self.indicatorsPainter(Indicators.RightGripper)
        elif buttonEvent == "JOYBUTTONUP":
            self.indicatorsPainter(Indicators.RightGripper, PAINT_BORDERS=False)

    def leftGripper(self, buttonEvent: str):
        self.vortexPilot.leftGripper(buttonEvent=buttonEvent)
        if buttonEvent == "JOYBUTTONDOWN":
            self.indicatorsPainter(Indicators.LeftGripper)
        elif buttonEvent == "JOYBUTTONUP":
            self.indicatorsPainter(Indicators.LeftGripper, PAINT_BORDERS=False)

    def led(self, buttonEvent: str):
        self.vortexPilot.led(buttonEvent=buttonEvent)
        if buttonEvent == "JOYBUTTONDOWN":
            self.indicatorsPainter(Indicators.Led)
        elif buttonEvent == "JOYBUTTONUP":
            self.indicatorsPainter(Indicators.Led, PAINT_BORDERS=False)

    def floatingDebris(self, buttonEvent: str):
        self.vortexPilot.floatingDebris(buttonEvent=buttonEvent)
        if buttonEvent == "JOYBUTTONDOWN":
            self.indicatorsPainter(Indicators.FloatingDebris)
        elif buttonEvent == "JOYBUTTONUP":
            self.indicatorsPainter(Indicators.FloatingDebris, PAINT_BORDERS=False)

    def stabilize(self, buttonEvent: str):
        self.vortexPilot.stabilize(buttonEvent=buttonEvent)
        if buttonEvent == "JOYBUTTONDOWN":
            self.indicatorsPainter(Indicators.Stabalize)
        elif buttonEvent == "JOYBUTTONUP":
            self.indicatorsPainter(Indicators.Stabalize, PAINT_BORDERS=False)

    def altitudeHold(self, buttonEvent: str):
        self.vortexPilot.altitudeHold(buttonEvent=buttonEvent)
        if buttonEvent == "JOYBUTTONDOWN":
            self.indicatorsPainter(Indicators.AltitudeHold)
        elif buttonEvent == "JOYBUTTONUP":
            self.indicatorsPainter(Indicators.AltitudeHold, PAINT_BORDERS=False)

    def fluidSuction(self, buttonEvent: str):
        self.vortexPilot.fluidSuction(buttonEvent=buttonEvent)
        if buttonEvent == "JOYBUTTONDOWN":
            self.indicatorsPainter(Indicators.FluidSuction)
        elif buttonEvent == "JOYBUTTONUP":
            self.indicatorsPainter(Indicators.FluidSuction, PAINT_BORDERS=False)

    def cameraSwitch(self, buttonEvent: str):
        if self.cameraSwitchEvent == buttonEvent:
            self.cameraSwitcher()

    def gain(self, buttonEvent: str):
        if self.gainUpdateEvent == buttonEvent:
            self.gainIndex += 1
            if self.gainIndex > 3:
                self.gainIndex = 0
            self.readingsLabelUpdater(Readings.Gain, str(self.gainValues[self.gainIndex]))

    def sampleTool(self, buttonEvent: str):
        pass

    def rotatingGripper(self, buttonEvent: str):
        pass

    def liftBag(self, buttonEvent: str):
        pass
        
    def surge(self, pwm:float):
        pwm = adjustPwm(pwm, self.gainValues[self.gainIndex])
        self.vortexPilot.surge(pwm=pwm)
        self.circularGaugePainter(CircularGauge.FourThrusters, int(abs(pwm-1500)/4))
        if (pwm > 1500):
            self.circularGaugesPixmap(CircularGaugesLabels.FourThrustersForwards)
        elif (pwm < 1500):
            self.circularGaugesPixmap(CircularGaugesLabels.FourThrustersBackwards)
        elif pwm == 1500:
            self.circularGaugesPixmap(CircularGaugesLabels.FourThrustersNone)

    def sway(self, pwm:float):
        pwm = adjustPwm(pwm, self.gainValues[self.gainIndex])
        self.vortexPilot.sway(pwm=pwm)
        self.circularGaugePainter(CircularGauge.FourThrusters, int(abs(pwm-1500)/4))
        if (pwm > 1500):
            self.circularGaugesPixmap(CircularGaugesLabels.FourThrustersRight)
        elif (pwm < 1500):
            self.circularGaugesPixmap(CircularGaugesLabels.FourThrustersLeft)
        elif pwm == 1500:
            self.circularGaugesPixmap(CircularGaugesLabels.FourThrustersNone)

    def heave(self, pwm:float):
        pwm = adjustPwm(pwm, self.gainValues[self.gainIndex])
        self.vortexPilot.heave(pwm=pwm)
        self.circularGaugePainter(CircularGauge.UpDownThrusters, int(abs(pwm-1500)/4))
        if (pwm > 1500):
            self.circularGaugesPixmap(CircularGaugesLabels.UpDownThrustersUP)
        elif (pwm < 1500):
            self.circularGaugesPixmap(CircularGaugesLabels.UpDownThrustersDOWN)
        elif pwm == 1500:
            self.circularGaugesPixmap(CircularGaugesLabels.UpDownThrustersNone)

    def roll(self, pwm:float):
        pwm = adjustPwm(pwm, self.gainValues[self.gainIndex])
        pass     
    def pitch(self, pwm:float):
        pwm = adjustPwm(pwm, self.gainValues[self.gainIndex])
        pass

    def yaw(self, pwm:float):
        pwm = adjustPwm(pwm, self.gainValues[self.gainIndex])
        self.vortexPilot.yaw(pwm=pwm)
        self.circularGaugePainter(CircularGauge.FourThrusters, int(abs(pwm-1500)/4))
        if (pwm > 1500):
            self.circularGaugesPixmap(CircularGaugesLabels.FourThrustersCW)
        elif (pwm < 1500):
            self.circularGaugesPixmap(CircularGaugesLabels.FourThrustersCCW)
        elif pwm == 1500:
            self.circularGaugesPixmap(CircularGaugesLabels.FourThrustersNone)

    def servo(self, pwm:float):
        pwm = adjustPwm(pwm, self.gainValues[self.gainIndex])
        self.vortexPilot.servo(pwm=pwm)
        self.circularGaugePainter(CircularGauge.Servo, int(abs(pwm-1500)/4))
        if (pwm > 1500):
            self.circularGaugesPixmap(CircularGaugesLabels.ServoCW)
        elif (pwm < 1500):
            self.circularGaugesPixmap(CircularGaugesLabels.ServoCCW)
        elif pwm == 1500:
            self.circularGaugesPixmap(CircularGaugesLabels.ServoNone)