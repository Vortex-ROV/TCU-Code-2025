import pygame

from VortexInterfaces import ControllerInterfaces

# Controller class that implements the ControllerInterface for collecting joystick data
class Controller(ControllerInterfaces):
    """
    Collects and processes joystick data.
    
    This class implements the `ControllerInterface` and is responsible for 
    initializing and managing connected controllers (joysticks/gamepads), 
    recording input events (e.g., button presses, axis movements, hat changes), 
    and collecting input data in a structured format.
    """
    
    def __init__(self):
        """
        Initializes the ControllerDataCollector.
        
        Sets up the Pygame environment, initializes controllers, and prepares 
        the data structure for storing joystick input.
        """
        pygame.init()  # Initialize Pygame library to handle events and controllers
        self.controllers = []  # List to store active controllers (joysticks)
        self.updateControllers()  # Update the list of controllers at the start

    def updateControllers(self):
        """
        Update the list of active controllers.
        
        This method checks the number of connected controllers (joysticks or gamepads),
        adds new ones to the list, and removes any disconnected controllers. It ensures that 
        the list of controllers is always up-to-date.
        """
        # Remove all controllers
        for controller in self.controllers[:]:
            self.controllers.remove(controller)
            controller.quit()  # Quit the controller that was removed

        joystick_count = pygame.joystick.get_count()  # Get the count of currently connected joysticks
        current_controllers = [pygame.joystick.Joystick(i) for i in range(joystick_count)]

        # Add new controllers (if they are not already in the list)
        for controller in current_controllers:
            if controller not in self.controllers:
                controller.init()  # Initialize the new controller
                self.controllers.append(controller)

    def getInitialControllerData(self):
        """
        Initializes and prepares a structure for controller data.
        
        Before processing events, we need to prepare the initial data structure
        to store the buttons, axes, and hats for each controller. This method sets
        the default values for all buttons, axes, and hats for every controller.
        
        Returns:
            dict: A dictionary containing initialized controller data with default values.
        """
        controller_data = {}

        # Initialize all buttons, axes, and hats for each controller with default values
        for controller_index, controller in enumerate(self.controllers):
            controller_name = f"Controller_{controller_index}"

            # Initialize dictionary for the controller (joystick/gamepad)
            controller_data[controller_name] = {
                "name": controller.get_name(),  # Store the actual controller name
                "buttons": {},  # Placeholder for button data
                "axes": {},  # Placeholder for axis data
                "hats": {}  # Placeholder for hat data
            }

            # Initialize buttons with default values (all buttons are not pressed)
            for button in range(controller.get_numbuttons()):
                controller_data[controller_name]["buttons"][button] = {
                    "event": None,
                    "value": 0  # Default value of button (not pressed)
                }

            # Initialize axes with default values (all axes are centered)
            for axis in range(controller.get_numaxes()):
                controller_data[controller_name]["axes"][axis] = {
                    "event": None,
                    "value": 0.0  # Default value for axis (centered)
                }

            # Initialize hats (4-way input) with default values (no direction)
            for hat in range(controller.get_numhats()):
                controller_data[controller_name]["hats"][hat] = {
                    "event": None,
                    "value": (0, 0)  # Default value for hat (no direction)
                }

        return controller_data

    def getControllerData(self):
        """
        Collect and update controller (joystick) input data.
        
        This method processes all joystick events (button presses, 
        axis movements, and hat motions), stores their values, 
        and returns a structured dictionary containing all the updated data.
        
        The returned dictionary contains:
        - "buttons": A dictionary with the states of joystick/gamepad buttons.
        - "axes": A dictionary with the current values of joystick/gamepad axes.
        - "hats": A dictionary with the direction values of joystick/gamepad hats.

        Returns:
            dict: A structured dictionary containing updated controller data (joystick).
        """
        # Initialize data structure with default values for buttons, axes, and hats
        controller_data = self.getInitialControllerData()

        # Process the events in the Pygame event queue
        for event in pygame.event.get():
            # Handle device added or removed events
            if event.type == pygame.JOYDEVICEADDED or event.type == pygame.JOYDEVICEREMOVED:
                self.updateControllers()  # Update the list of controllers
                continue  # Skip processing for device added/removed events

            # Record joystick button events (button down or up)
            if event.type == pygame.JOYBUTTONDOWN or event.type == pygame.JOYBUTTONUP:
                controller_name = f"Controller_{event.joy}"
                event_name = "JOYBUTTONDOWN" if event.type == pygame.JOYBUTTONDOWN else "JOYBUTTONUP"
                controller_data[controller_name]["buttons"][event.button] = {
                    "event": event_name,
                    "value": pygame.joystick.Joystick(event.joy).get_button(event.button) # Value is 1 for button down, 0 for button up
                }

            # Record axis motion events
            elif event.type == pygame.JOYAXISMOTION:
                controller_name = f"Controller_{event.joy}"
                controller_data[controller_name]["axes"][event.axis] = {
                    "event": "JOYAXISMOTION",
                    "value": event.value  # Store the actual axis value between -1.0 and 1.0
                }

            # Record hat motion events
            elif event.type == pygame.JOYHATMOTION:
                controller_name = f"Controller_{event.joy}"
                controller_data[controller_name]["hats"][event.hat] = {
                    "event": "JOYHATMOTION",
                    "value": event.value  # Store the hat direction as a tuple (x, y)
                }

        return controller_data

