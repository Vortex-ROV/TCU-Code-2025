from PyQt5.QtCore import QObject
from VortexStation.VortexWidgetNamesEnums import CameraLabels
import time
class PyqtRTSPCamera2Events(QObject):
    def __init__(self, cameraPixmap):
        super().__init__()
        self.cameraPixmap = cameraPixmap
        self.cameraLabel = CameraLabels.MainTopRight

    def RTSPCamera2FrameEvent(self, frame):
        self.cameraPixmap(self.cameraLabel, frame)
    
    def setCameraLabel(self, label):
        self.cameraLabel = label
