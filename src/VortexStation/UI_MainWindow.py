# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt5.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTabWidget,
    QVBoxLayout, QWidget)
from VortexStation import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 845)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QFrame{\n"
"	background-color: #282A36;\n"
"}\n"
"\n"
"QLabel{\n"
"	\n"
"	color: rgb(248, 248, 242);\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 5px; \n"
"}\n"
"\n"
"QPushButton:hover { \n"
"	background-color: #FFB86C; /* Hover background color (darker green) */ 	\n"
"	border-color: #FFB86C; /* Hover border color */ \n"
"} \n"
"\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.headerFrame = QFrame(self.centralwidget)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setMinimumSize(QSize(0, 50))
        self.headerFrame.setMaximumSize(QSize(16777215, 50))
        self.headerFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.headerFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.headerFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.navigationButtonFrame = QFrame(self.headerFrame)
        self.navigationButtonFrame.setObjectName(u"navigationButtonFrame")
        self.navigationButtonFrame.setMinimumSize(QSize(100, 0))
        self.navigationButtonFrame.setMaximumSize(QSize(100, 16777215))
        self.navigationButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.navigationButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.navigationButtonFrame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.navigationButton = QPushButton(self.navigationButtonFrame)
        self.navigationButton.setObjectName(u"navigationButton")
        self.navigationButton.setMinimumSize(QSize(0, 50))
        self.navigationButton.setMaximumSize(QSize(16777215, 50))
        icon = QIcon()
        icon.addFile(u":/headerLeftButton/feather/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.navigationButton.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.navigationButton)


        self.horizontalLayout_3.addWidget(self.navigationButtonFrame)

        self.headerTitleFrame = QFrame(self.headerFrame)
        self.headerTitleFrame.setObjectName(u"headerTitleFrame")
        self.headerTitleFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.headerTitleFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.headerTitleFrame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.tittleLabel = QLabel(self.headerTitleFrame)
        self.tittleLabel.setObjectName(u"tittleLabel")
        font = QFont()
        font.setPointSize(32)
        font.setBold(True)
        self.tittleLabel.setFont(font)
        self.tittleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.tittleLabel)


        self.horizontalLayout_3.addWidget(self.headerTitleFrame)

        self.headerRightButtonsFrame = QFrame(self.headerFrame)
        self.headerRightButtonsFrame.setObjectName(u"headerRightButtonsFrame")
        self.headerRightButtonsFrame.setMinimumSize(QSize(150, 0))
        self.headerRightButtonsFrame.setMaximumSize(QSize(150, 16777215))
        self.headerRightButtonsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.headerRightButtonsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.headerRightButtonsFrame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.minimizeButton = QPushButton(self.headerRightButtonsFrame)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setMinimumSize(QSize(0, 50))
        self.minimizeButton.setMaximumSize(QSize(16777215, 50))
        icon1 = QIcon()
        icon1.addFile(u":/headerRightButtons/feather/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeButton.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.minimizeButton)

        self.maximizeButton = QPushButton(self.headerRightButtonsFrame)
        self.maximizeButton.setObjectName(u"maximizeButton")
        self.maximizeButton.setMinimumSize(QSize(0, 50))
        self.maximizeButton.setMaximumSize(QSize(16777215, 50))
        icon2 = QIcon()
        icon2.addFile(u":/headerRightButtons/feather/maximize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeButton.setIcon(icon2)

        self.horizontalLayout_4.addWidget(self.maximizeButton)

        self.exitButton = QPushButton(self.headerRightButtonsFrame)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setMinimumSize(QSize(0, 50))
        self.exitButton.setMaximumSize(QSize(16777215, 50))
        icon3 = QIcon()
        icon3.addFile(u":/headerRightButtons/feather/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exitButton.setIcon(icon3)

        self.horizontalLayout_4.addWidget(self.exitButton)


        self.horizontalLayout_3.addWidget(self.headerRightButtonsFrame)


        self.verticalLayout.addWidget(self.headerFrame)

        self.mainBodyFrame = QFrame(self.centralwidget)
        self.mainBodyFrame.setObjectName(u"mainBodyFrame")
        self.mainBodyFrame.setStyleSheet(u"QPushButton{ \n"
"	background-repeat: no-repeat;\n"
"	background-position: left center;\n"
"	padding-left:30px;\n"
"	padding-bottom: 10px; \n"
"	padding-top: 10px; \n"
"	color: #F8F8F2; \n"
"	font-size: 15px; \n"
"} ")
        self.mainBodyFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainBodyFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.mainBodyFrame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.mainBodyLeftButtonsFrame = QFrame(self.mainBodyFrame)
        self.mainBodyLeftButtonsFrame.setObjectName(u"mainBodyLeftButtonsFrame")
        self.mainBodyLeftButtonsFrame.setMinimumSize(QSize(100, 0))
        self.mainBodyLeftButtonsFrame.setMaximumSize(QSize(0, 16777215))
        self.mainBodyLeftButtonsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainBodyLeftButtonsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mainBodyLeftButtonsFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.homeButton = QPushButton(self.mainBodyLeftButtonsFrame)
        self.homeButton.setObjectName(u"homeButton")
        font1 = QFont()
        font1.setBold(True)
        self.homeButton.setFont(font1)
        self.homeButton.setStyleSheet(u"QPushButton{ \n"
"background-image: url(:/mainBodyLeftButtons/feather/home.svg); \n"
"}\n"
"\n"
"QPushButton{border-left: 3px solid #FFB86C;}\n"
"\n"
"")

        self.verticalLayout_2.addWidget(self.homeButton)

        self.cameraButton = QPushButton(self.mainBodyLeftButtonsFrame)
        self.cameraButton.setObjectName(u"cameraButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cameraButton.sizePolicy().hasHeightForWidth())
        self.cameraButton.setSizePolicy(sizePolicy)
        self.cameraButton.setMinimumSize(QSize(100, 0))
        self.cameraButton.setFont(font1)
        self.cameraButton.setStyleSheet(u"QPushButton{ \n"
"background-image: url(:/mainBodyLeftButtons/feather/camera.svg); \n"
"} ")

        self.verticalLayout_2.addWidget(self.cameraButton)

        self.floatButton = QPushButton(self.mainBodyLeftButtonsFrame)
        self.floatButton.setObjectName(u"floatButton")
        self.floatButton.setFont(font1)
        self.floatButton.setStyleSheet(u"QPushButton{ \n"
"background-image: url(:/mainBodyLeftButtons/feather/camera.svg); \n"
"} ")

        self.verticalLayout_2.addWidget(self.floatButton)

        self.verticalSpacer = QSpacerItem(20, 403, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.settingsButton = QPushButton(self.mainBodyLeftButtonsFrame)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setFont(font1)
        self.settingsButton.setStyleSheet(u"QPushButton{ \n"
"background-image: url(:/mainBodyLeftButtons/feather/settings.svg); \n"
"} ")

        self.verticalLayout_2.addWidget(self.settingsButton)


        self.horizontalLayout_7.addWidget(self.mainBodyLeftButtonsFrame)

        self.mainBodyStackedWidget = QStackedWidget(self.mainBodyFrame)
        self.mainBodyStackedWidget.setObjectName(u"mainBodyStackedWidget")
        self.mainBodyStackedWidget.setStyleSheet(u"")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.homePage.setStyleSheet(u"QScrollArea {\n"
"        border: 2px solid #5e5e5e;\n"
"        background-color: #f0f0f0;\n"
"    }")
        self.horizontalLayout_9 = QHBoxLayout(self.homePage)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.homePageFrame = QFrame(self.homePage)
        self.homePageFrame.setObjectName(u"homePageFrame")
        self.homePageFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.homePageFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.homePageFrame)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.homePageStackedWidgetFrame = QFrame(self.homePageFrame)
        self.homePageStackedWidgetFrame.setObjectName(u"homePageStackedWidgetFrame")
        self.homePageStackedWidgetFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}\n"
"")
        self.homePageStackedWidgetFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.homePageStackedWidgetFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.homePageStackedWidgetFrame)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.homePageStackedWidget = QStackedWidget(self.homePageStackedWidgetFrame)
        self.homePageStackedWidget.setObjectName(u"homePageStackedWidget")
        self.mainHomePage = QWidget()
        self.mainHomePage.setObjectName(u"mainHomePage")
        self.homePageStackedWidget.addWidget(self.mainHomePage)
        self.secondayHomePage = QWidget()
        self.secondayHomePage.setObjectName(u"secondayHomePage")
        self.homePageStackedWidget.addWidget(self.secondayHomePage)

        self.horizontalLayout_16.addWidget(self.homePageStackedWidget)


        self.horizontalLayout_12.addWidget(self.homePageStackedWidgetFrame)

        self.homePageIndicatorFrame = QFrame(self.homePageFrame)
        self.homePageIndicatorFrame.setObjectName(u"homePageIndicatorFrame")
        self.homePageIndicatorFrame.setMinimumSize(QSize(200, 0))
        self.homePageIndicatorFrame.setMaximumSize(QSize(200, 16777215))
        self.homePageIndicatorFrame.setStyleSheet(u"")
        self.homePageIndicatorFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.homePageIndicatorFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.homePageIndicatorFrame)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gaugeFrame = QFrame(self.homePageIndicatorFrame)
        self.gaugeFrame.setObjectName(u"gaugeFrame")
        self.gaugeFrame.setStyleSheet(u"")
        self.gaugeFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.gaugeFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.gaugeFrame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.fourThrustersFrame = QFrame(self.gaugeFrame)
        self.fourThrustersFrame.setObjectName(u"fourThrustersFrame")
        self.fourThrustersFrame.setMinimumSize(QSize(150, 150))
        self.fourThrustersFrame.setMaximumSize(QSize(150, 150))
        self.fourThrustersFrame.setStyleSheet(u"")
        self.fourThrustersFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.fourThrustersFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.fourThrustersGauge = QFrame(self.fourThrustersFrame)
        self.fourThrustersGauge.setObjectName(u"fourThrustersGauge")
        self.fourThrustersGauge.setGeometry(QRect(10, 10, 130, 130))
        self.fourThrustersGauge.setMinimumSize(QSize(130, 130))
        self.fourThrustersGauge.setMaximumSize(QSize(130, 130))
        self.fourThrustersGauge.setStyleSheet(u"QFrame{\n"
"	border-radius:65px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(68, 71, 90, 255), stop:0.750 rgba(255, 184, 108, 255));\n"
"}\n"
"")
        self.fourThrustersGauge.setFrameShape(QFrame.Shape.StyledPanel)
        self.fourThrustersGauge.setFrameShadow(QFrame.Shadow.Raised)
        self.circularBG = QFrame(self.fourThrustersFrame)
        self.circularBG.setObjectName(u"circularBG")
        self.circularBG.setGeometry(QRect(10, 10, 130, 130))
        self.circularBG.setMinimumSize(QSize(130, 130))
        self.circularBG.setMaximumSize(QSize(130, 130))
        self.circularBG.setStyleSheet(u"QFrame{\n"
"	border-radius:65px;\n"
"	background-color: rgba(77, 77, 127, 100);\n"
"}")
        self.circularBG.setFrameShape(QFrame.Shape.StyledPanel)
        self.circularBG.setFrameShadow(QFrame.Shadow.Raised)
        self.frame = QFrame(self.fourThrustersFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 20, 110, 110))
        self.frame.setStyleSheet(u"QFrame{\n"
"	border-radius:55px;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(27, 27, 55, 55))
        self.frame_2.setStyleSheet(u"border-radius:70px;\n"
"")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.fourThrustersLabel = QLabel(self.frame_2)
        self.fourThrustersLabel.setObjectName(u"fourThrustersLabel")
        self.fourThrustersLabel.setScaledContents(True)
        self.fourThrustersLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_13.addWidget(self.fourThrustersLabel, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.circularBG.raise_()
        self.fourThrustersGauge.raise_()
        self.frame.raise_()

        self.verticalLayout_8.addWidget(self.fourThrustersFrame, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.upDownThrustersFrame = QFrame(self.gaugeFrame)
        self.upDownThrustersFrame.setObjectName(u"upDownThrustersFrame")
        self.upDownThrustersFrame.setMinimumSize(QSize(150, 150))
        self.upDownThrustersFrame.setMaximumSize(QSize(150, 150))
        self.upDownThrustersFrame.setStyleSheet(u"")
        self.upDownThrustersFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.upDownThrustersFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.upDownThrustersGauge = QFrame(self.upDownThrustersFrame)
        self.upDownThrustersGauge.setObjectName(u"upDownThrustersGauge")
        self.upDownThrustersGauge.setGeometry(QRect(10, 10, 130, 130))
        self.upDownThrustersGauge.setMinimumSize(QSize(130, 130))
        self.upDownThrustersGauge.setMaximumSize(QSize(130, 130))
        self.upDownThrustersGauge.setStyleSheet(u"QFrame{\n"
"	border-radius:65px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(68, 71, 90, 255), stop:0.750 rgba(255, 184, 108, 255));\n"
"}\n"
"")
        self.upDownThrustersGauge.setFrameShape(QFrame.Shape.StyledPanel)
        self.upDownThrustersGauge.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_7 = QFrame(self.upDownThrustersFrame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(20, 20, 110, 110))
        self.frame_7.setStyleSheet(u"QFrame{\n"
"	border-radius:55px;\n"
"}")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(27, 27, 55, 55))
        self.frame_9.setStyleSheet(u"border-radius:70px;\n"
"")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.upDownThrustersLabel = QLabel(self.frame_9)
        self.upDownThrustersLabel.setObjectName(u"upDownThrustersLabel")
        self.upDownThrustersLabel.setScaledContents(True)
        self.upDownThrustersLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_17.addWidget(self.upDownThrustersLabel, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.circularBG_4 = QFrame(self.upDownThrustersFrame)
        self.circularBG_4.setObjectName(u"circularBG_4")
        self.circularBG_4.setGeometry(QRect(10, 10, 130, 130))
        self.circularBG_4.setMinimumSize(QSize(130, 130))
        self.circularBG_4.setMaximumSize(QSize(130, 130))
        self.circularBG_4.setStyleSheet(u"QFrame{\n"
"	border-radius:65px;\n"
"	background-color: rgba(77, 77, 127, 100);\n"
"}")
        self.circularBG_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.circularBG_4.setFrameShadow(QFrame.Shadow.Raised)
        self.circularBG_4.raise_()
        self.upDownThrustersGauge.raise_()
        self.frame_7.raise_()

        self.verticalLayout_8.addWidget(self.upDownThrustersFrame, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.servoFrame = QFrame(self.gaugeFrame)
        self.servoFrame.setObjectName(u"servoFrame")
        self.servoFrame.setMinimumSize(QSize(150, 150))
        self.servoFrame.setMaximumSize(QSize(150, 150))
        self.servoFrame.setStyleSheet(u"")
        self.servoFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.servoFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.servoGauge = QFrame(self.servoFrame)
        self.servoGauge.setObjectName(u"servoGauge")
        self.servoGauge.setGeometry(QRect(10, 10, 130, 130))
        self.servoGauge.setMinimumSize(QSize(130, 130))
        self.servoGauge.setMaximumSize(QSize(130, 130))
        self.servoGauge.setStyleSheet(u"QFrame{\n"
"	border-radius:65px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(68, 71, 90, 255), stop:0.750 rgba(255, 184, 108, 255));\n"
"}\n"
"")
        self.servoGauge.setFrameShape(QFrame.Shape.StyledPanel)
        self.servoGauge.setFrameShadow(QFrame.Shadow.Raised)
        self.circularBG_2 = QFrame(self.servoFrame)
        self.circularBG_2.setObjectName(u"circularBG_2")
        self.circularBG_2.setGeometry(QRect(10, 10, 130, 130))
        self.circularBG_2.setMinimumSize(QSize(130, 130))
        self.circularBG_2.setMaximumSize(QSize(130, 130))
        self.circularBG_2.setStyleSheet(u"QFrame{\n"
"	border-radius:65px;\n"
"	background-color: rgba(77, 77, 127, 100);\n"
"}")
        self.circularBG_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.circularBG_2.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_3 = QFrame(self.servoFrame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(20, 20, 110, 110))
        self.frame_3.setStyleSheet(u"QFrame{\n"
"	border-radius:55px;\n"
"}")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(27, 27, 55, 55))
        self.frame_4.setStyleSheet(u"border-radius:70px;\n"
"")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.servoLabel = QLabel(self.frame_4)
        self.servoLabel.setObjectName(u"servoLabel")
        self.servoLabel.setScaledContents(True)
        self.servoLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_34.addWidget(self.servoLabel, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.circularBG_2.raise_()
        self.servoGauge.raise_()
        self.frame_3.raise_()

        self.verticalLayout_8.addWidget(self.servoFrame, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_3.addWidget(self.gaugeFrame)

        self.indicatorsFrame = QFrame(self.homePageIndicatorFrame)
        self.indicatorsFrame.setObjectName(u"indicatorsFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.indicatorsFrame.sizePolicy().hasHeightForWidth())
        self.indicatorsFrame.setSizePolicy(sizePolicy1)
        self.indicatorsFrame.setStyleSheet(u"QFrame{\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"")
        self.indicatorsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.indicatorsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.indicatorsFrame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.ledFrame = QFrame(self.indicatorsFrame)
        self.ledFrame.setObjectName(u"ledFrame")
        self.ledFrame.setMaximumSize(QSize(16777215, 30))
        self.ledFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.ledFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.ledFrame)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.ledLabel = QLabel(self.ledFrame)
        self.ledLabel.setObjectName(u"ledLabel")
        self.ledLabel.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.ledLabel.setFont(font2)
        self.ledLabel.setStyleSheet(u"")
        self.ledLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_42.addWidget(self.ledLabel)


        self.verticalLayout_4.addWidget(self.ledFrame)

        self.rightGripperFrame = QFrame(self.indicatorsFrame)
        self.rightGripperFrame.setObjectName(u"rightGripperFrame")
        self.rightGripperFrame.setMaximumSize(QSize(16777215, 30))
        self.rightGripperFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.rightGripperFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.rightGripperFrame)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.gripperLabel = QLabel(self.rightGripperFrame)
        self.gripperLabel.setObjectName(u"gripperLabel")
        self.gripperLabel.setFont(font2)
        self.gripperLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_43.addWidget(self.gripperLabel)


        self.verticalLayout_4.addWidget(self.rightGripperFrame)

        self.leftGripperFrame = QFrame(self.indicatorsFrame)
        self.leftGripperFrame.setObjectName(u"leftGripperFrame")
        self.leftGripperFrame.setMaximumSize(QSize(16777215, 30))
        self.leftGripperFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.leftGripperFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.leftGripperFrame)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.leftGripperLabel = QLabel(self.leftGripperFrame)
        self.leftGripperLabel.setObjectName(u"leftGripperLabel")
        self.leftGripperLabel.setFont(font2)
        self.leftGripperLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_44.addWidget(self.leftGripperLabel)


        self.verticalLayout_4.addWidget(self.leftGripperFrame)

        self.fluidSuctionFrame = QFrame(self.indicatorsFrame)
        self.fluidSuctionFrame.setObjectName(u"fluidSuctionFrame")
        self.fluidSuctionFrame.setMaximumSize(QSize(16777215, 30))
        self.fluidSuctionFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.fluidSuctionFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.fluidSuctionFrame)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.fluidSuctionLabel = QLabel(self.fluidSuctionFrame)
        self.fluidSuctionLabel.setObjectName(u"fluidSuctionLabel")
        self.fluidSuctionLabel.setFont(font2)
        self.fluidSuctionLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_45.addWidget(self.fluidSuctionLabel)


        self.verticalLayout_4.addWidget(self.fluidSuctionFrame)

        self.floatingDebrisFrame = QFrame(self.indicatorsFrame)
        self.floatingDebrisFrame.setObjectName(u"floatingDebrisFrame")
        self.floatingDebrisFrame.setMaximumSize(QSize(16777215, 30))
        self.floatingDebrisFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.floatingDebrisFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.floatingDebrisFrame)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.floatingDebrisLabel = QLabel(self.floatingDebrisFrame)
        self.floatingDebrisLabel.setObjectName(u"floatingDebrisLabel")
        self.floatingDebrisLabel.setFont(font2)
        self.floatingDebrisLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_48.addWidget(self.floatingDebrisLabel)


        self.verticalLayout_4.addWidget(self.floatingDebrisFrame)

        self.altitudeHoldFrame = QFrame(self.indicatorsFrame)
        self.altitudeHoldFrame.setObjectName(u"altitudeHoldFrame")
        self.altitudeHoldFrame.setMaximumSize(QSize(16777215, 30))
        self.altitudeHoldFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.altitudeHoldFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.altitudeHoldFrame)
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.altitudeHoldLabel = QLabel(self.altitudeHoldFrame)
        self.altitudeHoldLabel.setObjectName(u"altitudeHoldLabel")
        self.altitudeHoldLabel.setFont(font2)
        self.altitudeHoldLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_49.addWidget(self.altitudeHoldLabel)


        self.verticalLayout_4.addWidget(self.altitudeHoldFrame)

        self.stabilizeFrame = QFrame(self.indicatorsFrame)
        self.stabilizeFrame.setObjectName(u"stabilizeFrame")
        self.stabilizeFrame.setMaximumSize(QSize(16777215, 30))
        self.stabilizeFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.stabilizeFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.stabilizeFrame)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.stabilizeFrameLabel = QLabel(self.stabilizeFrame)
        self.stabilizeFrameLabel.setObjectName(u"stabilizeFrameLabel")
        self.stabilizeFrameLabel.setFont(font2)
        self.stabilizeFrameLabel.setStyleSheet(u"")
        self.stabilizeFrameLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.stabilizeFrameLabel)


        self.verticalLayout_4.addWidget(self.stabilizeFrame)


        self.verticalLayout_3.addWidget(self.indicatorsFrame)

        self.sensorReadingFrame = QFrame(self.homePageIndicatorFrame)
        self.sensorReadingFrame.setObjectName(u"sensorReadingFrame")
        self.sensorReadingFrame.setMaximumSize(QSize(16777215, 16777215))
        self.sensorReadingFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.sensorReadingFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.sensorReadingFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.sensorReadingFrame)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gainFrame = QFrame(self.sensorReadingFrame)
        self.gainFrame.setObjectName(u"gainFrame")
        self.gainFrame.setMaximumSize(QSize(16777215, 30))
        self.gainFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #6272A4;\n"
