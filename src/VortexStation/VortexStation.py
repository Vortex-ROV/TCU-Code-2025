import sys
import os
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizeGrip, QPushButton
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, QSettings
from PyQt5.QtGui import QIcon, QPixmap, QImage
from VortexStation.PyqtCompanionController import PyqtCompanionController
from VortexStation.PyqtCompanionControllerEvents import PyqtCompanionControllerEvents
from VortexStation.PyqtController import PyqtController
from VortexStation.PyqtControllerEvents import PyqtControllerEvents
from VortexStation.VortexPilotProxy import VortexPilotProxy
from VortexStation.UI_MainWindow import Ui_MainWindow
from VortexStation.VortexWidgetNamesEnums import CircularGauge, Indicators, VortexPilotAction, JoystickButtons, JoystickAxis, CircularGaugesLabels, Readings, CameraLabels
from VortexStation.PyqtRTSPCamera1 import PyqtRTSPCamera1
from VortexStation.PyqtRTSPCamera2 import PyqtRTSPCamera2
from VortexStation.PyqtRTSPCamera3 import PyqtRTSPCamera3
from VortexStation.PyqtRTSPCamera4 import PyqtRTSPCamera4
from VortexStation.PyqtRTSPCamera5 import PyqtRTSPCamera5
from VortexStation.PyqtRTSPCamera6 import PyqtRTSPCamera6
from VortexStation.PyqtRTSPCamera7 import PyqtRTSPCamera7
from VortexStation.PyqtRTSPCamera8 import PyqtRTSPCamera8
from VortexStation.PyqtRTSPCamera1Events import PyqtRTSPCamera1Events
from VortexStation.PyqtRTSPCamera2Events import PyqtRTSPCamera2Events
from VortexStation.PyqtRTSPCamera3Events import PyqtRTSPCamera3Events
from VortexStation.PyqtRTSPCamera4Events import PyqtRTSPCamera4Events
from VortexStation.PyqtRTSPCamera5Events import PyqtRTSPCamera5Events
from VortexStation.PyqtRTSPCamera6Events import PyqtRTSPCamera6Events
from VortexStation.PyqtRTSPCamera7Events import PyqtRTSPCamera7Events
from VortexStation.PyqtRTSPCamera8Events import PyqtRTSPCamera8Events
from VortexStation.PyqtOAKVidgearClient import PyqtOakVidgearClient
from VortexStation.PyqtOAKVidgearClientEvents import PyqtOakVidgearClientEvents
from VortexPilot import VortexPilot
from VortexStation.VortexStationUtils import Worker
from VortexPilot.ROVController import ROVController
from VortexPilot.PilotAdapter import PilotAdapter
from VortexCompanionController.VortexCompanionController import CompanionController
from VortexController.VortexController import Controller
import time

class VortexMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Dictionary for Circular Gauges
        self.circularGauges = {
            CircularGauge.FourThrusters: self.fourThrustersGauge,
            CircularGauge.UpDownThrusters: self.upDownThrustersGauge,
            CircularGauge.Servo: self.servoGauge,
        }

        # Dictionary for Circular Gauges Labels
        self.circularGaugesLabels = {
            CircularGaugesLabels.FourThrustersForwards: QPixmap(":/circularGaugesLabels/feather/arrow-up.svg"),
            CircularGaugesLabels.FourThrustersBackwards: QPixmap(":/circularGaugesLabels/feather/arrow-down.svg"),
            CircularGaugesLabels.FourThrustersRight: QPixmap(":/circularGaugesLabels/feather/arrow-right.svg"),
            CircularGaugesLabels.FourThrustersLeft: QPixmap(":/circularGaugesLabels/feather/arrow-left.svg"),
            CircularGaugesLabels.FourThrustersCW: QPixmap(":/circularGaugesLabels/feather/refresh-cw.svg"),
            CircularGaugesLabels.FourThrustersCCW: QPixmap(":/circularGaugesLabels/feather/refresh-ccw.svg"),
            CircularGaugesLabels.UpDownThrustersUP: QPixmap(":/circularGaugesLabels/feather/upload.svg"),
            CircularGaugesLabels.UpDownThrustersDOWN: QPixmap(":/circularGaugesLabels/feather/download.svg"),
            CircularGaugesLabels.ServoCW: QPixmap(":/circularGaugesLabels/feather/rotate-cw.svg"),
            CircularGaugesLabels.ServoCCW: QPixmap(":/circularGaugesLabels/feather/rotate-ccw.svg"),
        }

        # Dictionary for Indicator frames
        self.indicators = {
            Indicators.Led: self.ledFrame,
            Indicators.RightGripper: self.rightGripperFrame,
            Indicators.LeftGripper: self.leftGripperFrame,
            Indicators.FluidSuction: self.fluidSuctionFrame,
            Indicators.FloatingDebris: self.floatingDebrisFrame,
            Indicators.AltitudeHold: self.altitudeHoldFrame,
            Indicators.Stabalize: self.stabilizeFrame
        }

        # Dictionary for readings labels
        self.readingsLabels = {
            Readings.Gain: self.gainReadingLabel,
            Readings.PH: self.phSensorReadingLabel,
            Readings.Heading: self.headingReadingLabel,
            Readings.Depth: self.depthReadingLabel,
        }

        # Dictionary for camera labels
        self.cameraLabels = {
            CameraLabels.MainTopLeft: self.mainHomePageTopLeftCameraLabel,
            CameraLabels.MainTopRight: self.mainHomePageTopRightCameraLabel,
            CameraLabels.MainBottomLeft: self.mainHomePageBottomLeftCameraLabel,
            CameraLabels.MainBottomRight: self.mainHomePageBottomRightCameraLabel,
            CameraLabels.SecondaryTopLeft: self.secondaryHomePageTopLeftCameraLabel,
            CameraLabels.SecondaryTopRight: self.secondaryHomePageTopRightCameraLabel,
            CameraLabels.SecondaryBottomLeft: self.secondaryHomePageBottomLeftCameraLabel,
            CameraLabels.SecondaryBottomRight: self.secondaryHomePageBottomRightCameraLabel,
        }
        
        # lists are used to know which cameras are in which page.
        self.homePageCamerasList = []
        self.secondaryPageCamerasList = []

        # attributes for cameras classes
        self.pyqtOakVidgearClient = None
        self.pyqtOakVidgearClientEvents = None 
        self.pyqtRTSPCamera1 = None
        self.pyqtRTSPCamera1Events = None
        self.pyqtRTSPCamera2 = None
        self.pyqtRTSPCamera2Events = None 
        self.pyqtRTSPCamera3 = None
        self.pyqtRTSPCamera3Events = None 
        self.pyqtRTSPCamera4 = None
        self.pyqtRTSPCamera4Events = None 
        self.pyqtRTSPCamera5 = None
        self.pyqtRTSPCamera5Events = None 
        self.pyqtRTSPCamera6 = None
        self.pyqtRTSPCamera6Events = None 
        self.pyqtRTSPCamera7 = None
        self.pyqtRTSPCamera7Events = None 
        self.pyqtRTSPCamera8 = None
        self.pyqtRTSPCamera8Events = None 
        
        # attribtues used to move window
        self.clickPosition = None

        # remove title bar
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground) 

        # set all gauges to zero.
        for gauge in CircularGauge:
            self.circularGaugePainter(gauge, 0)
        
        # remove border paint from indicators
        for indicator in Indicators:
            self.indicatorsPainter(indicator, PAINT_BORDERS=False)

        # Vortex Pilot Class, Event and Mapping
        self.vortexPilot = PilotAdapter(ROVController())
        # self.vortexPilot = VortexPilot()

        # Controller Class, Event and Mapping
        self.vortexPilotProxy = VortexPilotProxy(self.vortexPilot, self.circularGaugePainter, self.indicatorsPainter, self.cameraSwitcher, self.circularGaugesPixmap, self.readingsLabelUpdater)

        # Controller Class, Event and Mapping
        # self.pyqtController = PyqtController(ControllerAdapter(JoystickHandler()), self.vortexPilotProxy.pilotActionsExecutor)
        self.pyqtController = PyqtController(Controller())
        self.pyqtControllerEvents = PyqtControllerEvents(self.vortexPilotProxy.pilotActionsExecutor)
        self.pyqtController.connect(self.pyqtControllerEvents)

        # CompanionController Class, Event and Mapping
        self.pyqtCompanionController = PyqtCompanionController(CompanionController(self.vortexPilot.rov_controller.client), self.vortexPilot.rov_controller.client)
        self.pyqtCompanionControllerEvents = PyqtCompanionControllerEvents(self.readingsLabelUpdater)
        self.pyqtCompanionController.connect(self.pyqtCompanionControllerEvents)
        # header right buttons logic
        self.IS_WINDOW_MAXIMIZED = False
        self.exitButton.clicked.connect(lambda: self.close())
        self.minimizeButton.clicked.connect(lambda: self.showMinimized())
        self.maximizeButton.clicked.connect(lambda: self.maximizeButtonLogic())

        #QSizeGrip
        QSizeGrip(self.sizeGripFrame)

        # toggle left menu
        self.navigationButton.clicked.connect(lambda: self.navigationButtonLogic())

        # QStackedWidget Logic
        self.homeButton.clicked.connect(lambda:self.homePageStackedWidget.setCurrentWidget(self.mainHomePage)) 
        self.homeButton.clicked.connect(lambda:self.mainBodyStackedWidget.setCurrentWidget(self.homePage)) 
        self.homeButton.clicked.connect(lambda:self.resumeHomePageCameras())
        self.cameraButton.clicked.connect(lambda:self.homePageStackedWidget.setCurrentWidget(self.secondayHomePage)) 
        self.cameraButton.clicked.connect(lambda:self.mainBodyStackedWidget.setCurrentWidget(self.homePage)) 
        self.cameraButton.clicked.connect(lambda:self.resumeSecondaryPageCameras())
        self.settingsButton.clicked.connect(lambda: self.mainBodyStackedWidget.setCurrentWidget(self.settingsPage))
        self.controllerSettingsButton.clicked.connect(lambda: self.mainBodyStackedWidget.setCurrentWidget(self.controllerSettingsPage))
        self.cameraSettingsButton.clicked.connect(lambda: self.mainBodyStackedWidget.setCurrentWidget(self.cameraSettingsPage))

        # ControllerSettingsPage Save Button Logic
        self.saveControllerSettingButton.clicked.connect(lambda: self.saveControllerSettingsButtonLogic())

        # CameraSetingsPage Save Button Logic
        self.saveCameraSettingButton.clicked.connect(lambda: self.saveCameraSettingsButtonLogic())

        # Main Body Left Buttons Styling
        for buttonWidget in self.mainBodyLeftButtonsFrame.findChildren(QPushButton): 
            buttonWidget.clicked.connect(lambda: self.leftMenuButtonsPainter())
        
        # header frame logic
        self.headerFrame.mouseMoveEvent = self.moveWindow

        # initialize cameras
        self.pyqtOakVidgearClient = PyqtOakVidgearClient()
        self.pyqtOakVidgearClientEvents = PyqtOakVidgearClientEvents(self.cameraPixmap)
        self.pyqtOakVidgearClient.oakFrameEvent.connect(self.pyqtOakVidgearClientEvents.oakFrameEvent)

        self.pyqtRTSPCamera1 = PyqtRTSPCamera1("videotestsrc ! videoconvert ! appsink")
        self.pyqtRTSPCamera1Events = PyqtRTSPCamera1Events(self.cameraPixmap)
        self.pyqtRTSPCamera1.RTSPCamera1FrameEvent.connect(self.pyqtRTSPCamera1Events.RTSPCamera1FrameEvent)


        self.pyqtRTSPCamera2 = PyqtRTSPCamera2("videotestsrc ! videoconvert ! appsink")
        self.pyqtRTSPCamera2Events = PyqtRTSPCamera2Events(self.cameraPixmap)
        self.pyqtRTSPCamera2.RTSPCamera2FrameEvent.connect(self.pyqtRTSPCamera2Events.RTSPCamera2FrameEvent)

        self.pyqtRTSPCamera3 = PyqtRTSPCamera3("videotestsrc ! videoconvert ! appsink")
        self.pyqtRTSPCamera3Events = PyqtRTSPCamera3Events(self.cameraPixmap)
        self.pyqtRTSPCamera3.RTSPCamera3FrameEvent.connect(self.pyqtRTSPCamera3Events.RTSPCamera3FrameEvent)


        self.pyqtRTSPCamera4 = PyqtRTSPCamera4("videotestsrc ! videoconvert ! appsink")
        self.pyqtRTSPCamera4Events = PyqtRTSPCamera4Events(self.cameraPixmap)
        self.pyqtRTSPCamera4.RTSPCamera4FrameEvent.connect(self.pyqtRTSPCamera4Events.RTSPCamera4FrameEvent)


        self.pyqtRTSPCamera5 = PyqtRTSPCamera5("videotestsrc ! videoconvert ! appsink")
        self.pyqtRTSPCamera5Events = PyqtRTSPCamera5Events(self.cameraPixmap)
        self.pyqtRTSPCamera5.RTSPCamera5FrameEvent.connect(self.pyqtRTSPCamera5Events.RTSPCamera5FrameEvent)


        self.pyqtRTSPCamera6 = PyqtRTSPCamera6("videotestsrc ! videoconvert ! appsink")
        self.pyqtRTSPCamera6Events = PyqtRTSPCamera6Events(self.cameraPixmap)
        self.pyqtRTSPCamera6.RTSPCamera6FrameEvent.connect(self.pyqtRTSPCamera6Events.RTSPCamera6FrameEvent)

        self.pyqtRTSPCamera7 = PyqtRTSPCamera7("videotestsrc ! videoconvert ! appsink")
        self.pyqtRTSPCamera7Events = PyqtRTSPCamera7Events(self.cameraPixmap)
        self.pyqtRTSPCamera7.RTSPCamera7FrameEvent.connect(self.pyqtRTSPCamera7Events.RTSPCamera7FrameEvent)


        self.pyqtRTSPCamera8 = PyqtRTSPCamera8("videotestsrc ! videoconvert ! appsink")
        self.pyqtRTSPCamera8Events = PyqtRTSPCamera8Events(self.cameraPixmap)
        self.pyqtRTSPCamera8.RTSPCamera8FrameEvent.connect(self.pyqtRTSPCamera8Events.RTSPCamera8FrameEvent)

        # start cameras threads
        cameraWorker = Worker(self.startCamerasThreads)
        cameraWorker.start()

        # sleep for 1 second before loading settings
        time.sleep(1)

        # Create a QSettings instance with the custom file path (using IniFormat) to save/load custom settings.
        self.settingsINI = QSettings(os.path.join(os.path.expanduser("~/Documents"), "VortexUI.ini"), QSettings.IniFormat)
        self.loadControllerSettingsLogic()
        self.loadCameraSettingsLogic()

        # go to home page.
        self.homeButton.click()

    def startCamerasThreads(self):
        time.sleep(1)
        self.pyqtOakVidgearClient.start()
        time.sleep(1)
        self.pyqtRTSPCamera1.start()
        time.sleep(1)
        self.pyqtRTSPCamera2.start()
        time.sleep(1)
        self.pyqtRTSPCamera3.start()
        time.sleep(1)
        self.pyqtRTSPCamera4.start()
        time.sleep(1)
        self.pyqtRTSPCamera5.start()
        time.sleep(1)
        self.pyqtRTSPCamera6.start()
        time.sleep(1)
        self.pyqtRTSPCamera7.start()
        time.sleep(1)
        self.pyqtRTSPCamera8.start()
        time.sleep(1)
        
    def cameraPixmap(self, cameraLabel, frame):
        height, width, _ = frame.shape
        bytes_per_line = 3 * width
        qImg = QImage(frame.data, width, height, bytes_per_line, QImage.Format_BGR888)
        pixmap = QPixmap.fromImage(qImg)
        scaledPixmap = pixmap.scaled(self.cameraLabels[cameraLabel].size(), Qt.IgnoreAspectRatio)
        self.cameraLabels[cameraLabel].setPixmap(scaledPixmap)

    def readingsLabelUpdater(self, key, value):
        labelWidget = self.readingsLabels[key]
        labelWidget.setText(value)
    
    def indicatorsPainter(self, key, PAINT_BORDERS=True):
        indicatorWidget = self.indicators[key]
        if PAINT_BORDERS:
            newStyle = indicatorWidget.styleSheet() + "QLabel{border: 3px solid #FFB86C;}" 
            indicatorWidget.setStyleSheet(newStyle)
        else:
            defaultStyle = indicatorWidget.styleSheet().replace("QLabel{border: 3px solid #FFB86C;}", "") 
            indicatorWidget.setStyleSheet(defaultStyle)

    def mousePressEvent(self, event): 
        self.clickPosition = event.globalPos()
    
    def moveWindow(self, event):
        if self.isMaximized() == False: 
            if event.buttons() == Qt.LeftButton:
                # top_left_corner of window + global position of mouse - the global position of mouse when the click happened (updated from mousePressEvent) 
                self.move(self.pos() + event.globalPos() - self.clickPosition) 
                self.clickPosition = event.globalPos()
   
    def leftMenuButtonsPainter(self): 
        for buttonWidget in self.mainBodyLeftButtonsFrame.findChildren(QPushButton): 
            # buttonWidget.objectName() != self.sender().objectName() 
            defaultStyle = buttonWidget.styleSheet().replace("QPushButton{border-left: 3px solid #FFB86C;}", "") 
            buttonWidget.setStyleSheet(defaultStyle) 
            # defaultStyle = buttonWidget.styleSheet().replace("QPushButton {border-bottom: 5px solid 
            #FFB86C;}", "") 
            # buttonWidget.setStyleSheet(defaultStyle) 
        newStyle = self.sender().styleSheet() + "QPushButton{border-left: 3px solid #FFB86C;}" 
        self.sender().setStyleSheet(newStyle)    
    
    def navigationButtonLogic(self):
        width = self.mainBodyLeftButtonsFrame.width() 
        
        if width == 30: 
            newWidth = 100 
        else: 
            newWidth = 30
    
        self.animation = QPropertyAnimation(self.mainBodyLeftButtonsFrame, b"minimumWidth") 
        self.animation.setDuration(100) 
        self.animation.setStartValue(width) 
        self.animation.setEndValue(newWidth) 
        self.animation.setEasingCurve(QEasingCurve.InOutQuart) 
        self.animation.start() 
    
    def maximizeButtonLogic(self):
        if (self.IS_WINDOW_MAXIMIZED):
            self.IS_WINDOW_MAXIMIZED = False
            self.showNormal()
            self.maximizeButton.setIcon(QIcon(":/headerRightButtons/feather/maximize-2.svg")) 
        else:
            self.IS_WINDOW_MAXIMIZED = True
            self.showMaximized()
            self.maximizeButton.setIcon(QIcon(":/headerRightButtons/feather/maximize.svg")) 

    def circularGaugePainter(self, key, value): 
        circularWidget = self.circularGauges[key]
        styleSheet = """ 
            QFrame{ 
                border-radius:65px; 
                background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(68, 71, 90, 255), stop:{STOP_2} rgba(255, 184, 108, 255)); 
            } 
        """ 
    
        progress = (100-value)/100 
        progress = max(0, min(progress, 1)) 
        stop_1 = str(progress - 0.001) 
        stop_2 = str(progress) 
    
        newStyleSheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2) 
        circularWidget.setStyleSheet(newStyleSheet)
    
    def circularGaugesPixmap(self, key):
        if (key == CircularGaugesLabels.FourThrustersForwards or
            key == CircularGaugesLabels.FourThrustersBackwards or
            key == CircularGaugesLabels.FourThrustersRight or
            key == CircularGaugesLabels.FourThrustersLeft or
            key == CircularGaugesLabels.FourThrustersCW or
            key == CircularGaugesLabels.FourThrustersCCW):
            self.fourThrustersLabel.setPixmap(self.circularGaugesLabels[key])
        elif (key == CircularGaugesLabels.UpDownThrustersUP or key == CircularGaugesLabels.UpDownThrustersDOWN):
            self.upDownThrustersLabel.setPixmap(self.circularGaugesLabels[key])
        elif(key == CircularGaugesLabels.ServoCW or key == CircularGaugesLabels.ServoCCW):
            self.servoLabel.setPixmap(self.circularGaugesLabels[key])
        elif(key == CircularGaugesLabels.FourThrustersNone):
            self.fourThrustersLabel.clear()
        elif(key == CircularGaugesLabels.UpDownThrustersNone):
            self.upDownThrustersLabel.clear()
        elif(key == CircularGaugesLabels.ServoNone):
            self.servoLabel.clear()    

    def cameraSwitcher(self):
        if self.homePageStackedWidget.currentIndex() == 0:
            self.cameraButton.click()
        elif self.homePageStackedWidget.currentIndex() == 1:
            self.homeButton.click()

    def saveControllerSettingsButtonLogic(self):
        comboBoxStringActionMapping =  {
            "Led": VortexPilotAction.Led ,
            "RightGripper"  :  VortexPilotAction.RightGripper,
            "LeftGripper": VortexPilotAction.LeftGripper,
            "FluidSuction": VortexPilotAction.FluidSuction,
            "FloatingDebris": VortexPilotAction.FloatingDebris,
            "AltitudeHold": VortexPilotAction.AltitudeHold,
            "Stabilize": VortexPilotAction.Stabilize,
            "CameraSwitch": VortexPilotAction.CameraSwitch,
            "Gain": VortexPilotAction.Gain,
            "Heave": VortexPilotAction.Heave,
            "Pitch": VortexPilotAction.Pitch,
            "Roll": VortexPilotAction.Roll,
            "Servo": VortexPilotAction.Servo,
            "Surge": VortexPilotAction.Surge,
            "Sway": VortexPilotAction.Sway,
            "Yaw": VortexPilotAction.Yaw,
            "None": ""
        }

        newButtonsActionMapping = {
            JoystickButtons.A.value: comboBoxStringActionMapping[self.AButtonComboBox.currentText()],
            JoystickButtons.B.value: comboBoxStringActionMapping[self.BButtonComboBox.currentText()],
            JoystickButtons.X.value: comboBoxStringActionMapping[self.XButtonComboBox.currentText()],
            JoystickButtons.Y.value: comboBoxStringActionMapping[self.YButtonComboBox.currentText()],
            JoystickButtons.LB.value: comboBoxStringActionMapping[self.LBButtonComboBox.currentText()],
            JoystickButtons.RB.value: comboBoxStringActionMapping[self.RBButtonComboBox.currentText()],
            JoystickButtons.BACK.value: comboBoxStringActionMapping[self.BACKButtonComboBox.currentText()],
            JoystickButtons.START.value: comboBoxStringActionMapping[self.STARTButtonComboBox.currentText()],
            JoystickButtons.LEFTPAD.value: comboBoxStringActionMapping[self.LEFTPADButtonComboBox.currentText()],
            JoystickButtons.RIGHTPAD.value: comboBoxStringActionMapping[self.RIGHTPADButtonComboBox.currentText()],
            JoystickButtons.HOME.value: comboBoxStringActionMapping[self.HOMEButtonComboBox.currentText()],
        }

        newAxesActionMapping = {
            JoystickAxis.RIGHTHORIZONTALAXIS.value: comboBoxStringActionMapping[self.RIGHTHORIZONTALAXISComboBox.currentText()],
            JoystickAxis.RIGHTVERTICALAXIS.value: comboBoxStringActionMapping[self.RIGHTVERTICALAXISComboBox.currentText()],
            JoystickAxis.LEFTHORIZONTALAXIS.value: comboBoxStringActionMapping[self.LEFTHORIZONTALAXISComboBox.currentText()],
            JoystickAxis.LEFTVERTICALAXIS.value: comboBoxStringActionMapping[self.LEFTVERTICALAXISComboBox.currentText()],
            JoystickAxis.LT.value: comboBoxStringActionMapping[self.LTButtonComboBox.currentText()],
            JoystickAxis.RT.value: comboBoxStringActionMapping[self.RTButtonComboBox.currentText()],
        }

        # save settings to INI file.
        self.settingsINI.setValue("A", self.AButtonComboBox.currentText())
        self.settingsINI.setValue("B", self.BButtonComboBox.currentText())
        self.settingsINI.setValue("X", self.XButtonComboBox.currentText())
        self.settingsINI.setValue("Y", self.YButtonComboBox.currentText())
        self.settingsINI.setValue("LB", self.LBButtonComboBox.currentText())
        self.settingsINI.setValue("RB", self.RBButtonComboBox.currentText())
        self.settingsINI.setValue("BACK", self.BACKButtonComboBox.currentText())
        self.settingsINI.setValue("START", self.STARTButtonComboBox.currentText())
        self.settingsINI.setValue("LEFTPAD", self.LEFTPADButtonComboBox.currentText())
        self.settingsINI.setValue("RIGHTPAD", self.RIGHTPADButtonComboBox.currentText())
        self.settingsINI.setValue("HOME", self.HOMEButtonComboBox.currentText())
        self.settingsINI.setValue("RIGHTHORIZONTALAXIS", self.RIGHTHORIZONTALAXISComboBox.currentText())
        self.settingsINI.setValue("RIGHTVERTICALAXIS", self.RIGHTVERTICALAXISComboBox.currentText())
        self.settingsINI.setValue("LEFTHORIZONTALAXIS", self.LEFTHORIZONTALAXISComboBox.currentText())
        self.settingsINI.setValue("LEFTVERTICALAXIS", self.LEFTVERTICALAXISComboBox.currentText())
        self.settingsINI.setValue("LT", self.LTButtonComboBox.currentText())
        self.settingsINI.setValue("RT", self.RTButtonComboBox.currentText())

        # update controller events mapping
        self.pyqtControllerEvents.setButtonsActionMapping(newButtonsActionMapping=newButtonsActionMapping)
        self.pyqtControllerEvents.setAxesActionMapping(newAxesActionMapping=newAxesActionMapping)

        # click on home button
        self.homeButton.click()

    def loadControllerSettingsLogic(self):
        settingsActionMapping =  {
            "Led": VortexPilotAction.Led ,
            "RightGripper"  :  VortexPilotAction.RightGripper,
            "LeftGripper": VortexPilotAction.LeftGripper,
            "FluidSuction": VortexPilotAction.FluidSuction,
            "FloatingDebris": VortexPilotAction.FloatingDebris,
            "AltitudeHold": VortexPilotAction.AltitudeHold,
            "Stabilize": VortexPilotAction.Stabilize,
            "CameraSwitch": VortexPilotAction.CameraSwitch,
            "Gain": VortexPilotAction.Gain,
            "Heave": VortexPilotAction.Heave,
            "Pitch": VortexPilotAction.Pitch,
            "Roll": VortexPilotAction.Roll,
            "Servo": VortexPilotAction.Servo,
            "Surge": VortexPilotAction.Surge,
            "Sway": VortexPilotAction.Sway,
            "Yaw": VortexPilotAction.Yaw,
            "None": ""
        }

        newButtonsActionMapping = {
        }

        newAxesActionMapping = {
        }

        # loading joystick buttons mapping from INI file.
        if self.settingsINI.contains("A"):
            newButtonsActionMapping[JoystickButtons.A.value] = settingsActionMapping[self.settingsINI.value("A")]
            self.AButtonComboBox.setCurrentText(self.settingsINI.value("A"))
        else:
            newButtonsActionMapping[JoystickButtons.A.value] = VortexPilotAction.RightGripper
            self.AButtonComboBox.setCurrentText("RightGripper")

        if self.settingsINI.contains("B"):
            newButtonsActionMapping[JoystickButtons.B.value] = settingsActionMapping[self.settingsINI.value("B")]
            self.BButtonComboBox.setCurrentText(self.settingsINI.value("B"))
        else:
            newButtonsActionMapping[JoystickButtons.B.value] = VortexPilotAction.LeftGripper
            self.BButtonComboBox.setCurrentText("LeftGripper")

        if self.settingsINI.contains("X"):
            newButtonsActionMapping[JoystickButtons.X.value] = settingsActionMapping[self.settingsINI.value("X")]
            self.XButtonComboBox.setCurrentText(self.settingsINI.value("X"))
        else:
            newButtonsActionMapping[JoystickButtons.X.value] = VortexPilotAction.Led
            self.XButtonComboBox.setCurrentText("Led")

        if self.settingsINI.contains("Y"):
            newButtonsActionMapping[JoystickButtons.Y.value] = settingsActionMapping[self.settingsINI.value("Y")]
            self.YButtonComboBox.setCurrentText(self.settingsINI.value("Y"))
        else:
            newButtonsActionMapping[JoystickButtons.Y.value] = VortexPilotAction.FloatingDebris
            self.YButtonComboBox.setCurrentText("FloatingDebris")

        if self.settingsINI.contains("LB"):
            newButtonsActionMapping[JoystickButtons.LB.value] = settingsActionMapping[self.settingsINI.value("LB")]
            self.LBButtonComboBox.setCurrentText(self.settingsINI.value("LB"))
        else:
            newButtonsActionMapping[JoystickButtons.LB.value] = VortexPilotAction.FluidSuction
            self.LBButtonComboBox.setCurrentText("FluidSuction")

        if self.settingsINI.contains("RB"):
            newButtonsActionMapping[JoystickButtons.RB.value] = settingsActionMapping[self.settingsINI.value("RB")]
            self.RBButtonComboBox.setCurrentText(self.settingsINI.value("RB"))
        else:
            newButtonsActionMapping[JoystickButtons.RB.value] = VortexPilotAction.AltitudeHold
            self.RBButtonComboBox.setCurrentText("AltitudeHold")

        if self.settingsINI.contains("START"):
            newButtonsActionMapping[JoystickButtons.START.value] = settingsActionMapping[self.settingsINI.value("START")]
            self.STARTButtonComboBox.setCurrentText(self.settingsINI.value("START"))
        else:
            newButtonsActionMapping[JoystickButtons.START.value] = VortexPilotAction.Gain
            self.STARTButtonComboBox.setCurrentText("Gain")

        if self.settingsINI.contains("BACK"):
            newButtonsActionMapping[JoystickButtons.BACK.value] = settingsActionMapping[self.settingsINI.value("BACK")]
            self.BACKButtonComboBox.setCurrentText(self.settingsINI.value("BACK"))
        else:
            newButtonsActionMapping[JoystickButtons.BACK.value] = VortexPilotAction.Stabilize
            self.BACKButtonComboBox.setCurrentText("Stabilize")

        if self.settingsINI.contains("RIGHTPAD"):
            newButtonsActionMapping[JoystickButtons.RIGHTPAD.value] = settingsActionMapping[self.settingsINI.value("RIGHTPAD")]
            self.RIGHTPADButtonComboBox.setCurrentText(self.settingsINI.value("RIGHTPAD"))
        else:
            newButtonsActionMapping[JoystickButtons.RIGHTPAD.value] = ""
            self.RIGHTPADButtonComboBox.setCurrentText("None")

        if self.settingsINI.contains("LEFTPAD"):
            newButtonsActionMapping[JoystickButtons.LEFTPAD.value] = settingsActionMapping[self.settingsINI.value("LEFTPAD")]
            self.LEFTPADButtonComboBox.setCurrentText(self.settingsINI.value("LEFTPAD"))
        else:
            newButtonsActionMapping[JoystickButtons.LEFTPAD.value] = VortexPilotAction.CameraSwitch
            self.LEFTPADButtonComboBox.setCurrentText("CameraSwitch")

        if self.settingsINI.contains("HOME"):
            newButtonsActionMapping[JoystickButtons.HOME.value] = settingsActionMapping[self.settingsINI.value("HOME")]
            self.HOMEButtonComboBox.setCurrentText(self.settingsINI.value("HOME"))
        else:
            newButtonsActionMapping[JoystickButtons.HOME.value] = ""
            self.HOMEButtonComboBox.setCurrentText("None")

        # loading joystick axes mapping from INI file.
        if self.settingsINI.contains("RIGHTHORIZONTALAXIS"):
            newAxesActionMapping[JoystickAxis.RIGHTHORIZONTALAXIS.value] = settingsActionMapping[self.settingsINI.value("RIGHTHORIZONTALAXIS")]
            self.RIGHTHORIZONTALAXISComboBox.setCurrentText(self.settingsINI.value("RIGHTHORIZONTALAXIS"))
        else:
            newAxesActionMapping[JoystickAxis.RIGHTHORIZONTALAXIS.value] = VortexPilotAction.Sway
            self.RIGHTHORIZONTALAXISComboBox.setCurrentText("Sway")

        if self.settingsINI.contains("RIGHTVERTICALAXIS"):
            newAxesActionMapping[JoystickAxis.RIGHTVERTICALAXIS.value] = settingsActionMapping[self.settingsINI.value("RIGHTVERTICALAXIS")]
            self.RIGHTVERTICALAXISComboBox.setCurrentText(self.settingsINI.value("RIGHTVERTICALAXIS"))
        else:
            newAxesActionMapping[JoystickAxis.RIGHTVERTICALAXIS.value] = VortexPilotAction.Surge
            self.RIGHTVERTICALAXISComboBox.setCurrentText("Surge")

        if self.settingsINI.contains("LEFTHORIZONTALAXIS"):
            newAxesActionMapping[JoystickAxis.LEFTHORIZONTALAXIS.value] = settingsActionMapping[self.settingsINI.value("LEFTHORIZONTALAXIS")]
            self.LEFTHORIZONTALAXISComboBox.setCurrentText(self.settingsINI.value("LEFTHORIZONTALAXIS"))
        else:
            newAxesActionMapping[JoystickAxis.LEFTHORIZONTALAXIS.value] = VortexPilotAction.Yaw
            self.LEFTHORIZONTALAXISComboBox.setCurrentText("Yaw")

        if self.settingsINI.contains("LEFTVERTICALAXIS"):
            newAxesActionMapping[JoystickAxis.LEFTVERTICALAXIS.value] = settingsActionMapping[self.settingsINI.value("LEFTVERTICALAXIS")]
            self.LEFTVERTICALAXISComboBox.setCurrentText(self.settingsINI.value("LEFTVERTICALAXIS"))
        else:
            newAxesActionMapping[JoystickAxis.LEFTVERTICALAXIS.value] = VortexPilotAction.Heave
            self.LEFTVERTICALAXISComboBox.setCurrentText("Heave")

        if self.settingsINI.contains("RT"):
            newAxesActionMapping[JoystickAxis.RT.value] = settingsActionMapping[self.settingsINI.value("RT")]
            self.RTButtonComboBox.setCurrentText(self.settingsINI.value("RT"))
        else:
            newAxesActionMapping[JoystickAxis.RT.value] = VortexPilotAction.Servo
            self.RTButtonComboBox.setCurrentText("Servo")

        if self.settingsINI.contains("LT"):
            newAxesActionMapping[JoystickAxis.LT.value] = settingsActionMapping[self.settingsINI.value("LT")]
            self.LTButtonComboBox.setCurrentText(self.settingsINI.value("LT"))
        else:
            newAxesActionMapping[JoystickAxis.LT.value] = VortexPilotAction.Servo
            self.LTButtonComboBox.setCurrentText("Servo")

        # update controller events mapping
        self.pyqtControllerEvents.setButtonsActionMapping(newButtonsActionMapping=newButtonsActionMapping)
        self.pyqtControllerEvents.setAxesActionMapping(newAxesActionMapping=newAxesActionMapping)

    def saveCameraSettingsButtonLogic(self):
        self.comboBoxCameraLabelsMapping = {
            "Camera1": CameraLabels.MainTopLeft,
            "Camera2": CameraLabels.MainTopRight,
            "Camera3": CameraLabels.MainBottomLeft,
            "Camera4": CameraLabels.MainBottomRight,
            "Camera5": CameraLabels.SecondaryTopLeft,
            "Camera6": CameraLabels.SecondaryTopRight,
            "Camera7": CameraLabels.SecondaryBottomLeft,
            "Camera8": CameraLabels.SecondaryBottomRight
        }

        self.pyqtOakVidgearClientEvents.setCameraLabel(self.comboBoxCameraLabelsMapping[self.OAKCameraLocationComboBox.currentText()])

        self.pyqtRTSPCamera1.setSource(self.lineEditRTSPCAMERA1SourceText.text())
        self.pyqtRTSPCamera1Events.setCameraLabel(self.comboBoxCameraLabelsMapping[self.RTSPCAMERA1LocationComboBox.currentText()])

        self.pyqtRTSPCamera2.setSource(self.lineEditRTSPCAMERA2SourceText.text())
        self.pyqtRTSPCamera2Events.setCameraLabel(self.comboBoxCameraLabelsMapping[self.RTSPCAMERA2LocationComboBox.currentText()])

        self.pyqtRTSPCamera3.setSource(self.lineEditRTSPCAMERA3SourceText.text())
        self.pyqtRTSPCamera3Events.setCameraLabel(self.comboBoxCameraLabelsMapping[self.RTSPCAMERA3LocationComboBox.currentText()])

        self.pyqtRTSPCamera4.setSource(self.lineEditRTSPCAMERA4SourceText.text())
        self.pyqtRTSPCamera4Events.setCameraLabel(self.comboBoxCameraLabelsMapping[self.RTSPCAMERA4LocationComboBox.currentText()])

        self.pyqtRTSPCamera5.setSource(self.lineEditRTSPCAMERA5SourceText.text())
        self.pyqtRTSPCamera5Events.setCameraLabel(self.comboBoxCameraLabelsMapping[self.RTSPCAMERA5LocationComboBox.currentText()])

        self.pyqtRTSPCamera6.setSource(self.lineEditRTSPCAMERA6SourceText.text())
        self.pyqtRTSPCamera6Events.setCameraLabel(self.comboBoxCameraLabelsMapping[self.RTSPCAMERA6LocationComboBox.currentText()])

        self.pyqtRTSPCamera7.setSource(self.lineEditRTSPCAMERA7SourceText.text())
        self.pyqtRTSPCamera7Events.setCameraLabel(self.comboBoxCameraLabelsMapping[self.RTSPCAMERA7LocationComboBox.currentText()])

        self.pyqtRTSPCamera8.setSource(self.lineEditRTSPCAMERA8SourceText.text())
        self.pyqtRTSPCamera8Events.setCameraLabel(self.comboBoxCameraLabelsMapping[self.RTSPCAMERA8LocationComboBox.currentText()])

        self.settingsINI.setValue("OAKCameraLabel", self.OAKCameraLocationComboBox.currentText())

        self.settingsINI.setValue("RTSPCamera1Source", self.lineEditRTSPCAMERA1SourceText.text())
        self.settingsINI.setValue("RTSPCamera1Label", self.RTSPCAMERA1LocationComboBox.currentText())

        self.settingsINI.setValue("RTSPCamera2Source", self.lineEditRTSPCAMERA2SourceText.text())
        self.settingsINI.setValue("RTSPCamera2Label", self.RTSPCAMERA2LocationComboBox.currentText())

        self.settingsINI.setValue("RTSPCamera3Source", self.lineEditRTSPCAMERA3SourceText.text())
        self.settingsINI.setValue("RTSPCamera3Label", self.RTSPCAMERA3LocationComboBox.currentText())

        self.settingsINI.setValue("RTSPCamera4Source", self.lineEditRTSPCAMERA4SourceText.text())
        self.settingsINI.setValue("RTSPCamera4Label", self.RTSPCAMERA4LocationComboBox.currentText())

        self.settingsINI.setValue("RTSPCamera5Source", self.lineEditRTSPCAMERA5SourceText.text())
        self.settingsINI.setValue("RTSPCamera5Label", self.RTSPCAMERA5LocationComboBox.currentText())

        self.settingsINI.setValue("RTSPCamera6Source", self.lineEditRTSPCAMERA6SourceText.text())
        self.settingsINI.setValue("RTSPCamera6Label", self.RTSPCAMERA6LocationComboBox.currentText())

        self.settingsINI.setValue("RTSPCamera7Source", self.lineEditRTSPCAMERA7SourceText.text())
        self.settingsINI.setValue("RTSPCamera7Label", self.RTSPCAMERA7LocationComboBox.currentText())

        self.settingsINI.setValue("RTSPCamera8Source", self.lineEditRTSPCAMERA8SourceText.text())
        self.settingsINI.setValue("RTSPCamera8Label", self.RTSPCAMERA8LocationComboBox.currentText())

        self.populateHomeAndSecondaryPageCamerasList()

        # click on home button
        self.homeButton.click()

    def loadCameraSettingsLogic(self):
        self.comboBoxCameraLabelsMapping = {
            "Camera1": CameraLabels.MainTopLeft,
            "Camera2": CameraLabels.MainTopRight,
            "Camera3": CameraLabels.MainBottomLeft,
            "Camera4": CameraLabels.MainBottomRight,
            "Camera5": CameraLabels.SecondaryTopLeft,
            "Camera6": CameraLabels.SecondaryTopRight,
            "Camera7": CameraLabels.SecondaryBottomLeft,
            "Camera8": CameraLabels.SecondaryBottomRight
        }

        # loading Camera source and label mapping from INI file.
        if self.settingsINI.contains("OAKCameraLabel"):
            self.OAKCameraLocationComboBox.setCurrentText(self.settingsINI.value("OAKCameraLabel"))
            self.pyqtOakVidgearClientEvents.setCameraLabel(self.comboBoxCameraLabelsMapping[self.settingsINI.value("OAKCameraLabel")])
        else:
            self.OAKCameraLocationComboBox.setCurrentText("Camera1")
            self.pyqtOakVidgearClientEvents.setCameraLabel(self.comboBoxCameraLabelsMapping["Camera1"])

        if self.settingsINI.contains("RTSPCamera1Source"):
            self.lineEditRTSPCAMERA1SourceText.setText(self.settingsINI.value("RTSPCamera1Source"))
            self.pyqtRTSPCamera1.setSource(self.settingsINI.value("RTSPCamera1Source"))
        else:
            self.lineEditRTSPCAMERA1SourceText.setText("None")
            self.pyqtRTSPCamera1.setSource("None")

        if self.settingsINI.contains("RTSPCamera1Label"):
            self.RTSPCAMERA1LocationComboBox.setCurrentText(self.settingsINI.value("RTSPCamera1Label"))
            self.pyqtRTSPCamera1Events.setCameraLabel(self.comboBoxCameraLabelsMapping[self.settingsINI.value("RTSPCamera1Label")])
        else:
            self.RTSPCAMERA1LocationComboBox.setCurrentText("Camera1")
            self.pyqtRTSPCamera1Events.setCameraLabel(self.comboBoxCameraLabelsMapping["Camera1"])

        if self.settingsINI.contains("RTSPCamera2Source"):
            self.lineEditRTSPCAMERA2SourceText.setText(self.settingsINI.value("RTSPCamera2Source"))
            self.pyqtRTSPCamera2.setSource(self.settingsINI.value("RTSPCamera2Source"))
        else:
            self.lineEditRTSPCAMERA2SourceText.setText("None")
            self.pyqtRTSPCamera2.setSource("None")

        if self.settingsINI.contains("RTSPCamera2Label"):
            self.RTSPCAMERA2LocationComboBox.setCurrentText(self.settingsINI.value("RTSPCamera2Label"))
            self.pyqtRTSPCamera2Events.setCameraLabel(self.comboBoxCameraLabelsMapping[self.settingsINI.value("RTSPCamera2Label")])
        else:
            self.RTSPCAMERA2LocationComboBox.setCurrentText("Camera2")
            self.pyqtRTSPCamera2Events.setCameraLabel(self.comboBoxCameraLabelsMapping["Camera2"])

        if self.settingsINI.contains("RTSPCamera3Source"):
            self.lineEditRTSPCAMERA3SourceText.setText(self.settingsINI.value("RTSPCamera3Source"))
            self.pyqtRTSPCamera3.setSource(self.settingsINI.value("RTSPCamera3Source"))
        else:
            self.lineEditRTSPCAMERA3SourceText.setText("None")
            self.pyqtRTSPCamera3.setSource("None")

        if self.settingsINI.contains("RTSPCamera3Label"):
            self.RTSPCAMERA3LocationComboBox.setCurrentText(self.settingsINI.value("RTSPCamera3Label"))
            self.pyqtRTSPCamera3Events.setCameraLabel(self.comboBoxCameraLabelsMapping[self.settingsINI.value("RTSPCamera3Label")])
        else:
            self.RTSPCAMERA3LocationComboBox.setCurrentText("Camera3")
            self.pyqtRTSPCamera3Events.setCameraLabel(self.comboBoxCameraLabelsMapping["Camera3"])

        if self.settingsINI.contains("RTSPCamera4Source"):
            self.lineEditRTSPCAMERA4SourceText.setText(self.settingsINI.value("RTSPCamera4Source"))
            self.pyqtRTSPCamera4.setSource(self.settingsINI.value("RTSPCamera4Source"))
        else:
            self.lineEditRTSPCAMERA4SourceText.setText("None")
            self.pyqtRTSPCamera4.setSource("None")
     
        if self.settingsINI.contains("RTSPCamera4Label"):
            self.RTSPCAMERA4LocationComboBox.setCurrentText(self.settingsINI.value("RTSPCamera4Label"))
            self.pyqtRTSPCamera4Events.setCameraLabel(self.comboBoxCameraLabelsMapping[self.settingsINI.value("RTSPCamera4Label")])
        else:
            self.RTSPCAMERA4LocationComboBox.setCurrentText("Camera4")
            self.pyqtRTSPCamera4Events.setCameraLabel(self.comboBoxCameraLabelsMapping["Camera4"])

        if self.settingsINI.contains("RTSPCamera5Source"):
            self.lineEditRTSPCAMERA5SourceText.setText(self.settingsINI.value("RTSPCamera5Source"))
            self.pyqtRTSPCamera5.setSource(self.settingsINI.value("RTSPCamera5Source"))
        else:
            self.lineEditRTSPCAMERA5SourceText.setText("None")
            self.pyqtRTSPCamera5.setSource("None")

        if self.settingsINI.contains("RTSPCamera5Label"):
            self.RTSPCAMERA5LocationComboBox.setCurrentText(self.settingsINI.value("RTSPCamera5Label"))
            self.pyqtRTSPCamera5Events.setCameraLabel(self.comboBoxCameraLabelsMapping[self.settingsINI.value("RTSPCamera5Label")])
        else:
            self.RTSPCAMERA5LocationComboBox.setCurrentText("Camera5")
            self.pyqtRTSPCamera5Events.setCameraLabel(self.comboBoxCameraLabelsMapping["Camera5"])

        if self.settingsINI.contains("RTSPCamera6Source"):
            self.lineEditRTSPCAMERA6SourceText.setText(self.settingsINI.value("RTSPCamera6Source"))
            self.pyqtRTSPCamera6.setSource(self.settingsINI.value("RTSPCamera6Source"))
        else:
            self.lineEditRTSPCAMERA6SourceText.setText("None")
            self.pyqtRTSPCamera6.setSource("None")

        if self.settingsINI.contains("RTSPCamera6Label"):
            self.RTSPCAMERA6LocationComboBox.setCurrentText(self.settingsINI.value("RTSPCamera6Label"))
            self.pyqtRTSPCamera6Events.setCameraLabel(self.comboBoxCameraLabelsMapping[self.settingsINI.value("RTSPCamera6Label")])
        else:
            self.RTSPCAMERA6LocationComboBox.setCurrentText("Camera6")
            self.pyqtRTSPCamera6Events.setCameraLabel(self.comboBoxCameraLabelsMapping["Camera6"])

        if self.settingsINI.contains("RTSPCamera7Source"):
            self.lineEditRTSPCAMERA7SourceText.setText(self.settingsINI.value("RTSPCamera7Source"))
            self.pyqtRTSPCamera7.setSource(self.settingsINI.value("RTSPCamera7Source"))
        else:
            self.lineEditRTSPCAMERA7SourceText.setText("None")
            self.pyqtRTSPCamera7.setSource("None")

        if self.settingsINI.contains("RTSPCamera7Label"):
            self.RTSPCAMERA7LocationComboBox.setCurrentText(self.settingsINI.value("RTSPCamera7Label"))
            self.pyqtRTSPCamera7Events.setCameraLabel(self.comboBoxCameraLabelsMapping[self.settingsINI.value("RTSPCamera7Label")])
        else:
            self.RTSPCAMERA7LocationComboBox.setCurrentText("Camera7")
            self.pyqtRTSPCamera7Events.setCameraLabel(self.comboBoxCameraLabelsMapping["Camera7"])

        if self.settingsINI.contains("RTSPCamera8Source"):
            self.lineEditRTSPCAMERA8SourceText.setText(self.settingsINI.value("RTSPCamera8Source"))
            self.pyqtRTSPCamera8.setSource(self.settingsINI.value("RTSPCamera8Source"))
        else:
            self.lineEditRTSPCAMERA8SourceText.setText("None")
            self.pyqtRTSPCamera8.setSource("None")

        if self.settingsINI.contains("RTSPCamera8Label"):
            self.RTSPCAMERA8LocationComboBox.setCurrentText(self.settingsINI.value("RTSPCamera8Label"))
            self.pyqtRTSPCamera8Events.setCameraLabel(self.comboBoxCameraLabelsMapping[self.settingsINI.value("RTSPCamera8Label")])
        else:
            self.RTSPCAMERA8LocationComboBox.setCurrentText("Camera8")
            self.pyqtRTSPCamera8Events.setCameraLabel(self.comboBoxCameraLabelsMapping["Camera8"])

        self.populateHomeAndSecondaryPageCamerasList()

    def populateHomeAndSecondaryPageCamerasList(self):
        homePageCamerasLabelsList = ["Camera1", "Camera2", "Camera3", "Camera4"]
        secondaryPageCamerasLabelsList = ["Camera5", "Camera6", "Camera7", "Camera8"]
        self.homePageCamerasList.clear()
        self.secondaryPageCamerasList.clear()

        if self.OAKCameraLocationComboBox.currentText() in homePageCamerasLabelsList:
            self.homePageCamerasList.append(self.pyqtOakVidgearClient)
        elif self.OAKCameraLocationComboBox.currentText() in secondaryPageCamerasLabelsList:
            self.secondaryPageCamerasList.append(self.pyqtOakVidgearClient)

        if self.RTSPCAMERA1LocationComboBox.currentText() in homePageCamerasLabelsList:
            self.homePageCamerasList.append(self.pyqtRTSPCamera1)
        elif self.RTSPCAMERA1LocationComboBox.currentText() in secondaryPageCamerasLabelsList:
            self.secondaryPageCamerasList.append(self.pyqtRTSPCamera1)

        if self.RTSPCAMERA2LocationComboBox.currentText() in homePageCamerasLabelsList:
            self.homePageCamerasList.append(self.pyqtRTSPCamera2)
        elif self.RTSPCAMERA2LocationComboBox.currentText() in secondaryPageCamerasLabelsList:
            self.secondaryPageCamerasList.append(self.pyqtRTSPCamera2)

        if self.RTSPCAMERA3LocationComboBox.currentText() in homePageCamerasLabelsList:
            self.homePageCamerasList.append(self.pyqtRTSPCamera3)
        elif self.RTSPCAMERA3LocationComboBox.currentText() in secondaryPageCamerasLabelsList:
            self.secondaryPageCamerasList.append(self.pyqtRTSPCamera3)

        if self.RTSPCAMERA4LocationComboBox.currentText() in homePageCamerasLabelsList:
            self.homePageCamerasList.append(self.pyqtRTSPCamera4)
        elif self.RTSPCAMERA4LocationComboBox.currentText() in secondaryPageCamerasLabelsList:
            self.secondaryPageCamerasList.append(self.pyqtRTSPCamera4)

        if self.RTSPCAMERA5LocationComboBox.currentText() in homePageCamerasLabelsList:
            self.homePageCamerasList.append(self.pyqtRTSPCamera5)
        elif self.RTSPCAMERA5LocationComboBox.currentText() in secondaryPageCamerasLabelsList:
            self.secondaryPageCamerasList.append(self.pyqtRTSPCamera5)

        if self.RTSPCAMERA6LocationComboBox.currentText() in homePageCamerasLabelsList:
            self.homePageCamerasList.append(self.pyqtRTSPCamera6)
        elif self.RTSPCAMERA6LocationComboBox.currentText() in secondaryPageCamerasLabelsList:
            self.secondaryPageCamerasList.append(self.pyqtRTSPCamera6)

        if self.RTSPCAMERA7LocationComboBox.currentText() in homePageCamerasLabelsList:
            self.homePageCamerasList.append(self.pyqtRTSPCamera7)
        elif self.RTSPCAMERA7LocationComboBox.currentText() in secondaryPageCamerasLabelsList:
            self.secondaryPageCamerasList.append(self.pyqtRTSPCamera7)

        if self.RTSPCAMERA8LocationComboBox.currentText() in homePageCamerasLabelsList:
            self.homePageCamerasList.append(self.pyqtRTSPCamera8)
        elif self.RTSPCAMERA8LocationComboBox.currentText() in secondaryPageCamerasLabelsList:
            self.secondaryPageCamerasList.append(self.pyqtRTSPCamera8)
    
    def resumeHomePageCameras(self):
        for camera in self.secondaryPageCamerasList:
            camera.pause()
    
        for camera in self.homePageCamerasList:
            camera.resume()
    
    def resumeSecondaryPageCameras(self):
        for camera in self.homePageCamerasList:
            camera.pause()

        for camera in self.secondaryPageCamerasList:
            camera.resume()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Create and show the main window
    window = VortexMainWindow()
    window.show()
    
    # Execute the application
    sys.exit(app.exec_())
