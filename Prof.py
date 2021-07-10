from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3 as sql
from Profinfo import *
from NewProf import *

class Ui_ProfWindow(object):
    
    def NewProf(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ProfInfoWindow()
        self.ui.setupPr(self.window)
        self.window.show()

    
    def GET_DATA(self):
        self.window = QtWidgets.QMainWindow()
        conn = sql.connect("DataBase Adress in your PC")
        c = conn.cursor()
        
        self.PRID_input = self.InputNumber.text()
        c.execute("SELECT * FROM tbl_prof WHERE PRID='{}'".format(self.PRID_input))
        
        self.ui = Ui_PRInfo(c.fetchone())
        self.ui.setupPrinfo(self.window)
        self.window.show()
        c.close()
    
    def setupPr(self, ProfWindow):
        ProfWindow.setObjectName("ProfWindow")
        ProfWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(ProfWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lable = QtWidgets.QLabel(self.centralwidget)
        self.lable.setGeometry(QtCore.QRect(310, 60, 211, 71))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lable.setFont(font)
        self.lable.setAlignment(QtCore.Qt.AlignCenter)
        self.lable.setObjectName("lable")
        self.ENTER_NAME_LABLE = QtWidgets.QLabel(self.centralwidget)
        self.ENTER_NAME_LABLE.setGeometry(QtCore.QRect(300, 210, 221, 71))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        self.ENTER_NAME_LABLE.setFont(font)
        self.ENTER_NAME_LABLE.setAlignment(QtCore.Qt.AlignCenter)
        self.ENTER_NAME_LABLE.setObjectName("ENTER_NAME_LABLE")
        self.InputNumber = QtWidgets.QLineEdit(self.centralwidget)
        self.InputNumber.setGeometry(QtCore.QRect(290, 280, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.InputNumber.setFont(font)
        self.InputNumber.setObjectName("InputNumber")
        self.SubmitButton = QtWidgets.QPushButton(self.centralwidget)
        self.SubmitButton.setGeometry(QtCore.QRect(180, 290, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.SubmitButton.setFont(font)
        self.SubmitButton.setObjectName("SubmitButton")
        self.SubmitButton.clicked.connect(self.GET_DATA)
        self.NewProfLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.NewProfLinkButton.setGeometry(QtCore.QRect(350, 330, 121, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.LinkVisited, brush)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.NewProfLinkButton.setFont(font)
        self.NewProfLinkButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.NewProfLinkButton.setToolTipDuration(-1)
        self.NewProfLinkButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon.fromTheme("l")
        self.NewProfLinkButton.setIcon(icon)
        self.NewProfLinkButton.setAutoDefault(False)
        self.NewProfLinkButton.setObjectName("NewProfLinkButton")
        self.NewProfLinkButton.clicked.connect(self.NewProf)
        ProfWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ProfWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        ProfWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ProfWindow)
        self.statusbar.setObjectName("statusbar")
        ProfWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ProfWindow)
        QtCore.QMetaObject.connectSlotsByName(ProfWindow)

    def retranslateUi(self, ProfWindow):
        _translate = QtCore.QCoreApplication.translate
        ProfWindow.setWindowTitle(_translate("ProfWindow", "Profesors"))
        self.lable.setText(_translate("ProfWindow", "Prof Panel"))
        self.ENTER_NAME_LABLE.setText(_translate("ProfWindow", ":Enter Pr ID"))
        self.SubmitButton.setText(_translate("ProfWindow", "submit"))
        self.NewProfLinkButton.setText(_translate("ProfWindow", "New Professor"))
        
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProfWindow = QtWidgets.QMainWindow()
    ui = Ui_ProfWindow()
    ui.setupPr(ProfWindow)
    ProfWindow.show()
    sys.exit(app.exec_())
