from abc import ABCMeta, abstractmethod, ABC
from PyQt5.QtCore import QObject

# Define a metaclass that inherits both from PyQt's QObject and ABCMeta for abstract classes
class OAKVidgearClientMeta(type(QObject), ABCMeta):
    pass

class OAKVidgearClientInterfaces(ABC, metaclass=OAKVidgearClientMeta):
    @abstractmethod
    def startOAKVidgearThread(self):
        pass

    @abstractmethod
    def stopOAKVidgearThread(self):
        pass
    
    @abstractmethod
    def getFrame(self):
        pass

    @abstractmethod 
    def startRecording(self, filename, frame_rate, resolution):
        pass

    @abstractmethod 
    def stopRecording(self):
        pass

    @abstractmethod 
    def writeFrame(self, frame):
        pass