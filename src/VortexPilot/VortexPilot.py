from VortexInterfaces import VortexPilotingInterfaces

class VortexPilot(VortexPilotingInterfaces):
    def __init__(self):
        pass
    
    def rightGripper(self, buttonEvent: str):
        if(buttonEvent=="JOYBUTTONDOWN"):
            print("rightGripper:ON")
        elif(buttonEvent=="JOYBUTTONUP"):
            print("rightGripper:OFF")

    def leftGripper(self, buttonEvent: str):
        if(buttonEvent=="JOYBUTTONDOWN"):
            print("leftGripper:ON")
        elif(buttonEvent=="JOYBUTTONUP"):
            print("leftGripper:OFF")

    def led(self, buttonEvent: str):
        if(buttonEvent=="JOYBUTTONDOWN"):
            print("led:ON")
        elif(buttonEvent=="JOYBUTTONUP"):
            print("led:OFF")

    def floatingDebris(self, buttonEvent: str):
        if(buttonEvent=="JOYBUTTONDOWN"):
            print("floatingDebris:ON")
        elif(buttonEvent=="JOYBUTTONUP"):
            print("floatingDebris:OFF")

    def stabilize(self, buttonEvent: str):
        if(buttonEvent=="JOYBUTTONDOWN"):
            print("stabilize:ON")
        elif(buttonEvent=="JOYBUTTONUP"):
            print("stabilize:OFF")

    def altitudeHold(self, buttonEvent: str):
        if(buttonEvent=="JOYBUTTONDOWN"):
            print("altitudeHold:ON")
        elif(buttonEvent=="JOYBUTTONUP"):
            print("altitudeHold:OFF")

    def fluidSuction(self, buttonEvent: str):
        if(buttonEvent=="JOYBUTTONDOWN"):
            print("fluidSuction:ON")
        elif(buttonEvent=="JOYBUTTONUP"):
            print("fluidSuction:OFF")

    def sampleTool(self, buttonEvent: str):
        pass

    def rotatingGripper(self, buttonEvent: str):
        pass

    def liftBag(self, buttonEvent: str):
        pass

    def surge(self, pwm:float):
        print("Surge:{}".format(pwm))
     
    def sway(self, pwm:float):
        print("sway:{}".format(pwm))
     
    def heave(self, pwm:float):
        print("heave:{}".format(pwm))
         
    def roll(self, pwm:float):
        print("roll:{}".format(pwm))
     
    def pitch(self, pwm:float):
        print("pitch:{}".format(pwm))
         
    def yaw(self, pwm:float):
        print("yaw:{}".format(pwm))

    def servo(self, pwm:float):
        print("servo:{}".format(pwm))
