from PyQt5.QtCore import QObject, QThread, pyqtSignal, QMutex, QWaitCondition, QMutexLocker
from VortexCameras import OAKVidgearClient  # Assuming OAKVidgearClient is imported correctly
import time

class PyqtOakVidgearClient(OAKVidgearClient, QThread):
    """
    Subclassing both QThread and OAKVidgearClient directly to handle video frames
    and processing in a separate thread without blocking the main GUI thread.
    """

    # Signal declaration to send frames to the GUI thread
    oakFrameEvent = pyqtSignal(object)

    def __init__(self, ipAddress="192.168.33.100", port="5454", options=None):
        """
        Initialize both QThread and OAKVidgearClient by passing arguments accordingly.
        """
        QThread.__init__(self)  # Initialize QThread
        OAKVidgearClient.__init__(self, ipAddress=ipAddress, port=port, options=options)

        self.running = True
        self.paused = False  # Flag to control pausing
        self.mutex = QMutex()  # Mutex to synchronize threads
        self.qWaitCondition = QWaitCondition()  # Condition variable for pausing
        # Start receiving frames
        self.startOAKVidgearThread()

    def run(self):
        """
        This method will be executed in a separate thread when the thread starts.
        Continuously retrieve frames from the OAKVidgearClient and emit them to the GUI thread.
        """
        while self.running:
            # print("OAK FRAME Thread")
            with QMutexLocker(self.mutex):
                if self.paused:
                    # Wait until the paused state is set to False
                    self.qWaitCondition.wait(self.mutex)
            # Fetch the latest frame using the client’s thread-safe getFrame() method
            frame = self.getFrame()
            if frame is not None:
                # Resize frame and emit it to the GUI thread
                self.oakFrameEvent.emit(frame)
                # print("OAK FRAME EMITTED")
            time.sleep(1/30)  # Small delay to avoid maxing out CPU

    def stop(self):
        """
        Stop the receiving process and end the thread properly.
        """
        self.stopOAKVidgearThread()  # Assuming stopReceiving exists in OAKVidgearClient
        self.running = False
        self.quit()  # This ensures the QThread stops and exits its event loop

    def pause(self):
        """Pause the camera stream."""
        with QMutexLocker(self.mutex):
            self.paused = True
        self.pauseOAKVidgearThread()

    def resume(self):
        """Resume the camera stream."""
        with QMutexLocker(self.mutex):
            self.paused = False
            self.qWaitCondition.wakeOne()  # Notify the thread to resume
        self.resumeOAKVidgearThread()