import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizeGrip, QPushButton
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, QSettings
from PyQt5.QtGui import QIcon, QPixmap
from VortexStation.PyqtCompanionController import PyqtCompanionController
from VortexStation.PyqtCompanionControllerEvents import PyqtCompanionControllerEvents
from VortexStation.PyqtController import PyqtController
from VortexStation.PyqtControllerEvents import PyqtControllerEvents
from VortexStation.VortexPilotProxy import VortexPilotProxy
from VortexStation.UI_MainWindow import Ui_MainWindow
from VortexStation.VortexWidgetNamesEnums import CircularGauge, Indicators, VortexPilotAction, JoystickButtons, JoystickAxis, CircularGaugesLabels, Readings
from VortexPilot.PilotAdapter import PilotAdapter
from VortexPilot.ROVController import ROVController
from VortexPilot.VortexPilot import VortexPilot
from VortexController.JoystickHandler import JoystickHandler
from VortexController.VortexController import Controller
from VortexController.ControllerAdapter import ControllerAdapter
from VortexCompanionController.VortexCompanionController import CompanionController

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
        self.cameraButton.clicked.connect(lambda:self.homePageStackedWidget.setCurrentWidget(self.secondayHomePage)) 
        self.cameraButton.clicked.connect(lambda:self.mainBodyStackedWidget.setCurrentWidget(self.homePage)) 
        self.settingsButton.clicked.connect(lambda: self.mainBodyStackedWidget.setCurrentWidget(self.settingsPage))
        self.controllerSettingsButton.clicked.connect(lambda: self.mainBodyStackedWidget.setCurrentWidget(self.controllerSettingsPage))

        # SettingsPage Button Logic
        self.saveSettingButton.clicked.connect(lambda: self.saveSettingsButtonLogic())

        # Main Body Left Buttons Styling
        for buttonWidget in self.mainBodyLeftButtonsFrame.findChildren(QPushButton): 
            buttonWidget.clicked.connect(lambda: self.leftMenuButtonsPainter())
        
        # header frame logic
        self.headerFrame.mouseMoveEvent = self.moveWindow

        # Create a QSettings instance with the custom file path (using IniFormat) to save custom settings.
        self.settingsINI = QSettings(os.path.join(os.path.expanduser("~/Documents"), "VortexUI.ini"), QSettings.IniFormat)
        self.loadSettingsLogic()
    
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
    
    def saveSettingsButtonLogic(self):
        # click on home button
        self.homeButton.click()

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

    def loadSettingsLogic(self):
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
            self.AButtonComboBox.setCurrentText("LeftGripper")

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
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Create and show the main window
    window = VortexMainWindow()
    window.show()
    
    # Execute the application
    sys.exit(app.exec_())
