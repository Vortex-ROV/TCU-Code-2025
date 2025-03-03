from VortexInterfaces import VortexPilotingInterfaces
from VortexPilot import VortexPilot
from VortexPilot.PilotAdapter import PilotAdapter
from VortexStation.VortexWidgetNamesEnums import CircularGauge, Indicators, VortexPilotAction, CircularGaugesLabels, Readings
from VortexStation.VortexStationUtils import adjustPwm

class VortexPilotProxy(VortexPilotingInterfaces):
    def __init__(self, vortexPilot: PilotAdapter, circularGaugePainter, indicatorsPainter, cameraSwitcher, circularGaugesPixmap, readingsLabelUpdater):
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

        self.pressed = {
            self.rightGripper: False,
            self.leftGripper: False,
            self.led: False,
            self.floatingDebris: False,
            self.fluidSuction: False,
            self.sampleTool: False,
            self.stabilize: False,
            self.altitudeHold: False,
            self.rotatingGripper: False,
        }

    def pilotActionsExecutor(self, key, *args):
        """Execute the corresponding action based on action name."""
        action = self.actions.get(key)
        if action:
            action(*args)
        else:
            print(f"Action '{key}' not found.")

        self.vortexPilot.rov_controller.post_process()

        # self.vortexPilot.rov_controller.post_process()

    def rightGripper(self, buttonEvent: str):
        if buttonEvent == "JOYBUTTONDOWN":
            if self.pressed[self.rightGripper] == False:
                self.vortexPilot.rightGripper("JOYBUTTONDOWN")
                self.pressed[self.rightGripper] = True
                self.indicatorsPainter(Indicators.RightGripper)
            else:
                self.vortexPilot.rightGripper("JOYBUTTONUP")
                self.pressed[self.rightGripper] = False
                self.indicatorsPainter(Indicators.RightGripper, PAINT_BORDERS=False)

    def leftGripper(self, buttonEvent: str):
        if buttonEvent == "JOYBUTTONDOWN":
            if self.pressed[self.leftGripper] == False:
                self.vortexPilot.leftGripper("JOYBUTTONDOWN")
                self.pressed[self.leftGripper] = True
                self.indicatorsPainter(Indicators.LeftGripper)
            else:
                self.vortexPilot.leftGripper("JOYBUTTONUP")
                self.pressed[self.leftGripper] = False
                self.indicatorsPainter(Indicators.LeftGripper, PAINT_BORDERS=False)

    def led(self, buttonEvent: str):
        if buttonEvent == "JOYBUTTONDOWN":
            if self.pressed[self.led] == False:
                self.vortexPilot.led("JOYBUTTONDOWN")
                self.pressed[self.led] = True
                self.indicatorsPainter(Indicators.Led)
            else:
                self.vortexPilot.led("JOYBUTTONUP")
                self.pressed[self.led] = False
                self.indicatorsPainter(Indicators.Led, PAINT_BORDERS=False)

    def floatingDebris(self, buttonEvent: str):
        if buttonEvent == "JOYBUTTONDOWN":
            if self.pressed[self.floatingDebris] == False:
                self.vortexPilot.floatingDebris("JOYBUTTONDOWN")
                self.pressed[self.floatingDebris] = True
                self.indicatorsPainter(Indicators.FloatingDebris)
            else:
                self.vortexPilot.floatingDebris("JOYBUTTONUP")
                self.pressed[self.floatingDebris] = False
                self.indicatorsPainter(Indicators.FloatingDebris, PAINT_BORDERS=False)

    def stabilize(self, buttonEvent: str):
        if buttonEvent == "JOYHATMOTION":
            if self.pressed[self.stabilize] == False:
                self.vortexPilot.stabilize("JOYBUTTONDOWN")
                self.pressed[self.stabilize] = True
                self.indicatorsPainter(Indicators.Stabalize)
            else:
                self.vortexPilot.stabilize("JOYBUTTONUP")
                self.pressed[self.stabilize] = False
                self.indicatorsPainter(Indicators.Stabalize, PAINT_BORDERS=False)

    def altitudeHold(self, buttonEvent: str):
        if buttonEvent == "JOYHATMOTION":
            if self.pressed[self.altitudeHold] == False:
                self.vortexPilot.altitudeHold("JOYBUTTONDOWN")
                self.pressed[self.altitudeHold] = True
                self.indicatorsPainter(Indicators.AltitudeHold)
            else:
                self.vortexPilot.altitudeHold("JOYBUTTONUP")
                self.pressed[self.altitudeHold] = False
                self.indicatorsPainter(Indicators.AltitudeHold, PAINT_BORDERS=False)

    def fluidSuction(self, buttonEvent: str):
        if buttonEvent == "JOYBUTTONDOWN":
            if self.pressed[self.fluidSuction] == False:
                self.vortexPilot.fluidSuction("JOYBUTTONDOWN")
                self.pressed[self.fluidSuction] = True
                self.indicatorsPainter(Indicators.FluidSuction)
            else:
                self.vortexPilot.fluidSuction("JOYBUTTONUP")
                self.pressed[self.fluidSuction] = False
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