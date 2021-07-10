from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
import sqlite3 as sql
from NewStudent import *
from Studentinfo import *

class Ui_StudentWindow(object):
    def NewStudent(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_StInfoWindow()
        self.ui.setupStInfo(self.window)
        self.window.show()

    # Connects to DB And Searchs in it
    def GET_DATA(self):
        self.window = QtWidgets.QMainWindow()
        conn = sql.connect("Database Address in your PC")
        c = conn.cursor()
        
        self.STID_input = self.InputNumber.text()
        c.execute("SELECT * FROM tbl_stt WHERE STID='{}'".format(self.STID_input))

        self.ui = Ui_StInfoWindowNotNew(c.fetchone())
        self.ui.setupStinfo(self.window)
        self.window.show()
        conn.commit()
        c.close()
    
    def setupSt(self, StudentWindow):
        StudentWindow.setObjectName("StudentWindow")
        StudentWindow.resize(800, 600)
        StudentWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        StudentWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(StudentWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 50, 271, 81))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.ENTER_NAME_LABLE = QtWidgets.QLabel(self.centralwidget)
        self.ENTER_NAME_LABLE.setGeometry(QtCore.QRect(300, 210, 221, 71))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        self.ENTER_NAME_LABLE.setFont(font)
        self.ENTER_NAME_LABLE.setAlignment(QtCore.Qt.AlignCenter)
        self.ENTER_NAME_LABLE.setObjectName("ENTER_NAME_LABLE")
        self.InputNumber = QtWidgets.QLineEdit(self.centralwidget)
        self.InputNumber.setGeometry(QtCore.QRect(290, 290, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.InputNumber.setFont(font)
        self.InputNumber.setObjectName("InputNumber")

        self.SubmitButton = QtWidgets.QPushButton(self.centralwidget)
        self.SubmitButton.setGeometry(QtCore.QRect(180, 300, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.SubmitButton.setFont(font)
        self.SubmitButton.setObjectName("SubmitButton")
        self.SubmitButton.clicked.connect(self.GET_DATA)
        
        self.NewStudentLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.NewStudentLinkButton.setGeometry(QtCore.QRect(320, 340, 170, 31))
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
        self.NewStudentLinkButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("B Koodak")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.NewStudentLinkButton.setFont(font)
        self.NewStudentLinkButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.NewStudentLinkButton.setToolTipDuration(-1)
        self.NewStudentLinkButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon.fromTheme("l")
        self.NewStudentLinkButton.setIcon(icon)
        self.NewStudentLinkButton.setAutoDefault(False)
        self.NewStudentLinkButton.setObjectName("NewStudentLinkButton")
        self.NewStudentLinkButton.clicked.connect(self.NewStudent)
        StudentWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StudentWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        StudentWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(StudentWindow)
        self.statusbar.setObjectName("statusbar")
        StudentWindow.setStatusBar(self.statusbar)
        self.retranslateUi(StudentWindow)
        QtCore.QMetaObject.connectSlotsByName(StudentWindow)

    def retranslateUi(self, StudentWindow):
        _translate = QtCore.QCoreApplication.translate
        StudentWindow.setWindowTitle(_translate("StudentWindow", "Student"))
        self.label.setText(_translate("StudentWindow", "Students' Panel"))
        self.ENTER_NAME_LABLE.setText(_translate("StudentWindow", "Enter a Student ID:"))
        self.SubmitButton.setText(_translate("StudentWindow", "submit"))
        self.NewStudentLinkButton.setText(_translate("StudentWindow", "Create a new Student"))

    def popup_error(self):
        msg = QMessageBox()
        msg.setWindowTitle("Not Found")
        msg.setText("NO Student with this Student ID!")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()
        
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StudentWindow = QtWidgets.QMainWindow()
    ui = Ui_StudentWindow()
    ui.setupSt(StudentWindow)
    StudentWindow.show()
    sys.exit(app.exec_())