"}")
        self.gainFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.gainFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.gainFrame)
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.gainLabel = QLabel(self.gainFrame)
        self.gainLabel.setObjectName(u"gainLabel")
        self.gainLabel.setFont(font2)
        self.gainLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_53.addWidget(self.gainLabel, 0, Qt.AlignmentFlag.AlignLeft)

        self.gainReadingLabel = QLabel(self.gainFrame)
        self.gainReadingLabel.setObjectName(u"gainReadingLabel")
        self.gainReadingLabel.setFont(font2)
        self.gainReadingLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_53.addWidget(self.gainReadingLabel, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_9.addWidget(self.gainFrame)

        self.phSensorFrame = QFrame(self.sensorReadingFrame)
        self.phSensorFrame.setObjectName(u"phSensorFrame")
        self.phSensorFrame.setMaximumSize(QSize(16777215, 30))
        self.phSensorFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #6272A4;\n"
"}")
        self.phSensorFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.phSensorFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.phSensorFrame)
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.phLael = QLabel(self.phSensorFrame)
        self.phLael.setObjectName(u"phLael")
        self.phLael.setFont(font2)
        self.phLael.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_50.addWidget(self.phLael, 0, Qt.AlignmentFlag.AlignLeft)

        self.phSensorReadingLabel = QLabel(self.phSensorFrame)
        self.phSensorReadingLabel.setObjectName(u"phSensorReadingLabel")
        self.phSensorReadingLabel.setFont(font2)
        self.phSensorReadingLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_50.addWidget(self.phSensorReadingLabel, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_9.addWidget(self.phSensorFrame)

        self.headingFrame = QFrame(self.sensorReadingFrame)
        self.headingFrame.setObjectName(u"headingFrame")
        self.headingFrame.setMaximumSize(QSize(16777215, 30))
        self.headingFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #6272A4;\n"
"}")
        self.headingFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.headingFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.headingFrame)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.headingLabel = QLabel(self.headingFrame)
        self.headingLabel.setObjectName(u"headingLabel")
        self.headingLabel.setFont(font2)
        self.headingLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_52.addWidget(self.headingLabel, 0, Qt.AlignmentFlag.AlignLeft)

        self.headingReadingLabel = QLabel(self.headingFrame)
        self.headingReadingLabel.setObjectName(u"headingReadingLabel")
        self.headingReadingLabel.setFont(font2)
        self.headingReadingLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_52.addWidget(self.headingReadingLabel, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_9.addWidget(self.headingFrame)

        self.depthFrame = QFrame(self.sensorReadingFrame)
        self.depthFrame.setObjectName(u"depthFrame")
        self.depthFrame.setMaximumSize(QSize(16777215, 30))
        self.depthFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #6272A4;\n"
"}")
        self.depthFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.depthFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.depthFrame)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.depthLabel = QLabel(self.depthFrame)
        self.depthLabel.setObjectName(u"depthLabel")
        self.depthLabel.setFont(font2)
        self.depthLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_51.addWidget(self.depthLabel, 0, Qt.AlignmentFlag.AlignLeft)

        self.depthReadingLabel = QLabel(self.depthFrame)
        self.depthReadingLabel.setObjectName(u"depthReadingLabel")
        self.depthReadingLabel.setFont(font2)
        self.depthReadingLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_51.addWidget(self.depthReadingLabel, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_9.addWidget(self.depthFrame)


        self.verticalLayout_3.addWidget(self.sensorReadingFrame, 0, Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout_12.addWidget(self.homePageIndicatorFrame)


        self.horizontalLayout_9.addWidget(self.homePageFrame)

        self.mainBodyStackedWidget.addWidget(self.homePage)
        self.floatPage = QWidget()
        self.floatPage.setObjectName(u"floatPage")
        self.floatPage.setStyleSheet(u"\n"
"  QTabBar::tab {\n"
"        background: transparent;   /* Default tab color */\n"
"        color: black;\n"
"    }\n"
"    QTabBar::tab:selected {\n"
"        background: darkgray;    /* Selected tab color */\n"
"        color: white;\n"
"    }\n"
"    QTabBar::tab:hover {\n"
"        background: gray;        /* Hover effect */\n"
"    }")
        self.verticalLayout_11 = QVBoxLayout(self.floatPage)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.profileTabs = QTabWidget(self.floatPage)
        self.profileTabs.setObjectName(u"profileTabs")
        self.profileTabs.setStyleSheet(u"\n"
"  QTabBar::tab {\n"
"        background: transparent;   /* Default tab color */\n"
"        color: black;\n"
"    }\n"
"    QTabBar::tab:selected {\n"
"        background: darkgray;    /* Selected tab color */\n"
"        color: white;\n"
"    }\n"
"    QTabBar::tab:hover {\n"
"        background: gray;        /* Hover effect */\n"
"    }")
        self.profile1 = QWidget()
        self.profile1.setObjectName(u"profile1")
        self.verticalLayout_37 = QVBoxLayout(self.profile1)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.floatTitle1 = QFrame(self.profile1)
        self.floatTitle1.setObjectName(u"floatTitle1")
        self.floatTitle1.setMinimumSize(QSize(0, 60))
        self.floatTitle1.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}\n"
"")
        self.floatTitle1.setFrameShape(QFrame.Shape.NoFrame)
        self.floatTitle1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.floatTitle1)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.floatLabel1 = QLabel(self.floatTitle1)
        self.floatLabel1.setObjectName(u"floatLabel1")
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        self.floatLabel1.setFont(font3)
        self.floatLabel1.setStyleSheet(u"")
        self.floatLabel1.setFrameShape(QFrame.Shape.NoFrame)
        self.floatLabel1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_31.addWidget(self.floatLabel1)


        self.verticalLayout_37.addWidget(self.floatTitle1)

        self.graphFrame1 = QFrame(self.profile1)
        self.graphFrame1.setObjectName(u"graphFrame1")
        self.graphFrame1.setMinimumSize(QSize(500, 650))
        self.graphFrame1.setFrameShape(QFrame.Shape.NoFrame)
        self.graphFrame1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_129 = QHBoxLayout(self.graphFrame1)
        self.horizontalLayout_129.setSpacing(0)
        self.horizontalLayout_129.setObjectName(u"horizontalLayout_129")
        self.horizontalLayout_129.setContentsMargins(0, 0, 0, 0)
        self.graphDisplay1 = QLabel(self.graphFrame1)
        self.graphDisplay1.setObjectName(u"graphDisplay1")
        self.graphDisplay1.setFrameShape(QFrame.Shape.NoFrame)
        self.graphDisplay1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_129.addWidget(self.graphDisplay1)


        self.verticalLayout_37.addWidget(self.graphFrame1)

        self.signalFrameText1 = QFrame(self.profile1)
        self.signalFrameText1.setObjectName(u"signalFrameText1")
        self.signalFrameText1.setMinimumSize(QSize(0, 50))
        self.signalFrameText1.setFrameShape(QFrame.Shape.NoFrame)
        self.signalFrameText1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.signalFrameText1)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.signalLabel1 = QLabel(self.signalFrameText1)
        self.signalLabel1.setObjectName(u"signalLabel1")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setItalic(True)
        self.signalLabel1.setFont(font4)
        self.signalLabel1.setStyleSheet(u"color: red")
        self.signalLabel1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_32.addWidget(self.signalLabel1)


        self.verticalLayout_37.addWidget(self.signalFrameText1)

        self.floatButtonsFrame1 = QFrame(self.profile1)
        self.floatButtonsFrame1.setObjectName(u"floatButtonsFrame1")
        self.floatButtonsFrame1.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}\n"
