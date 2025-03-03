from VortexInterfaces.VortexPilotingInterfaces import VortexPilotingInterfaces
from VortexPilot.ROVController import ROVController

class PilotAdapter(VortexPilotingInterfaces):
    def __init__(self, rov_controller: ROVController):
        self.rov_controller = rov_controller

    def rightGripper(self, buttonEvent: str):
        if buttonEvent == "JOYBUTTONDOWN":
            self.rov_controller.gripper_3(True)
        elif buttonEvent == "JOYBUTTONUP":
            self.rov_controller.gripper_3(False)

    def leftGripper(self, buttonEvent: str):
        if buttonEvent == "JOYBUTTONDOWN":
            self.rov_controller.gripper_2(True)
        elif buttonEvent == "JOYBUTTONUP":
            self.rov_controller.gripper_2(False)
    
    def led(self, buttonEvent: str):
        if buttonEvent == "JOYBUTTONDOWN":
            self.rov_controller.led(True)
        elif buttonEvent == "JOYBUTTONUP":
            self.rov_controller.led(False)
    
    def liftBag(self, buttonEvent: str):
        pass
    
    def fluidSuction(self, buttonEvent: str):
        if buttonEvent == "JOYBUTTONDOWN":
            self.rov_controller.pump1(True)
        elif buttonEvent == "JOYBUTTONUP":
            self.rov_controller.pump1(False)
    
    def sampleTool(self, buttonEvent: str):
        pass

    def floatingDebris(self, buttonEvent: str):
        if buttonEvent == "JOYBUTTONDOWN":
            self.rov_controller.pump2(True)
        elif buttonEvent == "JOYBUTTONUP":
            self.rov_controller.pump2(False)

    def stabilize(self, buttonEvent: str):
        if buttonEvent == "JOYBUTTONDOWN":
            self.rov_controller.set_stabilize(True)
        elif buttonEvent == "JOYBUTTONUP":
            self.rov_controller.set_stabilize(False)

    def altitudeHold(self, buttonEvent: str):
        if buttonEvent == "JOYBUTTONDOWN":
            self.rov_controller.set_alt_hold(True)
        elif buttonEvent == "JOYBUTTONUP":
            self.rov_controller.set_alt_hold(False)
    
    def rotatingGripper(self, buttonEvent: str):
        pass

    def surge(self, pwm:float):
        self.rov_controller.forward_channel(pwm)
    
    def sway(self, pwm:float):
        self.rov_controller.lateral_channel(pwm)
    
    def heave(self, pwm:float):
        self.rov_controller.throttle_channel(pwm)
    
    def roll(self, pwm:float):
        pass
    
    def pitch(self, pwm:float):
        pass
    
    def yaw(self, pwm:float):
        self.rov_controller.yaw_channel(pwm)

    def servo(self, pwm:float):
        self.rov_controller.servo(pwm)
