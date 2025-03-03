import sys
from PyQt5.QtWidgets import QApplication
from VortexStation import VortexMainWindow

def main():
    app = QApplication(sys.argv)
    # Create and show the main window
    window = VortexMainWindow()
    window.show()
    
    # Execute the application
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()