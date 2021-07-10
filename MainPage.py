from PyQt5 import QtCore, QtGui, QtWidgets
from Student import *
from CourseWindow import *
from Prof import *
from SCPT import *

class Ui_MainWindow(object):

    # Open Student Page
    def Student(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_StudentWindow()
        self.ui.setupSt(self.window)
        self.window.show()
    
    # Open Course Page
    def Course(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CourseWindow()
        self.ui.setupCORT(self.window)
        self.window.show()

    # Open Prof Page
    def Prof(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ProfWindow()
        self.ui.setupPr(self.window)
        self.window.show()
    
    # Open Score Page
    def Score(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SCPTWindow()
        self.ui.setupSCPT(self.window)
        self.window.show()
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(696, 638)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(200, 30, 301, 91))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.header.setFont(font)
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")
        self.Studentbutton = QtWidgets.QPushButton(self.centralwidget)
        self.Studentbutton.setGeometry(QtCore.QRect(250, 150, 211, 71))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Studentbutton.setFont(font)
        self.Studentbutton.setObjectName("Studentbutton")
        self.Studentbutton.clicked.connect(self.Student) # Links to Student Method, Makes Button Work
        self.ProfButton = QtWidgets.QPushButton(self.centralwidget)
        self.ProfButton.setGeometry(QtCore.QRect(250, 420, 211, 71))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ProfButton.setFont(font)
        self.ProfButton.setObjectName("ProfButton")
        self.ProfButton.clicked.connect(self.Prof) # Links to Prof Method, Makes Button Work
        self.UnitsButton = QtWidgets.QPushButton(self.centralwidget)
        self.UnitsButton.setGeometry(QtCore.QRect(250, 330, 211, 71))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.UnitsButton.setFont(font)
        self.UnitsButton.setObjectName("UnitsButton")
        self.UnitsButton.clicked.connect(self.Score) # Links to Score Method, Makes Button Work
        self.CourseButton = QtWidgets.QPushButton(self.centralwidget)
        self.CourseButton.setGeometry(QtCore.QRect(250, 240, 211, 71))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.CourseButton.setFont(font)
        self.CourseButton.setObjectName("CourseButton")
        self.CourseButton.clicked.connect(self.Course) # Links to Course Method, Makes Button Work
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 696, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.header.setText(_translate("MainWindow", "Main Page"))
        self.Studentbutton.setText(_translate("MainWindow", "Students"))
        self.ProfButton.setText(_translate("MainWindow", "Professors"))
        self.UnitsButton.setText(_translate("MainWindow", "Scores"))
        self.CourseButton.setText(_translate("MainWindow", "Courses"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
