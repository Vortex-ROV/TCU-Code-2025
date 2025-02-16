import matplotlib.pyplot as plt
import numpy as np
import serial
import time as tm
from threading import Thread, Event

class DepthPlotter:
    def __init__(self, port='COM8', baudrate=115200, timeout=5):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.time = []
        self.depth = []
        self.stop_event = Event()
        self.read_thread = None  # Ensure thread safety

    def read_data(self):
        def read_from_port():
            try:
                with serial.Serial(self.port, self.baudrate, timeout=self.timeout) as ser:
                    while not self.stop_event.is_set():
                        if ser.in_waiting > 0:
                            line = ser.readline().decode('utf-8', errors='ignore').strip()
                            try:
                                parts = line.split()
                                timestamp = parts[1]
                                depth = parts[3]
                                d = float(depth)
                                self.time.append(((float(timestamp.split(':')[0]))*60*60) + ((float(timestamp.split(':')[1]))*60) + float(timestamp.split(':')[2]))
                                self.depth.append(d)
                            except (ValueError, IndexError) as e:
                                print(f"Error parsing line: {line}. Error: {e}")
                                continue
            except serial.SerialException as e:
                print(f"Error opening serial port: {e}")

        self.stop_event.clear()
        self.read_thread = Thread(target=read_from_port, daemon=True)
        self.read_thread.start()

    def is_connected(self):
        try:
            with serial.Serial(self.port, self.baudrate, timeout=self.timeout) as ser:
                return ser.is_open
        except serial.SerialException as e:
            print(f"Error opening serial port: {e}")
            return False
        
    def detection(self):
        def detect_connection():
            connection_established = False
            try:
                while not connection_established:
                    try:
                        with serial.Serial(self.port, self.baudrate, timeout=self.timeout) as ser:
                            connection_established = True  # Change to True when connection is established
                            print("Connection established***************************************************************p")  # Print when connection is established
                            while not self.stop_event.is_set():
                                if ser.in_waiting > 0:
                                    line = ser.readline().decode('utf-8', errors='ignore').strip()
                                    try:
                                        parts = line.split()
                                        timestamp = parts[1]
                                        depth = parts[3]
                                        d = float(depth)
                                        self.time.append(((float(timestamp.split(':')[0]))*60*60) + ((float(timestamp.split(':')[1]))*60) + float(timestamp.split(':')[2]))
                                        self.depth.append(d)
                                    except (ValueError, IndexError) as e:
                                        print(f"Error parsing line: {line}. Error: {e}")
                                        continue
                    except serial.SerialException as e:
                        print(f"Error opening serial port: {e}")
                        print("Trying to connect to something")
                        tm.sleep(5 )
            except Exception as e:
                print(f"Error: {e}")


        self.stop_event.clear()
        self.detection_thread = Thread(target=detect_connection, daemon=True)
        self.detection_thread.start()

        return self.detection

    def stop_reading(self):
        self.stop_event.set()
        if self.read_thread:
            self.read_thread.join()

    def plot_data(self, canvas):
        if len(self.time) == 0 or len(self.depth) == 0:
            print("No data to plot")
            return

        time = np.array(self.time)
        depth = np.array(self.depth)

        ax = canvas.figure.gca()
        ax.clear()
        ax.axhline(2.5, color='black', linewidth=1, linestyle='--', label='Threshold 2.5m')
        ax.axhline(1.0, color='black', linewidth=1, linestyle='--', label='Threshold 1.0m')
        ax.plot(time, depth, label='Depth vs. Time', color='blue')

        ax.set_xlabel('Time (seconds)')
        ax.set_ylabel('Depth (meters)')
        ax.set_title('Depth vs. Time')

        ax.legend()
        ax.grid(True)
        canvas.draw()
