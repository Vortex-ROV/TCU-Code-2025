from abc import ABCMeta, abstractmethod, ABC
from PyQt5.QtCore import QObject

class CameraManagerMeta(type(QObject), ABCMeta):
    pass


class CameraManagerInterfaces(ABC, metaclass=CameraManagerMeta):
    """
    Abstract base class that defines the interface for a Camera Manager.

    This class provides the blueprint for implementing camera management functionality, including
    opening and closing the camera, reading frames from the camera, and changing the video source.

    Concrete implementations of this interface must provide their own versions of the abstract methods
    to interact with a camera or video source.

    Subclasses should implement the following methods:
        - openCamera: Open the camera or video source.
        - closeCamera: Close the camera or video source.
        - readFrame: Read a frame from the camera/video source.
        - setSource: Change the source of the camera or video stream.
    """
    
    @abstractmethod
    def openCamera(self, retryInterval=2, maxTries=5):
        """
        Open the camera or video source.

        This method should attempt to open the camera or video stream, retrying if it fails.
        The retry interval and maximum number of retries are configurable.

        Args:
            retryInterval (int): The number of seconds to wait before retrying if the camera fails to open. Default is 2 seconds.
            maxTries (int): The maximum number of attempts to open the camera. Default is 5.
        """
        pass

    @abstractmethod  
    def closeCamera(self):
        """
        Close the camera or video source.

        This method should release any resources associated with the camera or video stream,
        effectively closing the capture device.
        """
        pass
    
    @abstractmethod  
    def readFrame(self):
        """
        Read a frame from the camera or video source.

        This method should retrieve a single frame from the camera or video stream. If the frame cannot
        be read, the camera should be reopened automatically.

        Returns:
            frame: A frame (image) from the camera or video source.
            None: If the frame could not be read and the camera needs to be reopened.
        """
        pass
    
    @abstractmethod 
    def setSource(self, newSource):
        """
        Change the camera or video source.

        This method should allow changing the source (e.g., switch between multiple cameras or video files).

        Args:
            newSource: The new camera index or video file path to be used as the source.
        """
        pass

    @abstractmethod 
    def startRecording(self, filename, frame_rate, resolution):
        pass

    @abstractmethod 
    def stopRecording(self):
        pass

    @abstractmethod 
    def writeFrame(self, frame):
        pass
