from PyQt5.QtCore import QTimer, QObject, pyqtSignal
from VortexController import Controller

class PyqtController(QObject, Controller):
    button0Event = pyqtSignal(str, str, int, str, int)   # Signal for button press
    button1Event = pyqtSignal(str, str, int, str, int)   # Signal for button press
    button2Event = pyqtSignal(str, str, int, str, int)   # Signal for button press
    button3Event = pyqtSignal(str, str, int, str, int)   # Signal for button press
    button4Event = pyqtSignal(str, str, int, str, int)   # Signal for button press
    button5Event = pyqtSignal(str, str, int, str, int)   # Signal for button press
    button6Event = pyqtSignal(str, str, int, str, int)   # Signal for button press
    button7Event = pyqtSignal(str, str, int, str, int)   # Signal for button press
    button8Event = pyqtSignal(str, str, int, str, int)   # Signal for button press
    button9Event = pyqtSignal(str, str, int, str, int)   # Signal for button press
    button10Event = pyqtSignal(str, str, int, str, int)  # Signal for button press
    hat0Event = pyqtSignal(str, str, int, str, tuple)  # Signal for hats
    axis0Event = pyqtSignal(str, str, int, str, float) # Signal for axis
    axis1Event = pyqtSignal(str, str, int, str, float) # Signal for axis
    axis2Event = pyqtSignal(str, str, int, str, float) # Signal for axis
    axis3Event = pyqtSignal(str, str, int, str, float) # Signal for axis
    axis4Event = pyqtSignal(str, str, int, str, float) # Signal for axis
    axis5Event = pyqtSignal(str, str, int, str, float) # Signal for axis

    def __init__(self):
        super().__init__()
        # dead zone tolerance for axes values
        self.deadZoneValue = 0.1

        # Timer to periodically fetch and update controller data
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.getData)
        self.timer.start(20)  # Update every 20 ms

    def getData(self):
        controllerData = self.getControllerData()
        self.processData(controllerData)

    def processData(self, controllerData):
        for controller, data in controllerData.items():
            controllerName = data['name']

            # print(f"Controller: {controller}")
            # print(f"Name: {controllerName}")
            for axisId, axisData in data["axes"].items():
                if axisData["event"] is not None:
                    axisValue = min(max(axisData["value"], -1), 1)
                    # handle deadzone
                    if 0 <= axisId <= 3:
                        if abs(axisValue) <= self.deadZoneValue:
                            axisValue = 0
                            
                    # handle axisData
                    if axisId == 0:
                        self.axis0Event.emit(controller, controllerName, axisId, axisData["event"], axisValue)
                    elif axisId == 1:
                        self.axis1Event.emit(controller, controllerName, axisId, axisData["event"], axisValue)
                    elif axisId == 2:
                        self.axis2Event.emit(controller, controllerName, axisId, axisData["event"], axisValue)
                    elif axisId == 3:
                        self.axis3Event.emit(controller, controllerName, axisId, axisData["event"], axisValue)
                    elif axisId == 4:
                        self.axis4Event.emit(controller, controllerName, axisId, axisData["event"], axisValue)
                    elif axisId == 5:
                        self.axis5Event.emit(controller, controllerName, axisId, axisData["event"], axisValue)

            for hatId, hatData in data["hats"].items():
                if hatData["event"] is not None:
                    if hatId == 0:
                        self.hat0Event.emit(controller, controllerName, hatId, hatData["event"], hatData["value"])
    
            # Loop through buttons
            for buttonId, buttonData in data['buttons'].items():
                if buttonData["event"] is not None:
                    if buttonId == 0:
                        self.button0Event.emit(controller, controllerName, buttonId, buttonData["event"], buttonData["value"])
                    elif buttonId == 1:
                        self.button1Event.emit(controller, controllerName, buttonId, buttonData["event"], buttonData["value"])
                    elif buttonId == 2:
                        self.button2Event.emit(controller, controllerName, buttonId, buttonData["event"], buttonData["value"])
                    elif buttonId == 3:
                        self.button3Event.emit(controller, controllerName, buttonId, buttonData["event"], buttonData["value"])
                    elif buttonId == 4:
                        self.button4Event.emit(controller, controllerName, buttonId, buttonData["event"], buttonData["value"])
                    elif buttonId == 5:
                        self.button5Event.emit(controller, controllerName, buttonId, buttonData["event"], buttonData["value"])
                    elif buttonId == 6:
                        self.button6Event.emit(controller, controllerName, buttonId, buttonData["event"], buttonData["value"])
                    elif buttonId == 7:
                        self.button7Event.emit(controller, controllerName, buttonId, buttonData["event"], buttonData["value"])
                    elif buttonId == 8:
                        self.button8Event.emit(controller, controllerName, buttonId, buttonData["event"], buttonData["value"])
                    elif buttonId == 9:
                        self.button9Event.emit(controller, controllerName, buttonId, buttonData["event"], buttonData["value"])
                    elif buttonId == 10:
                        self.button10Event.emit(controller, controllerName, buttonId, buttonData["event"], buttonData["value"])

    def connect(self, eventsObject):
        self.button0Event.connect(eventsObject.button0Event)
        self.button1Event.connect(eventsObject.button1Event)
        self.button2Event.connect(eventsObject.button2Event)
        self.button3Event.connect(eventsObject.button3Event)
        self.button4Event.connect(eventsObject.button4Event)
        self.button5Event.connect(eventsObject.button5Event)
        self.button6Event.connect(eventsObject.button6Event)
        self.button7Event.connect(eventsObject.button7Event)
        self.button8Event.connect(eventsObject.button8Event)
        self.button9Event.connect(eventsObject.button9Event)
        self.button10Event.connect(eventsObject.button10Event)
        self.hat0Event.connect(eventsObject.hat0Event)
        self.axis0Event.connect(eventsObject.axis0Event)
        self.axis1Event.connect(eventsObject.axis1Event)
        self.axis2Event.connect(eventsObject.axis2Event)
        self.axis3Event.connect(eventsObject.axis3Event)
        self.axis4Event.connect(eventsObject.axis4Event)
        self.axis5Event.connect(eventsObject.axis5Event)
