from PyQt5.QtCore import QObject
from VortexStation.VortexWidgetNamesEnums import VortexPilotAction, JoystickButtons, JoystickAxis

class PyqtControllerEvents(QObject):
    def __init__(self, pilotActionsExecutor):
        super().__init__()

        self.pilotActionsExecutor = pilotActionsExecutor

        self.buttonsActionMapping = {
            JoystickButtons.A.value: VortexPilotAction.RightGripper,
            JoystickButtons.B.value: VortexPilotAction.LeftGripper,
            JoystickButtons.X.value: VortexPilotAction.Led,
            JoystickButtons.Y.value: VortexPilotAction.FloatingDebris,
            JoystickButtons.LB.value: VortexPilotAction.FluidSuction,
            JoystickButtons.RB.value: VortexPilotAction.AltitudeHold,
            JoystickButtons.BACK.value: VortexPilotAction.Stabilize,
            JoystickButtons.START.value: VortexPilotAction.Gain,
            JoystickButtons.LEFTPAD.value: VortexPilotAction.CameraSwitch,
            JoystickButtons.RIGHTPAD.value: "",
            JoystickButtons.HOME.value: "",
        }

        self.hatsActionMapping = {

        }

        self.axesActionMapping = {
            JoystickAxis.RIGHTHORIZONTALAXIS.value: VortexPilotAction.Sway,
            JoystickAxis.RIGHTVERTICALAXIS.value: VortexPilotAction.Surge,
            JoystickAxis.LEFTHORIZONTALAXIS.value: VortexPilotAction.Yaw,
            JoystickAxis.LEFTVERTICALAXIS.value: VortexPilotAction.Heave,
            JoystickAxis.LT.value: VortexPilotAction.Servo,
            JoystickAxis.RT.value: VortexPilotAction.Servo,
        }
        
    def button0Event(self, controller, controllerName, button_id, event, value):
        # print("Button{}Event: controller:{}, controllerName:{}, event:{}, value:{}".format(button_id, controller, controllerName, event, value))
        self.pilotActionsExecutor(self.buttonsActionMapping[button_id], event)

    def button1Event(self, controller, controllerName, button_id, event, value):
        # print("Button{}Event: controller:{}, controllerName:{}, event:{}, value:{}".format(button_id, controller, controllerName, event, value))
        self.pilotActionsExecutor(self.buttonsActionMapping[button_id], event)
        
    def button2Event(self, controller, controllerName, button_id, event, value):
        # print("Button{}Event: controller:{}, controllerName:{}, event:{}, value:{}".format(button_id, controller, controllerName, event, value))
        self.pilotActionsExecutor(self.buttonsActionMapping[button_id], event)
        
    def button3Event(self, controller, controllerName, button_id, event, value):
        # print("Button{}Event: controller:{}, controllerName:{}, event:{}, value:{}".format(button_id, controller, controllerName, event, value))
        self.pilotActionsExecutor(self.buttonsActionMapping[button_id], event)
        
    def button4Event(self, controller, controllerName, button_id, event, value):
        # print("Button{}Event: controller:{}, controllerName:{}, event:{}, value:{}".format(button_id, controller, controllerName, event, value))
        self.pilotActionsExecutor(self.buttonsActionMapping[button_id], event)
                    
    def button5Event(self, controller, controllerName, button_id, event, value):
        # print("Button{}Event: controller:{}, controllerName:{}, event:{}, value:{}".format(button_id, controller, controllerName, event, value))
        self.pilotActionsExecutor(self.buttonsActionMapping[button_id], event)
                    
    def button6Event(self, controller, controllerName, button_id, event, value):
        # print("Button{}Event: controller:{}, controllerName:{}, event:{}, value:{}".format(button_id, controller, controllerName, event, value))
        self.pilotActionsExecutor(self.buttonsActionMapping[button_id], event)
                    
    def button7Event(self, controller, controllerName, button_id, event, value):
        # print("Button{}Event: controller:{}, controllerName:{}, event:{}, value:{}".format(button_id, controller, controllerName, event, value))
        self.pilotActionsExecutor(self.buttonsActionMapping[button_id], event)
                    
    def button8Event(self, controller, controllerName, button_id, event, value):
        # print("Button{}Event: controller:{}, controllerName:{}, event:{}, value:{}".format(button_id, controller, controllerName, event, value))
        self.pilotActionsExecutor(self.buttonsActionMapping[button_id], event)
                    
    def button9Event(self, controller, controllerName, button_id, event, value):
        # print("Button{}Event: controller:{}, controllerName:{}, event:{}, value:{}".format(button_id, controller, controllerName, event, value))
        self.pilotActionsExecutor(self.buttonsActionMapping[button_id], event)
                    
    def button10Event(self, controller, controllerName, button_id, event, value):
        # print("Button{}Event: controller:{}, controllerName:{}, event:{}, value:{}".format(button_id, controller, controllerName, event, value))
        self.pilotActionsExecutor(self.buttonsActionMapping[button_id], event)
        
    def hat0Event(self, controller, controllerName, hat_id, event, value):       
        pass 
        # print("hat{}Event: controller:{}, controllerName:{}, event:{}, value:{}".format(hat_id, controller, controllerName, event, value))
    
    def axis0Event(self, controller, controllerName, axis_id, event, value):
        # print("axis{}Event: controller:{}, controllerName:{}, event:{}, value:{}".format(axis_id, controller, controllerName, event, value))
        value_pwm = int(round(((value + 1) * (1900 - 1100) / 2) + 1100))
        self.pilotActionsExecutor(self.axesActionMapping[axis_id], value_pwm)

    def axis1Event(self, controller, controllerName, axis_id, event, value):
        # print("axis{}Event: controller:{}, controllerName:{}, event:{}, value:{}".format(axis_id, controller, controllerName, event, value))
        value_pwm = int(round(((1 - value) * (1900 - 1100) / 2) + 1100))
        self.pilotActionsExecutor(self.axesActionMapping[axis_id], value_pwm)

    def axis2Event(self, controller, controllerName, axis_id, event, value):
        # print("axis{}Event: controller:{}, controllerName:{}, event:{}, value:{}".format(axis_id, controller, controllerName, event, value))
        value_pwm = int(round(((value + 1) * (1900 - 1100) / 2) + 1100))
        self.pilotActionsExecutor(self.axesActionMapping[axis_id], value_pwm)

    def axis3Event(self, controller, controllerName, axis_id, event, value):
        # print("axis{}Event: controller:{}, controllerName:{}, event:{}, value:{}".format(axis_id, controller, controllerName, event, value))
        value_pwm = int(round(((1 - value) * (1900 - 1100) / 2) + 1100))
        self.pilotActionsExecutor(self.axesActionMapping[axis_id], value_pwm)

    def axis4Event(self, controller, controllerName, axis_id, event, value):
        # print("axis{}Event: controller:{}, controllerName:{}, event:{}, value:{}".format(axis_id, controller, controllerName, event, value))
        value_pwm = int(round(((1 - value) * (1500 - 1100) / 2) + 1100))
        self.pilotActionsExecutor(self.axesActionMapping[axis_id], value_pwm)

    def axis5Event(self, controller, controllerName, axis_id, event, value):
        # print("axis{}Event: controller:{}, controllerName:{}, event:{}, value:{}".format(axis_id, controller, controllerName, event, value))
        value_pwm = int(round(((value + 1) * (1900 - 1500) / 2) + 1500))
        self.pilotActionsExecutor(self.axesActionMapping[axis_id], value_pwm)
    
    def setButtonsActionMapping(self, newButtonsActionMapping):
        self.buttonsActionMapping = newButtonsActionMapping
    
    def setAxesActionMapping(self, newAxesActionMapping):
        self.axesActionMapping = newAxesActionMapping
