from PyQt5.QtCore import QObject
from VortexStation.VortexWidgetNamesEnums import CameraLabels

class PyqtRTSPCamera3Events(QObject):
    def __init__(self, cameraPixmap):
        super().__init__()
        self.cameraPixmap = cameraPixmap
        self.cameraLabel = CameraLabels.MainBottomLeft

    def RTSPCamera3FrameEvent(self, frame):
        self.cameraPixmap(self.cameraLabel, frame)
    
    def setCameraLabel(self, label):
        self.cameraLabel = label
