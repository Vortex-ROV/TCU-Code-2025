import os

from PyQt5.QtCore import QThread

class Worker(QThread):
    def __init__(self, function, *args, **kwargs):
        super().__init__()
        self.args = args
        self.kwargs = kwargs
        self.function = function

    def run(self):
        self.function(*self.args, **self.kwargs)

def adjustPwm(pwm, gain):
    adjustedPwm = 1500
    
    if pwm == 1500:
        return adjustedPwm
    
    if pwm > 1500:
        adjustedPwm = min(pwm, 1500 + int(400*gain/100))
    elif pwm < 1500:
        adjustedPwm = max(pwm, 1500 - int(400*gain/100))

    return adjustedPwm

def createPhotosphereFolder():
    videosPath = os.path.join(os.path.expanduser("~"), "Videos")
    baseFolderName = "photosphere"
    folderName = baseFolderName
    folderPath = os.path.join(videosPath, folderName)

    counter = 1
    while os.path.exists(folderPath):
        folderName = f"{baseFolderName}{counter}"
        folderPath = os.path.join(videosPath, folderName)
        counter += 1

    os.makedirs(folderPath)
    print(f"Folder created: {folderPath}")
    return folderPath
