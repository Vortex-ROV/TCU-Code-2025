from PyQt5.QtCore import QObject
from VortexStation.VortexWidgetNamesEnums import CameraLabels

class PyqtRTSPCamera7Events(QObject):
    def __init__(self, cameraPixmap):
        super().__init__()
        self.cameraPixmap = cameraPixmap
        self.cameraLabel = CameraLabels.SecondaryBottomLeft

    def RTSPCamera7FrameEvent(self, frame):
        self.cameraPixmap(self.cameraLabel, frame)
    
    def setCameraLabel(self, label):
        self.cameraLabel = label
