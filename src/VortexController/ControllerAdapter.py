from VortexController.JoystickHandler import JoystickHandler
from VortexInterfaces.ControllerInterfaces import ControllerInterfaces

class ControllerAdapter(ControllerInterfaces):
    def __init__(self, joystick_handler: JoystickHandler):
        self.joystick_handler = joystick_handler

    def getControllerData(self):
        self.joystick_handler.handle_joy()
        controller_data = self.getInitialControllerData()
        data = self.joystick_handler.print_results()

        # buttons = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
        buttons = ["a", "b", "c", "d", "e", "f", "g", "h"]
        for index, button in enumerate(buttons):
            event_name = "JOYBUTTONDOWN" if data[button] else "JOYBUTTONUP"
            value = 1 if data[button] else 0
            controller_data["Controller_0"]["buttons"][index] = {
                "event": event_name,
                "value": value
            }

        for axis in range(6):
            event_name = "JOYAXISMOTION"
            controller_data["Controller_0"]["axes"][axis] = {
                "event": event_name,
                "value": data[axis]
            }


        hats = {"up": (0, 1), "down": (0, -1), "left": (-1, 0), "right": (1, 0)}
        for index, hat in enumerate(hats):
            if data[hat]:
                event_name = "JOYHATMOTION"
                controller_data["Controller_0"]["hats"][0] = {
                    "event": event_name,
                    "value": hats[hat]
                }

        return controller_data


    def getInitialControllerData(self):
        controller_data = {}

        # Initialize all buttons, axes, and hats for each controller with default values
        controller_name = f"Controller_0"

        # Initialize dictionary for the controller (joystick/gamepad)
        controller_data[controller_name] = {
            "name": "Xbox 360 Controller",  # Store the actual controller name
            "buttons": {},  # Placeholder for button data
            "axes": {},  # Placeholder for axis data
            "hats": {}  # Placeholder for hat data
        }

        # Initialize buttons with default values (all buttons are not pressed)
        for button in range(12):
            controller_data[controller_name]["buttons"][button] = {
                "event": None,
                "value": 0  # Default value of button (not pressed)
            }

        # Initialize axes with default values (all axes are centered)
        for axis in range(6):
            controller_data[controller_name]["axes"][axis] = {
                "event": None,
                "value": 0.0  # Default value for axis (centered)
            }

        # Initialize hats (4-way input) with default values (no direction)
        for hat in range(4):
            controller_data[controller_name]["hats"][hat] = {
                "event": None,
                "value": (0, 0)  # Default value for hat (no direction)
            }

        return controller_data
