import random

from VortexInterfaces import CompanionControllerInterface

class CompanionController(CompanionControllerInterface):
    
    def __init__(self):
        pass

    def readSensorsData(self):
        return {
            "depth": self.getDepth(),
            "PH": self.getPH(),
            "heading": self.getHeading()
        }

    def getDepth(self):
        return round(random.uniform(0, 5), 2)
    
    def getPH(self):
        return round(random.uniform(0, 14), 1)
    
    def getHeading(self):
        return random.randint(0,359)