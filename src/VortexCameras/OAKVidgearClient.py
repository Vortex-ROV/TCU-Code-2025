import simplejpeg
import cv2
from vidgear.gears import NetGear
import threading
import sys
from VortexInterfaces import OAKVidgearClientInterfaces

class OAKVidgearClient(OAKVidgearClientInterfaces):
    """
    This class handles the creation of a NetGear client to receive video frames over the network,
    with support for thread-safe frame retrieval and controlled client shutdown.
    """
    
    def __init__(self, ipAddress="192.168.33.100", port="5454", options=None):
        """
        Initializes the OAKVidgearClient with connection parameters and options.
        
        :param ipAddress: The IP address of the NetGear server.
        :param port: The port number of the NetGear server.
        :param options: Optional dictionary to specify custom connection settings.
        """
        # Default options if none provided by the user
        if options is None:
            options = {
                "jpeg_compression": True,  # Enable JPEG compression for video stream
                "jpeg_compression_quality": 90,  # Set the quality of JPEG compression
                "jpeg_compression_fastdct": True,  # Enable fast Discrete Cosine Transform for compression
                "jpeg_compression_fastupsample": True,  # Enable fast upsampling for JPEG compression
                "max_retries": sys.maxsize,  # Set max retries to avoid network issues
            }
        
        # NetGear client setup for receiving video stream
        self.client = NetGear(
            receive_mode=True,  # Set to receive mode (not sending)
            address=ipAddress,  # Specify the IP address to connect to
            port=port,  # Specify the port to connect to
            protocol="tcp",  # Use TCP protocol for communication
            pattern=1,  # Frame pattern, typically 1 for standard streaming
            logging=True,  # Enable logging for debugging
            **options,  # Include any additional options passed to the constructor
        )
        
        # Lock for thread-safe access to the current frame
        self.lock = threading.Lock()
        
        # Initialize current frame to None (frame will be updated with new data)
        self.currentFrame = None
        
        # Flag to control whether the client is still running
        self.running = True

        # Flag to control pausing the thread
        self.paused = False
        
        # Condition variable to pause/resume the thread
        self.waitCondition = threading.Condition()

        # Add a VideoWriter object
        self.videoWriter = None

        # Flag to check if recording is in progress
        self.isRecording = False

    def startOAKVidgearThread(self):
        """
        Starts the background thread to receive frames continuously.
        The thread will run the internal method `_receiveFrames` to fetch frames.
        """
        # Create and start a new thread to receive frames
        receivingThread = threading.Thread(target=self._receiveFrames)
        
        # Make the thread a daemon thread so it will automatically exit when the main program exits
        receivingThread.daemon = True
        receivingThread.start()

    def _receiveFrames(self):
        """
        Internal method that continuously receives frames from the NetGear client.
        This runs on a background thread to avoid blocking the main program.
        The received frame is stored in `currentFrame` with thread-safety provided by a lock.
        """
        while self.running:
            # print("OAK CLIENT THREAD")
            with self.waitCondition:
                while self.paused:
                    self.waitCondition.wait()  # Wait until resumed

            # Receive the frame from the NetGear server
            frame = self.client.recv()

            # If no frame is received (None), stop the loop
            if frame is None:
                break
            
            # Lock the frame to ensure thread-safe updates
            with self.lock:
                self.currentFrame = frame
            # print("OAK CLIENT Frame")

    def getFrame(self):
        """
        Thread-safe method to retrieve the latest received frame.
        
        :return: The current video frame if available, otherwise None.
        """
        # Lock the access to the frame to ensure no other thread can modify it while being read
        with self.lock:
            return self.currentFrame

    def stopOAKVidgearThread(self):
        """
        Stops the background thread from receiving frames and closes the NetGear client.
        This method should be called when you want to cleanly shut down the client.
        """
        # Set the running flag to False to stop receiving frames
        self.running = False
        
        # Close the NetGear client to free up resources
        self.client.close()

    def pauseOAKVidgearThread(self):
        """Pause the frame receiving thread."""
        with self.waitCondition:
            self.paused = True

    def resumeOAKVidgearThread(self):
        """Resume the frame receiving thread."""
        with self.waitCondition:
            self.paused = False
            self.waitCondition.notify()  # Wake the thread to continue receiving frames

    def startRecording(self, filename, frameRate, resolution):
        """
        Starts recording frames to an MP4 file.

        :param filename: the name of the output MP4 file
        :param frameRate: frames per second to record at
        :param resolution: resolution (width, height) of the video
        """
        if self.isRecording:
            print("Recording already in progress. Cannot start a new recording.")
            return  # Don't start recording if it's already in progress

        self.isRecording = True
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use 'mp4v' codec for MP4 file
        self.videoWriter = cv2.VideoWriter(filename, fourcc, frameRate, resolution)

        print(f"Recording started and saving to {filename}")

    def stopRecording(self):
        """
        Stops recording and saves the video file.
        """
        if self.isRecording:
            self.isRecording = False
            if self.videoWriter is not None:
                self.videoWriter.release()
                self.videoWriter = None
                print("Recording stopped.")
        else:
            print("No recording is in progress.")
    
    def writeFrame(self, frame):
        """
        Writes a frame to the recording video if recording is active.

        :param frame: the frame to write
        """
        if self.isRecording and self.videoWriter is not None:
            self.videoWriter.write(frame)
        else:
            print("No Recording in progress")