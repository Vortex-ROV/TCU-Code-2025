from abc import ABCMeta, abstractmethod, ABC
from PyQt5.QtCore import QObject

# Define a metaclass that inherits both from PyQt's QObject and ABCMeta for abstract classes
class ControllerMeta(type(QObject), ABCMeta):
    pass


# Abstract base class that defines the interface for collecting controller data
class ControllerInterfaces(ABC, metaclass=ControllerMeta):
    """
    Abstract base class for Controller data collection.
    
    This class defines an interface for collecting controller data (joystick). 
    Any subclass must implement the following methods:
    - `getControllerData()`: This method returns the current state of the controllers, including buttons, axes, and hats.
    - `getInitialControllerData()`: This method initializes and returns the data structure for controllers, 
      with all buttons, axes, and hats set to their default values.
    """
    
    abstractmethod
    def getControllerData(self):
        """
        Abstract method to get controller data (joystick).
        
        This method must be implemented by subclasses to collect joystick events, 
        button states, axis values, and hat values.
        
        Returns:
            dict: A dictionary containing controller data (buttons, axes, hats states).
        """
        pass

    abstractmethod
    def getInitialControllerData(self):
        """
        Abstract method to initialize and return the initial controller data.
        
        This method prepares a data structure with the default values for buttons, axes,
        and hats for each connected controller. The structure is meant to be used as the 
        initial state before collecting any joystick events.
        
        Returns:
            dict: A dictionary with the initial state of all controllers, with all buttons set to 0, 
                  axes set to 0.0 (centered), and hats set to (0, 0) (no direction).
        """
        pass