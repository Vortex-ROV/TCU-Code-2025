from PyQt5.QtCore import QObject
from VortexStation.VortexWidgetNamesEnums import CameraLabels

class PyqtRTSPCamera1Events(QObject):
    def __init__(self, cameraPixmap):
        super().__init__()
        self.cameraPixmap = cameraPixmap
        self.cameraLabel = CameraLabels.MainTopLeft

    def RTSPCamera1FrameEvent(self, frame):
        self.cameraPixmap(self.cameraLabel, frame)
    
    def setCameraLabel(self, label):
        self.cameraLabel = label