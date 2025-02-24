import pygame
import json
import time
from VortexController import Controller

def JoystickTest():
    """
    Example usage of the ControllerDataCollector class.
    
    This block of code initializes the Pygame display, creates an instance of the
    ControllerDataCollector, and enters the main game loop where controller and keyboard
    input data is collected, printed to the console, and updated every 2 seconds.
    """

    # Initialize the Pygame display (needed to capture events)
    screen = pygame.display.set_mode((640, 480))  # Initialize display window

    # Create the ControllerDataCollector instance
    collector = Controller()

    # Main game loop
    running = True
    while running:
        # Collect controller data through the `getControllerData` method
        controller_data = collector.getControllerData()

        # Pretty-print the controller data in JSON format
        print("Controller and Keyboard Data:")
        print(json.dumps(controller_data, indent=4))  # Pretty-print controller data with indentation

        # Handle events like window close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Exit the loop if the window is closed

        # Sleep for 2 seconds to prevent flooding the console with too many outputs
        time.sleep(2)

    pygame.quit()  # Quit Pygame when the loop is finished
