from PyQt5.QtCore import QTimer, QObject, pyqtSignal
from VortexCompanionController import CompanionController

class PyqtCompanionController(QObject, CompanionController):
    depthEvent = pyqtSignal(float)      # Signal for depth data
    PHEvent = pyqtSignal(float)         # Signal for PH data
    headingEvent = pyqtSignal(int)      # Signal for headingEvent

    def __init__(self):
        super().__init__()
        # Timer to periodically fetch sensor readings
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.getData)
        self.timer.start(500)  # Update every 500 ms

    def getData(self):
        sensorReadings = self.readSensorsData()
        self.processReadings(sensorReadings)

    def processReadings(self, sensorReadings):
        for dataType, value in sensorReadings.items():
            if dataType == "depth":
                self.depthEvent.emit(value)
            elif dataType == "PH":
                self.PHEvent.emit(value)
            elif dataType == "heading":
                self.headingEvent.emit(value)
    
    def connect(self, eventsObject):
        self.depthEvent.connect(eventsObject.depthEvent)
        self.PHEvent.connect(eventsObject.PHEvent)
        self.headingEvent.connect(eventsObject.headingEvent)
