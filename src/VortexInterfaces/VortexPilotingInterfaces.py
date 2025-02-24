from abc import abstractmethod, ABC

class VortexPilotingInterfaces(ABC):
    @abstractmethod
    def rightGripper(self, buttonEvent: str):
        pass

    @abstractmethod  
    def leftGripper(self, buttonEvent: str):
        pass
    
    @abstractmethod  
    def led(self, buttonEvent: str):
        pass
    
    @abstractmethod 
    def liftBag(self, buttonEvent: str):
        pass
    
    @abstractmethod 
    def fluidSuction(self, buttonEvent: str):
        pass
    
    @abstractmethod 
    def sampleTool(self, buttonEvent: str):
        pass

    @abstractmethod 
    def floatingDebris(self, buttonEvent: str):
        pass

    @abstractmethod 
    def stabilize(self, buttonEvent: str):
        pass

    @abstractmethod 
    def altitudeHold(self, buttonEvent: str):
        pass
    
    @abstractmethod 
    def rotatingGripper(self, buttonEvent: str):
        pass

    @abstractmethod 
    def surge(self, pwm:float):
        pass
    
    @abstractmethod 
    def sway(self, pwm:float):
        pass
    
    @abstractmethod 
    def heave(self, pwm:float):
        pass
    
    @abstractmethod 
    def roll(self, pwm:float):
        pass
    
    @abstractmethod 
    def pitch(self, pwm:float):
        pass
    
    @abstractmethod 
    def yaw(self, pwm:float):
        pass

    @abstractmethod 
    def servo(self, pwm:float):
        pass