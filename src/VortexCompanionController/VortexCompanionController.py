import random

from VortexInterfaces import CompanionControllerInterface
import json

class CompanionController(CompanionControllerInterface):
    
    def __init__(self, socket):
        self.socket = socket
        self.old_ph = 0

    def readSensorsData(self):
        return {
            "depth": self.getDepth(),
            "PH": self.getPH(),
            "heading": self.getHeading()
        }

    def getDepth(self):
        return round(random.uniform(0, 5), 2)
    
    def getPH(self):
        b = self.socket.receive(1024)
        try:
            if b is not None:
                b = b.decode().split("\n")
                x = None
                try:
                    x = json.loads(b[-2])
                except:
                    pass

                if x is not None:
                    self.old_ph = x["ph"]
                    return x["ph"]
        except:
            pass
            
        return self.old_ph
    
    def getHeading(self):
        return random.randint(0,359)
    
