import cv2
from VortexCameras import CameraManager


def CameraManagerTest():
    
    stream = CameraManager(source=0)  # Initialize with the default camera (0)
    
    stream.openCamera(maxTries=3)  # Attempt to open the camera with a maximum of 3 tries
    
    # Capture 10 frames or until the user interrupts
    for i in range(10):
        frame = stream.readFrame()
        if frame is not None:
            # Do something with the frame (e.g. display it)
            cv2.imshow("Frame", frame)
        
        # Example of changing the source after 5 frames
        if i == 5:
            stream.setSource(1)  # Change the source to camera 1 (or a different video file)
        
        # Exit loop if user presses 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    stream.closeCamera()  # Close the camera when done
    cv2.destroyAllWindows()