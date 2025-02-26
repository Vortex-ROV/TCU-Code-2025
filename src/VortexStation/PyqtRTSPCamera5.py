import cv2
import time
from PyQt5.QtCore import QObject, QThread, pyqtSignal, QMutex, QWaitCondition, QMutexLocker

from VortexCameras import CameraManager

class PyqtRTSPCamera5(CameraManager, QThread):
    RTSPCamera5FrameEvent = pyqtSignal(object)

    def __init__(self, source):
        CameraManager.__init__(self, source)  # Explicitly call CameraManager's __init__()
        QThread.__init__(self)  # Explicitly call QThread's __init__()
        self.running = True
        self.paused = False  # Flag to control pausing
        self.mutex = QMutex()  # Mutex to synchronize threads
        self.qWaitCondition = QWaitCondition()  # Condition variable for pausing

    def run(self):
        """
        The main logic of the background thread to continuously fetch frames
        and emit them to the main GUI thread for display.
        """
        while self.running:
            # print("RTSPCAMERA5 FRAME Thread")
            with QMutexLocker(self.mutex):
                if self.paused:
                    # Wait until the paused state is set to False
                    self.qWaitCondition.wait(self.mutex)
            frame = self.readFrame()
            if frame is not None:
                self.RTSPCamera5FrameEvent.emit(frame)  # Emit frame to main thread for display
                # print("RTSPCAMERA5 FRAME EMITTED")
            time.sleep(1/30)  # Small delay to avoid maxing out CPU

    def stop(self):
        """Stop the camera stream and close resources."""
        self.running = False
        self.closeCamera()
        self.quit()
        self.wait()

    def pause(self):
        """Pause the camera stream."""
        with QMutexLocker(self.mutex):
            self.paused = True

    def resume(self):
        """Resume the camera stream."""
        with QMutexLocker(self.mutex):
            self.paused = False
            self.qWaitCondition.wakeOne()  # Notify the thread to resume