"")
        self.floatButtonsFrame1.setFrameShape(QFrame.Shape.NoFrame)
        self.floatButtonsFrame1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_130 = QHBoxLayout(self.floatButtonsFrame1)
        self.horizontalLayout_130.setSpacing(5)
        self.horizontalLayout_130.setObjectName(u"horizontalLayout_130")
        self.horizontalLayout_130.setContentsMargins(0, 0, 0, 0)
        self.startReadingFrame1 = QFrame(self.floatButtonsFrame1)
        self.startReadingFrame1.setObjectName(u"startReadingFrame1")
        self.startReadingFrame1.setFrameShape(QFrame.Shape.NoFrame)
        self.startReadingFrame1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_131 = QHBoxLayout(self.startReadingFrame1)
        self.horizontalLayout_131.setSpacing(0)
        self.horizontalLayout_131.setObjectName(u"horizontalLayout_131")
        self.horizontalLayout_131.setContentsMargins(0, 0, 0, 0)
        self.startReading1 = QPushButton(self.startReadingFrame1)
        self.startReading1.setObjectName(u"startReading1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.startReading1.sizePolicy().hasHeightForWidth())
        self.startReading1.setSizePolicy(sizePolicy2)

        self.horizontalLayout_131.addWidget(self.startReading1)


        self.horizontalLayout_130.addWidget(self.startReadingFrame1)

        self.stopReadingFrame1 = QFrame(self.floatButtonsFrame1)
        self.stopReadingFrame1.setObjectName(u"stopReadingFrame1")
        self.stopReadingFrame1.setFrameShape(QFrame.Shape.NoFrame)
        self.stopReadingFrame1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_132 = QHBoxLayout(self.stopReadingFrame1)
        self.horizontalLayout_132.setSpacing(0)
        self.horizontalLayout_132.setObjectName(u"horizontalLayout_132")
        self.horizontalLayout_132.setContentsMargins(0, 0, 0, 0)
        self.stopReading1 = QPushButton(self.stopReadingFrame1)
        self.stopReading1.setObjectName(u"stopReading1")
        sizePolicy2.setHeightForWidth(self.stopReading1.sizePolicy().hasHeightForWidth())
        self.stopReading1.setSizePolicy(sizePolicy2)

        self.horizontalLayout_132.addWidget(self.stopReading1)


        self.horizontalLayout_130.addWidget(self.stopReadingFrame1)


        self.verticalLayout_37.addWidget(self.floatButtonsFrame1)

        self.profileTabs.addTab(self.profile1, "")
        self.profile2 = QWidget()
        self.profile2.setObjectName(u"profile2")
        self.verticalLayout_38 = QVBoxLayout(self.profile2)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.floatTitle2 = QFrame(self.profile2)
        self.floatTitle2.setObjectName(u"floatTitle2")
        self.floatTitle2.setMinimumSize(QSize(0, 60))
        self.floatTitle2.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}\n"
"")
        self.floatTitle2.setFrameShape(QFrame.Shape.NoFrame)
        self.floatTitle2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.floatTitle2)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.floatLabel2 = QLabel(self.floatTitle2)
        self.floatLabel2.setObjectName(u"floatLabel2")
        self.floatLabel2.setFont(font3)
        self.floatLabel2.setStyleSheet(u"")
        self.floatLabel2.setFrameShape(QFrame.Shape.NoFrame)
        self.floatLabel2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_35.addWidget(self.floatLabel2)


        self.verticalLayout_38.addWidget(self.floatTitle2)

        self.graphFrame2 = QFrame(self.profile2)
        self.graphFrame2.setObjectName(u"graphFrame2")
        self.graphFrame2.setMinimumSize(QSize(500, 650))
        self.graphFrame2.setFrameShape(QFrame.Shape.NoFrame)
        self.graphFrame2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_140 = QHBoxLayout(self.graphFrame2)
        self.horizontalLayout_140.setSpacing(0)
        self.horizontalLayout_140.setObjectName(u"horizontalLayout_140")
        self.horizontalLayout_140.setContentsMargins(0, 0, 0, 0)
        self.graphDisplay2 = QLabel(self.graphFrame2)
        self.graphDisplay2.setObjectName(u"graphDisplay2")
        self.graphDisplay2.setFrameShape(QFrame.Shape.NoFrame)
        self.graphDisplay2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_140.addWidget(self.graphDisplay2)


        self.verticalLayout_38.addWidget(self.graphFrame2)

        self.signalFrameText2 = QFrame(self.profile2)
        self.signalFrameText2.setObjectName(u"signalFrameText2")
        self.signalFrameText2.setMinimumSize(QSize(0, 50))
        self.signalFrameText2.setFrameShape(QFrame.Shape.NoFrame)
        self.signalFrameText2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.signalFrameText2)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.signalLabel2 = QLabel(self.signalFrameText2)
        self.signalLabel2.setObjectName(u"signalLabel2")
        self.signalLabel2.setFont(font4)
        self.signalLabel2.setStyleSheet(u"color: red")
        self.signalLabel2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_36.addWidget(self.signalLabel2)


        self.verticalLayout_38.addWidget(self.signalFrameText2)

        self.floatButtonsFrame2 = QFrame(self.profile2)
        self.floatButtonsFrame2.setObjectName(u"floatButtonsFrame2")
        self.floatButtonsFrame2.setMinimumSize(QSize(0, 65))
        self.floatButtonsFrame2.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}\n"
"")
        self.floatButtonsFrame2.setFrameShape(QFrame.Shape.NoFrame)
        self.floatButtonsFrame2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_137 = QHBoxLayout(self.floatButtonsFrame2)
        self.horizontalLayout_137.setSpacing(5)
        self.horizontalLayout_137.setObjectName(u"horizontalLayout_137")
        self.horizontalLayout_137.setContentsMargins(0, 0, 0, 0)
        self.startReadingFrame2 = QFrame(self.floatButtonsFrame2)
        self.startReadingFrame2.setObjectName(u"startReadingFrame2")
        self.startReadingFrame2.setFrameShape(QFrame.Shape.NoFrame)
        self.startReadingFrame2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_138 = QHBoxLayout(self.startReadingFrame2)
        self.horizontalLayout_138.setSpacing(0)
        self.horizontalLayout_138.setObjectName(u"horizontalLayout_138")
        self.horizontalLayout_138.setContentsMargins(0, 0, 0, 0)
        self.startReading2 = QPushButton(self.startReadingFrame2)
        self.startReading2.setObjectName(u"startReading2")
        sizePolicy2.setHeightForWidth(self.startReading2.sizePolicy().hasHeightForWidth())
        self.startReading2.setSizePolicy(sizePolicy2)

        self.horizontalLayout_138.addWidget(self.startReading2)


        self.horizontalLayout_137.addWidget(self.startReadingFrame2)

        self.stopReadingFrame2 = QFrame(self.floatButtonsFrame2)
        self.stopReadingFrame2.setObjectName(u"stopReadingFrame2")
        self.stopReadingFrame2.setFrameShape(QFrame.Shape.NoFrame)
        self.stopReadingFrame2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_139 = QHBoxLayout(self.stopReadingFrame2)
        self.horizontalLayout_139.setSpacing(0)
        self.horizontalLayout_139.setObjectName(u"horizontalLayout_139")
        self.horizontalLayout_139.setContentsMargins(0, 0, 0, 0)
        self.stopReading2 = QPushButton(self.stopReadingFrame2)
        self.stopReading2.setObjectName(u"stopReading2")
        sizePolicy2.setHeightForWidth(self.stopReading2.sizePolicy().hasHeightForWidth())
        self.stopReading2.setSizePolicy(sizePolicy2)

        self.horizontalLayout_139.addWidget(self.stopReading2)


        self.horizontalLayout_137.addWidget(self.stopReadingFrame2)


        self.verticalLayout_38.addWidget(self.floatButtonsFrame2)

        self.profileTabs.addTab(self.profile2, "")

        self.verticalLayout_11.addWidget(self.profileTabs)

        self.mainBodyStackedWidget.addWidget(self.floatPage)
        self.cameraPage = QWidget()
        self.cameraPage.setObjectName(u"cameraPage")
        self.cameraPage.setStyleSheet(u"")
        self.horizontalLayout_11 = QHBoxLayout(self.cameraPage)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.cameraPageFrame = QFrame(self.cameraPage)
        self.cameraPageFrame.setObjectName(u"cameraPageFrame")
        self.cameraPageFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.cameraPageFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_11.addWidget(self.cameraPageFrame)

        self.mainBodyStackedWidget.addWidget(self.cameraPage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.horizontalLayout_8 = QHBoxLayout(self.settingsPage)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.settingsPageFrame = QFrame(self.settingsPage)
        self.settingsPageFrame.setObjectName(u"settingsPageFrame")
        self.settingsPageFrame.setStyleSheet(u"")
        self.settingsPageFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.settingsPageFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.settingsPageFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.settingsPageControllerSettingsFrame = QFrame(self.settingsPageFrame)
        self.settingsPageControllerSettingsFrame.setObjectName(u"settingsPageControllerSettingsFrame")
        self.settingsPageControllerSettingsFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}\n"
"")
        self.settingsPageControllerSettingsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.settingsPageControllerSettingsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.settingsPageControllerSettingsFrame)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.controllerSettingsButton = QPushButton(self.settingsPageControllerSettingsFrame)
        self.controllerSettingsButton.setObjectName(u"controllerSettingsButton")
        sizePolicy2.setHeightForWidth(self.controllerSettingsButton.sizePolicy().hasHeightForWidth())
        self.controllerSettingsButton.setSizePolicy(sizePolicy2)
        self.controllerSettingsButton.setStyleSheet(u"QPushButton{\n"
"	image: url(:/controllerImage/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Control Screen/Solid/Control Solid Inv 4k.png);\n"
"}\n"
"")

        self.horizontalLayout_19.addWidget(self.controllerSettingsButton)


        self.verticalLayout_5.addWidget(self.settingsPageControllerSettingsFrame)

        self.settingsPageGeneralSettingsFrame = QFrame(self.settingsPageFrame)
        self.settingsPageGeneralSettingsFrame.setObjectName(u"settingsPageGeneralSettingsFrame")
        self.settingsPageGeneralSettingsFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}\n"
"")
        self.settingsPageGeneralSettingsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.settingsPageGeneralSettingsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.settingsPageGeneralSettingsFrame)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.generalSettingsButton = QPushButton(self.settingsPageGeneralSettingsFrame)
        self.generalSettingsButton.setObjectName(u"generalSettingsButton")
        sizePolicy2.setHeightForWidth(self.generalSettingsButton.sizePolicy().hasHeightForWidth())
        self.generalSettingsButton.setSizePolicy(sizePolicy2)

        self.horizontalLayout_18.addWidget(self.generalSettingsButton)


        self.verticalLayout_5.addWidget(self.settingsPageGeneralSettingsFrame)


        self.horizontalLayout_8.addWidget(self.settingsPageFrame)

        self.mainBodyStackedWidget.addWidget(self.settingsPage)
        self.controllerSettingsPage = QWidget()
        self.controllerSettingsPage.setObjectName(u"controllerSettingsPage")
        self.controllerSettingsPage.setStyleSheet(u"")
        self.horizontalLayout_10 = QHBoxLayout(self.controllerSettingsPage)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.controllerSettingsPageFrame = QFrame(self.controllerSettingsPage)
        self.controllerSettingsPageFrame.setObjectName(u"controllerSettingsPageFrame")
        self.controllerSettingsPageFrame.setStyleSheet(u"")
        self.controllerSettingsPageFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.controllerSettingsPageFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.controllerSettingsPageFrame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.controllerSettingsSolidButtonsFrame = QFrame(self.controllerSettingsPageFrame)
        self.controllerSettingsSolidButtonsFrame.setObjectName(u"controllerSettingsSolidButtonsFrame")
        self.controllerSettingsSolidButtonsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.controllerSettingsSolidButtonsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.controllerSettingsSolidButtonsFrame)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.controllerSettingsSolidButtonsFrame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea {\n"
"    border: 1px solid #282A36;\n"
"}\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 678, 2660))
        self.horizontalLayout_20 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.controllerSettingsSolidButtonsFrameInScrollArea = QFrame(self.scrollAreaWidgetContents)
        self.controllerSettingsSolidButtonsFrameInScrollArea.setObjectName(u"controllerSettingsSolidButtonsFrameInScrollArea")
        self.controllerSettingsSolidButtonsFrameInScrollArea.setStyleSheet(u"QComboBox {\n"
"    background-color: #f0f0f0;\n"
"    border-radius: 5px;\n"
"    color: #2c3e50; /* Text color */\n"
"    font-size: 25px; /* Font size */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #44475A; \n"
"    selection-background-color: #44475A;; /* Background color of selected item */\n"
"}\n"
"\n"
"\n"
"")
        self.controllerSettingsSolidButtonsFrameInScrollArea.setFrameShape(QFrame.Shape.StyledPanel)
        self.controllerSettingsSolidButtonsFrameInScrollArea.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.controllerSettingsSolidButtonsFrameInScrollArea)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.AButtonFrame = QFrame(self.controllerSettingsSolidButtonsFrameInScrollArea)
        self.AButtonFrame.setObjectName(u"AButtonFrame")
        self.AButtonFrame.setMaximumSize(QSize(16777215, 125))
        self.AButtonFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.AButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.AButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.AButtonFrame)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.AButtonLabel = QLabel(self.AButtonFrame)
        self.AButtonLabel.setObjectName(u"AButtonLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.AButtonLabel.sizePolicy().hasHeightForWidth())
        self.AButtonLabel.setSizePolicy(sizePolicy3)
        self.AButtonLabel.setMaximumSize(QSize(100, 100))
        self.AButtonLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/A.svg"))
        self.AButtonLabel.setScaledContents(True)

        self.horizontalLayout_46.addWidget(self.AButtonLabel)

        self.AButtonComboBox = QComboBox(self.AButtonFrame)
        self.AButtonComboBox.addItem("")
        self.AButtonComboBox.addItem("")
        self.AButtonComboBox.addItem("")
        self.AButtonComboBox.addItem("")
        self.AButtonComboBox.addItem("")
        self.AButtonComboBox.addItem("")
        self.AButtonComboBox.addItem("")
        self.AButtonComboBox.addItem("")
        self.AButtonComboBox.addItem("")
        self.AButtonComboBox.addItem("")
        self.AButtonComboBox.setObjectName(u"AButtonComboBox")
        self.AButtonComboBox.setMaximumSize(QSize(16777215, 50))
        self.AButtonComboBox.setEditable(False)

        self.horizontalLayout_46.addWidget(self.AButtonComboBox)


        self.verticalLayout_7.addWidget(self.AButtonFrame)

        self.BButtonFrame = QFrame(self.controllerSettingsSolidButtonsFrameInScrollArea)
        self.BButtonFrame.setObjectName(u"BButtonFrame")
        self.BButtonFrame.setMaximumSize(QSize(16777215, 125))
        self.BButtonFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.BButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.BButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.BButtonFrame)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.BButtonLabel = QLabel(self.BButtonFrame)
        self.BButtonLabel.setObjectName(u"BButtonLabel")
        sizePolicy3.setHeightForWidth(self.BButtonLabel.sizePolicy().hasHeightForWidth())
        self.BButtonLabel.setSizePolicy(sizePolicy3)
        self.BButtonLabel.setMaximumSize(QSize(100, 100))
        self.BButtonLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/B.svg"))
        self.BButtonLabel.setScaledContents(True)

        self.horizontalLayout_22.addWidget(self.BButtonLabel)

        self.BButtonComboBox = QComboBox(self.BButtonFrame)
        self.BButtonComboBox.addItem("")
        self.BButtonComboBox.addItem("")
        self.BButtonComboBox.addItem("")
        self.BButtonComboBox.addItem("")
        self.BButtonComboBox.addItem("")
        self.BButtonComboBox.addItem("")
        self.BButtonComboBox.addItem("")
        self.BButtonComboBox.addItem("")
        self.BButtonComboBox.addItem("")
        self.BButtonComboBox.addItem("")
        self.BButtonComboBox.setObjectName(u"BButtonComboBox")
        self.BButtonComboBox.setMaximumSize(QSize(16777215, 50))
        self.BButtonComboBox.setEditable(False)

        self.horizontalLayout_22.addWidget(self.BButtonComboBox)


        self.verticalLayout_7.addWidget(self.BButtonFrame)

        self.YButtonFrame = QFrame(self.controllerSettingsSolidButtonsFrameInScrollArea)
        self.YButtonFrame.setObjectName(u"YButtonFrame")
        self.YButtonFrame.setMaximumSize(QSize(16777215, 125))
        self.YButtonFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.YButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.YButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.YButtonFrame)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.YButtonLabel = QLabel(self.YButtonFrame)
        self.YButtonLabel.setObjectName(u"YButtonLabel")
        sizePolicy3.setHeightForWidth(self.YButtonLabel.sizePolicy().hasHeightForWidth())
        self.YButtonLabel.setSizePolicy(sizePolicy3)
        self.YButtonLabel.setMaximumSize(QSize(100, 100))
        self.YButtonLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/Y.svg"))
        self.YButtonLabel.setScaledContents(True)

        self.horizontalLayout_41.addWidget(self.YButtonLabel)

        self.YButtonComboBox = QComboBox(self.YButtonFrame)
        self.YButtonComboBox.addItem("")
        self.YButtonComboBox.addItem("")
        self.YButtonComboBox.addItem("")
        self.YButtonComboBox.addItem("")
        self.YButtonComboBox.addItem("")
        self.YButtonComboBox.addItem("")
        self.YButtonComboBox.addItem("")
        self.YButtonComboBox.addItem("")
        self.YButtonComboBox.addItem("")
        self.YButtonComboBox.addItem("")
        self.YButtonComboBox.setObjectName(u"YButtonComboBox")
        self.YButtonComboBox.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_41.addWidget(self.YButtonComboBox)


        self.verticalLayout_7.addWidget(self.YButtonFrame)

        self.XButtonFrame = QFrame(self.controllerSettingsSolidButtonsFrameInScrollArea)
        self.XButtonFrame.setObjectName(u"XButtonFrame")
        self.XButtonFrame.setMaximumSize(QSize(16777215, 125))
        self.XButtonFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.XButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.XButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.XButtonFrame)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.XButtonLabel = QLabel(self.XButtonFrame)
        self.XButtonLabel.setObjectName(u"XButtonLabel")
        sizePolicy3.setHeightForWidth(self.XButtonLabel.sizePolicy().hasHeightForWidth())
        self.XButtonLabel.setSizePolicy(sizePolicy3)
        self.XButtonLabel.setMaximumSize(QSize(100, 100))
        self.XButtonLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/X.svg"))
        self.XButtonLabel.setScaledContents(True)

        self.horizontalLayout_31.addWidget(self.XButtonLabel)

        self.XButtonComboBox = QComboBox(self.XButtonFrame)
        self.XButtonComboBox.addItem("")
        self.XButtonComboBox.addItem("")
        self.XButtonComboBox.addItem("")
        self.XButtonComboBox.addItem("")
        self.XButtonComboBox.addItem("")
        self.XButtonComboBox.addItem("")
        self.XButtonComboBox.addItem("")
        self.XButtonComboBox.addItem("")
        self.XButtonComboBox.addItem("")
        self.XButtonComboBox.addItem("")
        self.XButtonComboBox.setObjectName(u"XButtonComboBox")
        self.XButtonComboBox.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_31.addWidget(self.XButtonComboBox)


        self.verticalLayout_7.addWidget(self.XButtonFrame)

        self.LBButtonFrame = QFrame(self.controllerSettingsSolidButtonsFrameInScrollArea)
        self.LBButtonFrame.setObjectName(u"LBButtonFrame")
        self.LBButtonFrame.setMaximumSize(QSize(16777215, 125))
        self.LBButtonFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.LBButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.LBButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.LBButtonFrame)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.LBButtonLabel = QLabel(self.LBButtonFrame)
        self.LBButtonLabel.setObjectName(u"LBButtonLabel")
        sizePolicy3.setHeightForWidth(self.LBButtonLabel.sizePolicy().hasHeightForWidth())
        self.LBButtonLabel.setSizePolicy(sizePolicy3)
        self.LBButtonLabel.setMaximumSize(QSize(100, 100))
        self.LBButtonLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/Left Bumper.svg"))
        self.LBButtonLabel.setScaledContents(True)

        self.horizontalLayout_23.addWidget(self.LBButtonLabel)

        self.LBButtonComboBox = QComboBox(self.LBButtonFrame)
        self.LBButtonComboBox.addItem("")
        self.LBButtonComboBox.addItem("")
        self.LBButtonComboBox.addItem("")
        self.LBButtonComboBox.addItem("")
        self.LBButtonComboBox.addItem("")
        self.LBButtonComboBox.addItem("")
        self.LBButtonComboBox.addItem("")
        self.LBButtonComboBox.addItem("")
        self.LBButtonComboBox.addItem("")
        self.LBButtonComboBox.addItem("")
        self.LBButtonComboBox.setObjectName(u"LBButtonComboBox")
        self.LBButtonComboBox.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_23.addWidget(self.LBButtonComboBox)


        self.verticalLayout_7.addWidget(self.LBButtonFrame)

        self.RBButtonFrame = QFrame(self.controllerSettingsSolidButtonsFrameInScrollArea)
        self.RBButtonFrame.setObjectName(u"RBButtonFrame")
        self.RBButtonFrame.setMaximumSize(QSize(16777215, 125))
        self.RBButtonFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.RBButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.RBButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.RBButtonFrame)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.RBButtonLabel = QLabel(self.RBButtonFrame)
        self.RBButtonLabel.setObjectName(u"RBButtonLabel")
        sizePolicy3.setHeightForWidth(self.RBButtonLabel.sizePolicy().hasHeightForWidth())
        self.RBButtonLabel.setSizePolicy(sizePolicy3)
        self.RBButtonLabel.setMaximumSize(QSize(100, 100))
        self.RBButtonLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/Right Bumper.svg"))
        self.RBButtonLabel.setScaledContents(True)

        self.horizontalLayout_38.addWidget(self.RBButtonLabel)

        self.RBButtonComboBox = QComboBox(self.RBButtonFrame)
        self.RBButtonComboBox.addItem("")
        self.RBButtonComboBox.addItem("")
        self.RBButtonComboBox.addItem("")
        self.RBButtonComboBox.addItem("")
        self.RBButtonComboBox.addItem("")
        self.RBButtonComboBox.addItem("")
        self.RBButtonComboBox.addItem("")
        self.RBButtonComboBox.addItem("")
        self.RBButtonComboBox.addItem("")
        self.RBButtonComboBox.addItem("")
        self.RBButtonComboBox.setObjectName(u"RBButtonComboBox")
        self.RBButtonComboBox.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_38.addWidget(self.RBButtonComboBox)


        self.verticalLayout_7.addWidget(self.RBButtonFrame)

        self.STARTButtonFrame = QFrame(self.controllerSettingsSolidButtonsFrameInScrollArea)
        self.STARTButtonFrame.setObjectName(u"STARTButtonFrame")
        self.STARTButtonFrame.setMaximumSize(QSize(16777215, 125))
        self.STARTButtonFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.STARTButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.STARTButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.STARTButtonFrame)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.STARTButtonLabel = QLabel(self.STARTButtonFrame)
        self.STARTButtonLabel.setObjectName(u"STARTButtonLabel")
        sizePolicy3.setHeightForWidth(self.STARTButtonLabel.sizePolicy().hasHeightForWidth())
        self.STARTButtonLabel.setSizePolicy(sizePolicy3)
        self.STARTButtonLabel.setMaximumSize(QSize(100, 100))
        self.STARTButtonLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/Menu.svg"))
        self.STARTButtonLabel.setScaledContents(True)

        self.horizontalLayout_28.addWidget(self.STARTButtonLabel)

        self.STARTButtonComboBox = QComboBox(self.STARTButtonFrame)
        self.STARTButtonComboBox.addItem("")
        self.STARTButtonComboBox.addItem("")
        self.STARTButtonComboBox.addItem("")
        self.STARTButtonComboBox.addItem("")
        self.STARTButtonComboBox.addItem("")
        self.STARTButtonComboBox.addItem("")
        self.STARTButtonComboBox.addItem("")
        self.STARTButtonComboBox.addItem("")
        self.STARTButtonComboBox.addItem("")
        self.STARTButtonComboBox.addItem("")
        self.STARTButtonComboBox.setObjectName(u"STARTButtonComboBox")
        self.STARTButtonComboBox.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_28.addWidget(self.STARTButtonComboBox)


        self.verticalLayout_7.addWidget(self.STARTButtonFrame)

        self.BACKButtonFrame = QFrame(self.controllerSettingsSolidButtonsFrameInScrollArea)
        self.BACKButtonFrame.setObjectName(u"BACKButtonFrame")
        self.BACKButtonFrame.setMaximumSize(QSize(16777215, 125))
        self.BACKButtonFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.BACKButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.BACKButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.BACKButtonFrame)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.BACKButtonLabel = QLabel(self.BACKButtonFrame)
        self.BACKButtonLabel.setObjectName(u"BACKButtonLabel")
        sizePolicy3.setHeightForWidth(self.BACKButtonLabel.sizePolicy().hasHeightForWidth())
        self.BACKButtonLabel.setSizePolicy(sizePolicy3)
        self.BACKButtonLabel.setMaximumSize(QSize(100, 100))
        self.BACKButtonLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/View.svg"))
        self.BACKButtonLabel.setScaledContents(True)

        self.horizontalLayout_24.addWidget(self.BACKButtonLabel)

        self.BACKButtonComboBox = QComboBox(self.BACKButtonFrame)
        self.BACKButtonComboBox.addItem("")
        self.BACKButtonComboBox.addItem("")
        self.BACKButtonComboBox.addItem("")
        self.BACKButtonComboBox.addItem("")
        self.BACKButtonComboBox.addItem("")
        self.BACKButtonComboBox.addItem("")
        self.BACKButtonComboBox.addItem("")
        self.BACKButtonComboBox.addItem("")
        self.BACKButtonComboBox.addItem("")
        self.BACKButtonComboBox.addItem("")
        self.BACKButtonComboBox.setObjectName(u"BACKButtonComboBox")
        self.BACKButtonComboBox.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_24.addWidget(self.BACKButtonComboBox)


        self.verticalLayout_7.addWidget(self.BACKButtonFrame)

        self.RIGHTPADButtonFrame = QFrame(self.controllerSettingsSolidButtonsFrameInScrollArea)
        self.RIGHTPADButtonFrame.setObjectName(u"RIGHTPADButtonFrame")
        self.RIGHTPADButtonFrame.setMaximumSize(QSize(16777215, 125))
        self.RIGHTPADButtonFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.RIGHTPADButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.RIGHTPADButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.RIGHTPADButtonFrame)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.RIGHTPADButtonLabel = QLabel(self.RIGHTPADButtonFrame)
        self.RIGHTPADButtonLabel.setObjectName(u"RIGHTPADButtonLabel")
        sizePolicy3.setHeightForWidth(self.RIGHTPADButtonLabel.sizePolicy().hasHeightForWidth())
        self.RIGHTPADButtonLabel.setSizePolicy(sizePolicy3)
        self.RIGHTPADButtonLabel.setMaximumSize(QSize(100, 100))
        self.RIGHTPADButtonLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.RIGHTPADButtonLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/Right Stick Click.svg"))
        self.RIGHTPADButtonLabel.setScaledContents(True)

        self.horizontalLayout_37.addWidget(self.RIGHTPADButtonLabel)

        self.RIGHTPADButtonComboBox = QComboBox(self.RIGHTPADButtonFrame)
        self.RIGHTPADButtonComboBox.addItem("")
        self.RIGHTPADButtonComboBox.addItem("")
        self.RIGHTPADButtonComboBox.addItem("")
        self.RIGHTPADButtonComboBox.addItem("")
        self.RIGHTPADButtonComboBox.addItem("")
        self.RIGHTPADButtonComboBox.addItem("")
        self.RIGHTPADButtonComboBox.addItem("")
        self.RIGHTPADButtonComboBox.addItem("")
        self.RIGHTPADButtonComboBox.addItem("")
        self.RIGHTPADButtonComboBox.addItem("")
        self.RIGHTPADButtonComboBox.setObjectName(u"RIGHTPADButtonComboBox")
        self.RIGHTPADButtonComboBox.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_37.addWidget(self.RIGHTPADButtonComboBox)


        self.verticalLayout_7.addWidget(self.RIGHTPADButtonFrame)

        self.LEFTPADButtonFrame = QFrame(self.controllerSettingsSolidButtonsFrameInScrollArea)
        self.LEFTPADButtonFrame.setObjectName(u"LEFTPADButtonFrame")
        self.LEFTPADButtonFrame.setMaximumSize(QSize(16777215, 125))
        self.LEFTPADButtonFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.LEFTPADButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.LEFTPADButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.LEFTPADButtonFrame)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.LEFTPADButtonLabel = QLabel(self.LEFTPADButtonFrame)
        self.LEFTPADButtonLabel.setObjectName(u"LEFTPADButtonLabel")
        sizePolicy3.setHeightForWidth(self.LEFTPADButtonLabel.sizePolicy().hasHeightForWidth())
        self.LEFTPADButtonLabel.setSizePolicy(sizePolicy3)
        self.LEFTPADButtonLabel.setMaximumSize(QSize(100, 100))
        self.LEFTPADButtonLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/Left Stick Click.svg"))
        self.LEFTPADButtonLabel.setScaledContents(True)

        self.horizontalLayout_35.addWidget(self.LEFTPADButtonLabel)

        self.LEFTPADButtonComboBox = QComboBox(self.LEFTPADButtonFrame)
        self.LEFTPADButtonComboBox.addItem("")
        self.LEFTPADButtonComboBox.addItem("")
        self.LEFTPADButtonComboBox.addItem("")
        self.LEFTPADButtonComboBox.addItem("")
        self.LEFTPADButtonComboBox.addItem("")
        self.LEFTPADButtonComboBox.addItem("")
        self.LEFTPADButtonComboBox.addItem("")
        self.LEFTPADButtonComboBox.addItem("")
        self.LEFTPADButtonComboBox.addItem("")
        self.LEFTPADButtonComboBox.addItem("")
        self.LEFTPADButtonComboBox.setObjectName(u"LEFTPADButtonComboBox")
        self.LEFTPADButtonComboBox.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_35.addWidget(self.LEFTPADButtonComboBox)


        self.verticalLayout_7.addWidget(self.LEFTPADButtonFrame)

        self.HOMEButtonFrame = QFrame(self.controllerSettingsSolidButtonsFrameInScrollArea)
        self.HOMEButtonFrame.setObjectName(u"HOMEButtonFrame")
        self.HOMEButtonFrame.setMaximumSize(QSize(16777215, 125))
        self.HOMEButtonFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.HOMEButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.HOMEButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.HOMEButtonFrame)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.HOMEButtonLabel = QLabel(self.HOMEButtonFrame)
        self.HOMEButtonLabel.setObjectName(u"HOMEButtonLabel")
        sizePolicy3.setHeightForWidth(self.HOMEButtonLabel.sizePolicy().hasHeightForWidth())
        self.HOMEButtonLabel.setSizePolicy(sizePolicy3)
        self.HOMEButtonLabel.setMaximumSize(QSize(100, 100))
        self.HOMEButtonLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/Home.svg"))
        self.HOMEButtonLabel.setScaledContents(True)

        self.horizontalLayout_29.addWidget(self.HOMEButtonLabel)

        self.HOMEButtonComboBox = QComboBox(self.HOMEButtonFrame)
        self.HOMEButtonComboBox.addItem("")
        self.HOMEButtonComboBox.addItem("")
        self.HOMEButtonComboBox.addItem("")
        self.HOMEButtonComboBox.addItem("")
        self.HOMEButtonComboBox.addItem("")
        self.HOMEButtonComboBox.addItem("")
        self.HOMEButtonComboBox.addItem("")
        self.HOMEButtonComboBox.addItem("")
        self.HOMEButtonComboBox.addItem("")
        self.HOMEButtonComboBox.addItem("")
        self.HOMEButtonComboBox.setObjectName(u"HOMEButtonComboBox")
        self.HOMEButtonComboBox.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_29.addWidget(self.HOMEButtonComboBox)


        self.verticalLayout_7.addWidget(self.HOMEButtonFrame)

        self.PADUPButtonFrame = QFrame(self.controllerSettingsSolidButtonsFrameInScrollArea)
        self.PADUPButtonFrame.setObjectName(u"PADUPButtonFrame")
        self.PADUPButtonFrame.setMaximumSize(QSize(16777215, 125))
        self.PADUPButtonFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.PADUPButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.PADUPButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.PADUPButtonFrame)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.PADUPButtonLabel = QLabel(self.PADUPButtonFrame)
        self.PADUPButtonLabel.setObjectName(u"PADUPButtonLabel")
        sizePolicy3.setHeightForWidth(self.PADUPButtonLabel.sizePolicy().hasHeightForWidth())
        self.PADUPButtonLabel.setSizePolicy(sizePolicy3)
        self.PADUPButtonLabel.setMaximumSize(QSize(100, 100))
        self.PADUPButtonLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/D-Pad Up.svg"))
        self.PADUPButtonLabel.setScaledContents(True)

        self.horizontalLayout_25.addWidget(self.PADUPButtonLabel)

        self.PADUPButtonComboBox = QComboBox(self.PADUPButtonFrame)
        self.PADUPButtonComboBox.addItem("")
        self.PADUPButtonComboBox.addItem("")
        self.PADUPButtonComboBox.addItem("")
        self.PADUPButtonComboBox.addItem("")
        self.PADUPButtonComboBox.addItem("")
        self.PADUPButtonComboBox.addItem("")
        self.PADUPButtonComboBox.addItem("")
        self.PADUPButtonComboBox.addItem("")
        self.PADUPButtonComboBox.addItem("")
        self.PADUPButtonComboBox.addItem("")
        self.PADUPButtonComboBox.setObjectName(u"PADUPButtonComboBox")
        self.PADUPButtonComboBox.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_25.addWidget(self.PADUPButtonComboBox)


        self.verticalLayout_7.addWidget(self.PADUPButtonFrame)

        self.PADDOWNButtonFrame = QFrame(self.controllerSettingsSolidButtonsFrameInScrollArea)
        self.PADDOWNButtonFrame.setObjectName(u"PADDOWNButtonFrame")
        self.PADDOWNButtonFrame.setMaximumSize(QSize(16777215, 125))
        self.PADDOWNButtonFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.PADDOWNButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.PADDOWNButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.PADDOWNButtonFrame)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.PADDOWNButtonLabel = QLabel(self.PADDOWNButtonFrame)
        self.PADDOWNButtonLabel.setObjectName(u"PADDOWNButtonLabel")
        sizePolicy3.setHeightForWidth(self.PADDOWNButtonLabel.sizePolicy().hasHeightForWidth())
        self.PADDOWNButtonLabel.setSizePolicy(sizePolicy3)
        self.PADDOWNButtonLabel.setMaximumSize(QSize(100, 100))
        self.PADDOWNButtonLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/D-Pad Down.svg"))
        self.PADDOWNButtonLabel.setScaledContents(True)

        self.horizontalLayout_36.addWidget(self.PADDOWNButtonLabel)

        self.PADDOWNButtonComboBox = QComboBox(self.PADDOWNButtonFrame)
        self.PADDOWNButtonComboBox.addItem("")
        self.PADDOWNButtonComboBox.addItem("")
        self.PADDOWNButtonComboBox.addItem("")
        self.PADDOWNButtonComboBox.addItem("")
        self.PADDOWNButtonComboBox.addItem("")
        self.PADDOWNButtonComboBox.addItem("")
        self.PADDOWNButtonComboBox.addItem("")
        self.PADDOWNButtonComboBox.addItem("")
        self.PADDOWNButtonComboBox.addItem("")
        self.PADDOWNButtonComboBox.addItem("")
        self.PADDOWNButtonComboBox.setObjectName(u"PADDOWNButtonComboBox")
        self.PADDOWNButtonComboBox.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_36.addWidget(self.PADDOWNButtonComboBox)


        self.verticalLayout_7.addWidget(self.PADDOWNButtonFrame)

        self.PADRIGHTButtonFrame = QFrame(self.controllerSettingsSolidButtonsFrameInScrollArea)
        self.PADRIGHTButtonFrame.setObjectName(u"PADRIGHTButtonFrame")
        self.PADRIGHTButtonFrame.setMaximumSize(QSize(16777215, 125))
        self.PADRIGHTButtonFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.PADRIGHTButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.PADRIGHTButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.PADRIGHTButtonFrame)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.PADRIGHTButtonLabel = QLabel(self.PADRIGHTButtonFrame)
        self.PADRIGHTButtonLabel.setObjectName(u"PADRIGHTButtonLabel")
        sizePolicy3.setHeightForWidth(self.PADRIGHTButtonLabel.sizePolicy().hasHeightForWidth())
        self.PADRIGHTButtonLabel.setSizePolicy(sizePolicy3)
        self.PADRIGHTButtonLabel.setMaximumSize(QSize(100, 100))
        self.PADRIGHTButtonLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/D-Pad Right.svg"))
        self.PADRIGHTButtonLabel.setScaledContents(True)

        self.horizontalLayout_33.addWidget(self.PADRIGHTButtonLabel)

        self.PADRIGHTButtonComboBox = QComboBox(self.PADRIGHTButtonFrame)
        self.PADRIGHTButtonComboBox.addItem("")
        self.PADRIGHTButtonComboBox.addItem("")
        self.PADRIGHTButtonComboBox.addItem("")
        self.PADRIGHTButtonComboBox.addItem("")
        self.PADRIGHTButtonComboBox.addItem("")
        self.PADRIGHTButtonComboBox.addItem("")
        self.PADRIGHTButtonComboBox.addItem("")
        self.PADRIGHTButtonComboBox.addItem("")
        self.PADRIGHTButtonComboBox.addItem("")
        self.PADRIGHTButtonComboBox.addItem("")
        self.PADRIGHTButtonComboBox.setObjectName(u"PADRIGHTButtonComboBox")
        self.PADRIGHTButtonComboBox.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_33.addWidget(self.PADRIGHTButtonComboBox)


        self.verticalLayout_7.addWidget(self.PADRIGHTButtonFrame)

        self.PADLEFTButtonFrame = QFrame(self.controllerSettingsSolidButtonsFrameInScrollArea)
        self.PADLEFTButtonFrame.setObjectName(u"PADLEFTButtonFrame")
        self.PADLEFTButtonFrame.setMaximumSize(QSize(16777215, 125))
        self.PADLEFTButtonFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.PADLEFTButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.PADLEFTButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.PADLEFTButtonFrame)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.PADLEFTButtonLabel = QLabel(self.PADLEFTButtonFrame)
        self.PADLEFTButtonLabel.setObjectName(u"PADLEFTButtonLabel")
        sizePolicy3.setHeightForWidth(self.PADLEFTButtonLabel.sizePolicy().hasHeightForWidth())
        self.PADLEFTButtonLabel.setSizePolicy(sizePolicy3)
        self.PADLEFTButtonLabel.setMaximumSize(QSize(100, 100))
        self.PADLEFTButtonLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/D-Pad Left.svg"))
        self.PADLEFTButtonLabel.setScaledContents(True)

        self.horizontalLayout_26.addWidget(self.PADLEFTButtonLabel)

        self.PADLEFTButtonComboBox = QComboBox(self.PADLEFTButtonFrame)
        self.PADLEFTButtonComboBox.addItem("")
        self.PADLEFTButtonComboBox.addItem("")
        self.PADLEFTButtonComboBox.addItem("")
        self.PADLEFTButtonComboBox.addItem("")
        self.PADLEFTButtonComboBox.addItem("")
        self.PADLEFTButtonComboBox.addItem("")
        self.PADLEFTButtonComboBox.addItem("")
        self.PADLEFTButtonComboBox.addItem("")
        self.PADLEFTButtonComboBox.addItem("")
        self.PADLEFTButtonComboBox.addItem("")
        self.PADLEFTButtonComboBox.setObjectName(u"PADLEFTButtonComboBox")
        self.PADLEFTButtonComboBox.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_26.addWidget(self.PADLEFTButtonComboBox)


        self.verticalLayout_7.addWidget(self.PADLEFTButtonFrame)

        self.RIGHTVERTICALAXISFrame = QFrame(self.controllerSettingsSolidButtonsFrameInScrollArea)
        self.RIGHTVERTICALAXISFrame.setObjectName(u"RIGHTVERTICALAXISFrame")
        self.RIGHTVERTICALAXISFrame.setMaximumSize(QSize(16777215, 125))
        self.RIGHTVERTICALAXISFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.RIGHTVERTICALAXISFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.RIGHTVERTICALAXISFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.RIGHTVERTICALAXISFrame)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.RIGHTVERTICALAXISLabel = QLabel(self.RIGHTVERTICALAXISFrame)
        self.RIGHTVERTICALAXISLabel.setObjectName(u"RIGHTVERTICALAXISLabel")
        sizePolicy3.setHeightForWidth(self.RIGHTVERTICALAXISLabel.sizePolicy().hasHeightForWidth())
        self.RIGHTVERTICALAXISLabel.setSizePolicy(sizePolicy3)
        self.RIGHTVERTICALAXISLabel.setMaximumSize(QSize(100, 100))
        self.RIGHTVERTICALAXISLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/Right Stick Up.svg"))
        self.RIGHTVERTICALAXISLabel.setScaledContents(True)

        self.horizontalLayout_40.addWidget(self.RIGHTVERTICALAXISLabel)

        self.RIGHTVERTICALAXISComboBox = QComboBox(self.RIGHTVERTICALAXISFrame)
        self.RIGHTVERTICALAXISComboBox.addItem("")
        self.RIGHTVERTICALAXISComboBox.addItem("")
        self.RIGHTVERTICALAXISComboBox.addItem("")
        self.RIGHTVERTICALAXISComboBox.addItem("")
        self.RIGHTVERTICALAXISComboBox.addItem("")
        self.RIGHTVERTICALAXISComboBox.addItem("")
        self.RIGHTVERTICALAXISComboBox.addItem("")
        self.RIGHTVERTICALAXISComboBox.addItem("")
        self.RIGHTVERTICALAXISComboBox.setObjectName(u"RIGHTVERTICALAXISComboBox")
        self.RIGHTVERTICALAXISComboBox.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_40.addWidget(self.RIGHTVERTICALAXISComboBox)


        self.verticalLayout_7.addWidget(self.RIGHTVERTICALAXISFrame)

        self.RIGHTHORIZONTALAXISFrame = QFrame(self.controllerSettingsSolidButtonsFrameInScrollArea)
        self.RIGHTHORIZONTALAXISFrame.setObjectName(u"RIGHTHORIZONTALAXISFrame")
        self.RIGHTHORIZONTALAXISFrame.setMaximumSize(QSize(16777215, 125))
        self.RIGHTHORIZONTALAXISFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.RIGHTHORIZONTALAXISFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.RIGHTHORIZONTALAXISFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.RIGHTHORIZONTALAXISFrame)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.RIGHTHORIZONTALAXISLabel = QLabel(self.RIGHTHORIZONTALAXISFrame)
        self.RIGHTHORIZONTALAXISLabel.setObjectName(u"RIGHTHORIZONTALAXISLabel")
        sizePolicy3.setHeightForWidth(self.RIGHTHORIZONTALAXISLabel.sizePolicy().hasHeightForWidth())
        self.RIGHTHORIZONTALAXISLabel.setSizePolicy(sizePolicy3)
        self.RIGHTHORIZONTALAXISLabel.setMaximumSize(QSize(100, 100))
        self.RIGHTHORIZONTALAXISLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/Right Stick Right.svg"))
        self.RIGHTHORIZONTALAXISLabel.setScaledContents(True)

        self.horizontalLayout_30.addWidget(self.RIGHTHORIZONTALAXISLabel)

        self.RIGHTHORIZONTALAXISComboBox = QComboBox(self.RIGHTHORIZONTALAXISFrame)
        self.RIGHTHORIZONTALAXISComboBox.addItem("")
        self.RIGHTHORIZONTALAXISComboBox.addItem("")
        self.RIGHTHORIZONTALAXISComboBox.addItem("")
        self.RIGHTHORIZONTALAXISComboBox.addItem("")
        self.RIGHTHORIZONTALAXISComboBox.addItem("")
        self.RIGHTHORIZONTALAXISComboBox.addItem("")
        self.RIGHTHORIZONTALAXISComboBox.addItem("")
        self.RIGHTHORIZONTALAXISComboBox.addItem("")
        self.RIGHTHORIZONTALAXISComboBox.setObjectName(u"RIGHTHORIZONTALAXISComboBox")
        self.RIGHTHORIZONTALAXISComboBox.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_30.addWidget(self.RIGHTHORIZONTALAXISComboBox)


        self.verticalLayout_7.addWidget(self.RIGHTHORIZONTALAXISFrame)

        self.LEFTVERTICALAXISFrame = QFrame(self.controllerSettingsSolidButtonsFrameInScrollArea)
        self.LEFTVERTICALAXISFrame.setObjectName(u"LEFTVERTICALAXISFrame")
        self.LEFTVERTICALAXISFrame.setMaximumSize(QSize(16777215, 125))
        self.LEFTVERTICALAXISFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.LEFTVERTICALAXISFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.LEFTVERTICALAXISFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.LEFTVERTICALAXISFrame)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.LEFTVERTICALAXISLabel = QLabel(self.LEFTVERTICALAXISFrame)
        self.LEFTVERTICALAXISLabel.setObjectName(u"LEFTVERTICALAXISLabel")
        sizePolicy3.setHeightForWidth(self.LEFTVERTICALAXISLabel.sizePolicy().hasHeightForWidth())
        self.LEFTVERTICALAXISLabel.setSizePolicy(sizePolicy3)
        self.LEFTVERTICALAXISLabel.setMaximumSize(QSize(100, 100))
        self.LEFTVERTICALAXISLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/Left Stick Up.svg"))
        self.LEFTVERTICALAXISLabel.setScaledContents(True)

        self.horizontalLayout_27.addWidget(self.LEFTVERTICALAXISLabel)

        self.LEFTVERTICALAXISComboBox = QComboBox(self.LEFTVERTICALAXISFrame)
        self.LEFTVERTICALAXISComboBox.addItem("")
        self.LEFTVERTICALAXISComboBox.addItem("")
        self.LEFTVERTICALAXISComboBox.addItem("")
        self.LEFTVERTICALAXISComboBox.addItem("")
        self.LEFTVERTICALAXISComboBox.addItem("")
        self.LEFTVERTICALAXISComboBox.addItem("")
        self.LEFTVERTICALAXISComboBox.addItem("")
        self.LEFTVERTICALAXISComboBox.addItem("")
        self.LEFTVERTICALAXISComboBox.setObjectName(u"LEFTVERTICALAXISComboBox")
        self.LEFTVERTICALAXISComboBox.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_27.addWidget(self.LEFTVERTICALAXISComboBox)


        self.verticalLayout_7.addWidget(self.LEFTVERTICALAXISFrame)

        self.LEFTHORIZONTALAXISFrame = QFrame(self.controllerSettingsSolidButtonsFrameInScrollArea)
        self.LEFTHORIZONTALAXISFrame.setObjectName(u"LEFTHORIZONTALAXISFrame")
        self.LEFTHORIZONTALAXISFrame.setMaximumSize(QSize(16777215, 125))
        self.LEFTHORIZONTALAXISFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.LEFTHORIZONTALAXISFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.LEFTHORIZONTALAXISFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.LEFTHORIZONTALAXISFrame)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.LEFTHORIZONTALAXISLabel = QLabel(self.LEFTHORIZONTALAXISFrame)
        self.LEFTHORIZONTALAXISLabel.setObjectName(u"LEFTHORIZONTALAXISLabel")
        sizePolicy3.setHeightForWidth(self.LEFTHORIZONTALAXISLabel.sizePolicy().hasHeightForWidth())
        self.LEFTHORIZONTALAXISLabel.setSizePolicy(sizePolicy3)
        self.LEFTHORIZONTALAXISLabel.setMaximumSize(QSize(100, 100))
        self.LEFTHORIZONTALAXISLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/Left Stick Right.svg"))
        self.LEFTHORIZONTALAXISLabel.setScaledContents(True)

        self.horizontalLayout_39.addWidget(self.LEFTHORIZONTALAXISLabel)

        self.LEFTHORIZONTALAXISComboBox = QComboBox(self.LEFTHORIZONTALAXISFrame)
        self.LEFTHORIZONTALAXISComboBox.addItem("")
        self.LEFTHORIZONTALAXISComboBox.addItem("")
        self.LEFTHORIZONTALAXISComboBox.addItem("")
        self.LEFTHORIZONTALAXISComboBox.addItem("")
        self.LEFTHORIZONTALAXISComboBox.addItem("")
        self.LEFTHORIZONTALAXISComboBox.addItem("")
        self.LEFTHORIZONTALAXISComboBox.addItem("")
        self.LEFTHORIZONTALAXISComboBox.addItem("")
        self.LEFTHORIZONTALAXISComboBox.setObjectName(u"LEFTHORIZONTALAXISComboBox")
        self.LEFTHORIZONTALAXISComboBox.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_39.addWidget(self.LEFTHORIZONTALAXISComboBox)


        self.verticalLayout_7.addWidget(self.LEFTHORIZONTALAXISFrame)

        self.RTButtonFrame = QFrame(self.controllerSettingsSolidButtonsFrameInScrollArea)
        self.RTButtonFrame.setObjectName(u"RTButtonFrame")
        self.RTButtonFrame.setMaximumSize(QSize(16777215, 125))
        self.RTButtonFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.RTButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.RTButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.RTButtonFrame)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.RTButtonLabel = QLabel(self.RTButtonFrame)
        self.RTButtonLabel.setObjectName(u"RTButtonLabel")
        sizePolicy3.setHeightForWidth(self.RTButtonLabel.sizePolicy().hasHeightForWidth())
        self.RTButtonLabel.setSizePolicy(sizePolicy3)
        self.RTButtonLabel.setMaximumSize(QSize(100, 100))
        self.RTButtonLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/Right Trigger.svg"))
        self.RTButtonLabel.setScaledContents(True)

        self.horizontalLayout_32.addWidget(self.RTButtonLabel)

        self.RTButtonComboBox = QComboBox(self.RTButtonFrame)
        self.RTButtonComboBox.addItem("")
        self.RTButtonComboBox.addItem("")
        self.RTButtonComboBox.addItem("")
        self.RTButtonComboBox.addItem("")
        self.RTButtonComboBox.addItem("")
        self.RTButtonComboBox.addItem("")
        self.RTButtonComboBox.addItem("")
        self.RTButtonComboBox.addItem("")
        self.RTButtonComboBox.setObjectName(u"RTButtonComboBox")
        self.RTButtonComboBox.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_32.addWidget(self.RTButtonComboBox)


        self.verticalLayout_7.addWidget(self.RTButtonFrame)

        self.LTButtonFrame = QFrame(self.controllerSettingsSolidButtonsFrameInScrollArea)
        self.LTButtonFrame.setObjectName(u"LTButtonFrame")
        self.LTButtonFrame.setMaximumSize(QSize(16777215, 125))
        self.LTButtonFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.LTButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.LTButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.LTButtonFrame)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.LTButtonLabel = QLabel(self.LTButtonFrame)
        self.LTButtonLabel.setObjectName(u"LTButtonLabel")
        sizePolicy3.setHeightForWidth(self.LTButtonLabel.sizePolicy().hasHeightForWidth())
        self.LTButtonLabel.setSizePolicy(sizePolicy3)
        self.LTButtonLabel.setMaximumSize(QSize(100, 100))
        self.LTButtonLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/Left Trigger.svg"))
        self.LTButtonLabel.setScaledContents(True)

        self.horizontalLayout_21.addWidget(self.LTButtonLabel)

        self.LTButtonComboBox = QComboBox(self.LTButtonFrame)
        self.LTButtonComboBox.addItem("")
        self.LTButtonComboBox.addItem("")
        self.LTButtonComboBox.addItem("")
        self.LTButtonComboBox.addItem("")
        self.LTButtonComboBox.addItem("")
        self.LTButtonComboBox.addItem("")
        self.LTButtonComboBox.addItem("")
        self.LTButtonComboBox.addItem("")
        self.LTButtonComboBox.setObjectName(u"LTButtonComboBox")
        self.LTButtonComboBox.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_21.addWidget(self.LTButtonComboBox)


        self.verticalLayout_7.addWidget(self.LTButtonFrame)


        self.horizontalLayout_20.addWidget(self.controllerSettingsSolidButtonsFrameInScrollArea)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_15.addWidget(self.scrollArea)


        self.verticalLayout_6.addWidget(self.controllerSettingsSolidButtonsFrame)

        self.saveSettingFrame = QFrame(self.controllerSettingsPageFrame)
        self.saveSettingFrame.setObjectName(u"saveSettingFrame")
        self.saveSettingFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.saveSettingFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.saveSettingFrame)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.saveSettingButton = QPushButton(self.saveSettingFrame)
        self.saveSettingButton.setObjectName(u"saveSettingButton")
        font5 = QFont()
        font5.setBold(False)
        font5.setItalic(False)
        font5.setUnderline(False)
        self.saveSettingButton.setFont(font5)
        self.saveSettingButton.setStyleSheet(u"QPushButton{\n"
"	font-size: 20px;\n"
"	border-radius: 5px; \n"
"	border: 3px solid #FFB86C;\n"
"}\n"
"")

        self.horizontalLayout_14.addWidget(self.saveSettingButton)


        self.verticalLayout_6.addWidget(self.saveSettingFrame)


        self.horizontalLayout_10.addWidget(self.controllerSettingsPageFrame)

        self.mainBodyStackedWidget.addWidget(self.controllerSettingsPage)

        self.horizontalLayout_7.addWidget(self.mainBodyStackedWidget)


        self.verticalLayout.addWidget(self.mainBodyFrame)

        self.footerFrame = QFrame(self.centralwidget)
        self.footerFrame.setObjectName(u"footerFrame")
        self.footerFrame.setMinimumSize(QSize(0, 20))
        self.footerFrame.setMaximumSize(QSize(16777215, 20))
        self.footerFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.footerFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.footerFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.footerVersionFrame = QFrame(self.footerFrame)
        self.footerVersionFrame.setObjectName(u"footerVersionFrame")
        self.footerVersionFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.footerVersionFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.footerVersionFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.footerVersionFrame)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)


        self.horizontalLayout.addWidget(self.footerVersionFrame, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)

        self.horizontalSpacer = QSpacerItem(733, 15, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.sizeGripFrame = QFrame(self.footerFrame)
        self.sizeGripFrame.setObjectName(u"sizeGripFrame")
        self.sizeGripFrame.setMinimumSize(QSize(20, 20))
        self.sizeGripFrame.setMaximumSize(QSize(20, 20))
        self.sizeGripFrame.setStyleSheet(u"QSizeGrip{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        self.sizeGripFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.sizeGripFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout.addWidget(self.sizeGripFrame)


        self.verticalLayout.addWidget(self.footerFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainBodyStackedWidget.setCurrentIndex(1)
        self.homePageStackedWidget.setCurrentIndex(1)
        self.profileTabs.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.navigationButton.setText("")
        self.tittleLabel.setText(QCoreApplication.translate("MainWindow", u"VortexUI", None))
        self.minimizeButton.setText("")
        self.maximizeButton.setText("")
        self.exitButton.setText("")
        self.homeButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.cameraButton.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.floatButton.setText(QCoreApplication.translate("MainWindow", u"Float", None))
        self.settingsButton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.fourThrustersLabel.setText("")
        self.upDownThrustersLabel.setText("")
        self.servoLabel.setText("")
        self.ledLabel.setText(QCoreApplication.translate("MainWindow", u"Led", None))
        self.gripperLabel.setText(QCoreApplication.translate("MainWindow", u"RightGripper", None))
        self.leftGripperLabel.setText(QCoreApplication.translate("MainWindow", u"LeftGripper", None))
        self.fluidSuctionLabel.setText(QCoreApplication.translate("MainWindow", u"FluidSuction", None))
        self.floatingDebrisLabel.setText(QCoreApplication.translate("MainWindow", u"FloatingDebris", None))
        self.altitudeHoldLabel.setText(QCoreApplication.translate("MainWindow", u"AltitudeHold", None))
        self.stabilizeFrameLabel.setText(QCoreApplication.translate("MainWindow", u"Stabilize", None))
        self.gainLabel.setText(QCoreApplication.translate("MainWindow", u"Gain", None))
        self.gainReadingLabel.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.phLael.setText(QCoreApplication.translate("MainWindow", u"PH", None))
        self.phSensorReadingLabel.setText(QCoreApplication.translate("MainWindow", u"7.1", None))
        self.headingLabel.setText(QCoreApplication.translate("MainWindow", u"Heading", None))
        self.headingReadingLabel.setText(QCoreApplication.translate("MainWindow", u"300", None))
        self.depthLabel.setText(QCoreApplication.translate("MainWindow", u"Depth", None))
        self.depthReadingLabel.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.floatLabel1.setText(QCoreApplication.translate("MainWindow", u"ROV MARGIN OF ERROR", None))
        self.graphDisplay1.setText(QCoreApplication.translate("MainWindow", u"graphDisplay", None))
        self.signalLabel1.setText(QCoreApplication.translate("MainWindow", u"No Signal Has Been Recieved Yet", None))
        self.startReading1.setText(QCoreApplication.translate("MainWindow", u"Start Reading", None))
        self.stopReading1.setText(QCoreApplication.translate("MainWindow", u"Stop Reading", None))
        self.profileTabs.setTabText(self.profileTabs.indexOf(self.profile1), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.floatLabel2.setText(QCoreApplication.translate("MainWindow", u"ROV MARGIN OF ERROR", None))
        self.graphDisplay2.setText(QCoreApplication.translate("MainWindow", u"graphDisplay", None))
        self.signalLabel2.setText(QCoreApplication.translate("MainWindow", u"No Signal Has Been Recieved Yet", None))
        self.startReading2.setText(QCoreApplication.translate("MainWindow", u"Start Reading", None))
        self.stopReading2.setText(QCoreApplication.translate("MainWindow", u"Stop Reading", None))
        self.profileTabs.setTabText(self.profileTabs.indexOf(self.profile2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.controllerSettingsButton.setText("")
        self.generalSettingsButton.setText(QCoreApplication.translate("MainWindow", u"General Settings", None))
        self.AButtonLabel.setText("")
        self.AButtonComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"RightGripper", None))
        self.AButtonComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"AltitudeHold", None))
        self.AButtonComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"CameraSwitch", None))
        self.AButtonComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"FloatingDebris", None))
        self.AButtonComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"FluidSuction", None))
        self.AButtonComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Led", None))
        self.AButtonComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"LeftGripper", None))
        self.AButtonComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Gain", None))
        self.AButtonComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Stabilize", None))
        self.AButtonComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"None", None))

        self.BButtonLabel.setText("")
        self.BButtonComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"LeftGripper", None))
        self.BButtonComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"AltitudeHold", None))
        self.BButtonComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"CameraSwitch", None))
        self.BButtonComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"FloatingDebris", None))
        self.BButtonComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"FluidSuction", None))
        self.BButtonComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Led", None))
        self.BButtonComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Gain", None))
        self.BButtonComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"RightGripper", None))
        self.BButtonComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Stabilize", None))
        self.BButtonComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"None", None))

        self.YButtonLabel.setText("")
        self.YButtonComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"FloatingDebris", None))
        self.YButtonComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"AltitudeHold", None))
        self.YButtonComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"CameraSwitch", None))
        self.YButtonComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"FluidSuction", None))
        self.YButtonComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Led", None))
        self.YButtonComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"LeftGripper", None))
        self.YButtonComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Gain", None))
        self.YButtonComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"RightGripper", None))
        self.YButtonComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Stabilize", None))
        self.YButtonComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"None", None))

        self.XButtonLabel.setText("")
        self.XButtonComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Led", None))
        self.XButtonComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"AltitudeHold", None))
        self.XButtonComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"CameraSwitch", None))
        self.XButtonComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"FloatingDebris", None))
        self.XButtonComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"FluidSuction", None))
        self.XButtonComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"LeftGripper", None))
        self.XButtonComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Gain", None))
        self.XButtonComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"RightGripper", None))
        self.XButtonComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Stabilize", None))
        self.XButtonComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"None", None))

        self.LBButtonLabel.setText("")
        self.LBButtonComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"FluidSuction", None))
        self.LBButtonComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"AltitudeHold", None))
        self.LBButtonComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"CameraSwitch", None))
        self.LBButtonComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"FloatingDebris", None))
        self.LBButtonComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Led", None))
        self.LBButtonComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"LeftGripper", None))
        self.LBButtonComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Gain", None))
        self.LBButtonComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"RightGripper", None))
        self.LBButtonComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Stabilize", None))
        self.LBButtonComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"None", None))

        self.RBButtonLabel.setText("")
        self.RBButtonComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"AltitudeHold", None))
        self.RBButtonComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"CameraSwitch", None))
        self.RBButtonComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"FloatingDebris", None))
        self.RBButtonComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"FluidSuction", None))
        self.RBButtonComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Led", None))
        self.RBButtonComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"LeftGripper", None))
        self.RBButtonComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Gain", None))
        self.RBButtonComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"RightGripper", None))
        self.RBButtonComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Stabilize", None))
        self.RBButtonComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"None", None))

        self.STARTButtonLabel.setText("")
        self.STARTButtonComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Gain", None))
        self.STARTButtonComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"AltitudeHold", None))
        self.STARTButtonComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"CameraSwitch", None))
        self.STARTButtonComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"FloatingDebris", None))
        self.STARTButtonComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"FluidSuction", None))
        self.STARTButtonComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Led", None))
        self.STARTButtonComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"LeftGripper", None))
        self.STARTButtonComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"RightGripper", None))
        self.STARTButtonComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Stabilize", None))
        self.STARTButtonComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"None", None))

        self.BACKButtonLabel.setText("")
        self.BACKButtonComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Stabilize", None))
        self.BACKButtonComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"AltitudeHold", None))
        self.BACKButtonComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"CameraSwitch", None))
        self.BACKButtonComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"FloatingDebris", None))
        self.BACKButtonComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"FluidSuction", None))
        self.BACKButtonComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Led", None))
        self.BACKButtonComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"LeftGripper", None))
        self.BACKButtonComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Gain", None))
        self.BACKButtonComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"RightGripper", None))
        self.BACKButtonComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"None", None))

        self.RIGHTPADButtonLabel.setText("")
        self.RIGHTPADButtonComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.RIGHTPADButtonComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"AltitudeHold", None))
        self.RIGHTPADButtonComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"CameraSwitch", None))
        self.RIGHTPADButtonComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"FloatingDebris", None))
        self.RIGHTPADButtonComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"FluidSuction", None))
        self.RIGHTPADButtonComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Led", None))
        self.RIGHTPADButtonComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"LeftGripper", None))
        self.RIGHTPADButtonComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Gain", None))
        self.RIGHTPADButtonComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"RightGripper", None))
        self.RIGHTPADButtonComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Stabilize", None))

        self.LEFTPADButtonLabel.setText("")
        self.LEFTPADButtonComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"CameraSwitch", None))
        self.LEFTPADButtonComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"AltitudeHold", None))
        self.LEFTPADButtonComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"FloatingDebris", None))
        self.LEFTPADButtonComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"FluidSuction", None))
        self.LEFTPADButtonComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Led", None))
        self.LEFTPADButtonComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"LeftGripper", None))
        self.LEFTPADButtonComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Gain", None))
        self.LEFTPADButtonComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"RightGripper", None))
        self.LEFTPADButtonComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Stabilize", None))
        self.LEFTPADButtonComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"None", None))

        self.HOMEButtonLabel.setText("")
        self.HOMEButtonComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.HOMEButtonComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"AltitudeHold", None))
        self.HOMEButtonComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"CameraSwitch", None))
        self.HOMEButtonComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"FloatingDebris", None))
        self.HOMEButtonComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"FluidSuction", None))
        self.HOMEButtonComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Led", None))
        self.HOMEButtonComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"LeftGripper", None))
        self.HOMEButtonComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Gain", None))
        self.HOMEButtonComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"RightGripper", None))
        self.HOMEButtonComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Stabilize", None))

        self.PADUPButtonLabel.setText("")
        self.PADUPButtonComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.PADUPButtonComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"AltitudeHold", None))
        self.PADUPButtonComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"CameraSwitch", None))
        self.PADUPButtonComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"FloatingDebris", None))
        self.PADUPButtonComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"FluidSuction", None))
        self.PADUPButtonComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Led", None))
        self.PADUPButtonComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"LeftGripper", None))
        self.PADUPButtonComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Gain", None))
        self.PADUPButtonComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"RightGripper", None))
        self.PADUPButtonComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Stabilize", None))

        self.PADDOWNButtonLabel.setText("")
        self.PADDOWNButtonComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.PADDOWNButtonComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"AltitudeHold", None))
        self.PADDOWNButtonComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"CameraSwitch", None))
        self.PADDOWNButtonComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"FluidSuction", None))
        self.PADDOWNButtonComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"FloatingDebris", None))
        self.PADDOWNButtonComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Led", None))
        self.PADDOWNButtonComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"LeftGripper", None))
        self.PADDOWNButtonComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Gain", None))
        self.PADDOWNButtonComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"RightGripper", None))
        self.PADDOWNButtonComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Stabilize", None))

        self.PADRIGHTButtonLabel.setText("")
        self.PADRIGHTButtonComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.PADRIGHTButtonComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"AltitudeHold", None))
        self.PADRIGHTButtonComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"CameraSwitch", None))
        self.PADRIGHTButtonComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"FloatingDebris", None))
        self.PADRIGHTButtonComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"FluidSuction", None))
        self.PADRIGHTButtonComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Led", None))
        self.PADRIGHTButtonComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"LeftGripper", None))
        self.PADRIGHTButtonComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Gain", None))
        self.PADRIGHTButtonComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"RightGripper", None))
        self.PADRIGHTButtonComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Stabilize", None))

        self.PADLEFTButtonLabel.setText("")
        self.PADLEFTButtonComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.PADLEFTButtonComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"AltitudeHold", None))
        self.PADLEFTButtonComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"CameraSwitch", None))
        self.PADLEFTButtonComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"FloatingDebris", None))
        self.PADLEFTButtonComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"FluidSuction", None))
        self.PADLEFTButtonComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Led", None))
        self.PADLEFTButtonComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"LeftGripper", None))
        self.PADLEFTButtonComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Gain", None))
        self.PADLEFTButtonComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"RightGripper", None))
        self.PADLEFTButtonComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Stabilize", None))

        self.RIGHTVERTICALAXISLabel.setText("")
        self.RIGHTVERTICALAXISComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Surge", None))
        self.RIGHTVERTICALAXISComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Heave", None))
        self.RIGHTVERTICALAXISComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Pitch", None))
        self.RIGHTVERTICALAXISComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Roll", None))
        self.RIGHTVERTICALAXISComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Servo", None))
        self.RIGHTVERTICALAXISComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Sway", None))
        self.RIGHTVERTICALAXISComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Yaw", None))
        self.RIGHTVERTICALAXISComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"None", None))

        self.RIGHTHORIZONTALAXISLabel.setText("")
        self.RIGHTHORIZONTALAXISComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Sway", None))
        self.RIGHTHORIZONTALAXISComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Heave", None))
        self.RIGHTHORIZONTALAXISComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Pitch", None))
        self.RIGHTHORIZONTALAXISComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Roll", None))
        self.RIGHTHORIZONTALAXISComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Servo", None))
        self.RIGHTHORIZONTALAXISComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Surge", None))
        self.RIGHTHORIZONTALAXISComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Yaw", None))
        self.RIGHTHORIZONTALAXISComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"None", None))

        self.LEFTVERTICALAXISLabel.setText("")
        self.LEFTVERTICALAXISComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Heave", None))
        self.LEFTVERTICALAXISComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Pitch", None))
        self.LEFTVERTICALAXISComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Roll", None))
        self.LEFTVERTICALAXISComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Servo", None))
        self.LEFTVERTICALAXISComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Surge", None))
        self.LEFTVERTICALAXISComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Sway", None))
        self.LEFTVERTICALAXISComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Yaw", None))
        self.LEFTVERTICALAXISComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"None", None))

        self.LEFTHORIZONTALAXISLabel.setText("")
        self.LEFTHORIZONTALAXISComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Yaw", None))
        self.LEFTHORIZONTALAXISComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Heave", None))
        self.LEFTHORIZONTALAXISComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Pitch", None))
        self.LEFTHORIZONTALAXISComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Roll", None))
        self.LEFTHORIZONTALAXISComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Servo", None))
        self.LEFTHORIZONTALAXISComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Surge", None))
        self.LEFTHORIZONTALAXISComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Sway", None))
        self.LEFTHORIZONTALAXISComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"None", None))

        self.RTButtonLabel.setText("")
        self.RTButtonComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Servo", None))
        self.RTButtonComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Heave", None))
        self.RTButtonComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Pitch", None))
        self.RTButtonComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Roll", None))
        self.RTButtonComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Surge", None))
        self.RTButtonComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Sway", None))
        self.RTButtonComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Yaw", None))
        self.RTButtonComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"None", None))

        self.LTButtonLabel.setText("")
        self.LTButtonComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Servo", None))
        self.LTButtonComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Heave", None))
        self.LTButtonComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Pitch", None))
        self.LTButtonComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Roll", None))
        self.LTButtonComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Surge", None))
        self.LTButtonComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Sway", None))
        self.LTButtonComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Yaw", None))
        self.LTButtonComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"None", None))

        self.saveSettingButton.setText(QCoreApplication.translate("MainWindow", u"Save Settings", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"v1.0", None))
    # retranslateUi

