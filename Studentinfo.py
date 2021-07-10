from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3 as sql
from PyQt5.QtWidgets import QMessageBox
from StudentinfoEdit import *

class Ui_StInfoWindowNotNew(object):
    
    def __init__(self, row):
        self.STID = row[0]
        self.STNAME = row[1]
        self.STLEV = row[2]
        self.STMJR = row[3]
        self.AGE = row[4]
        self.STATUS = row[5]

    def Delete_ST(self):
        conn = sql.connect("Database Address in your PC")
        c = conn.cursor()
        c.execute("DELETE FROM tbl_stt WHERE STID='{}'".format(self.STID))
        conn.commit()
        c.close()
        self.popup_error()
        
    def setupStinfo(self, StInfoWindowNotNew):
        StInfoWindowNotNew.setObjectName("StInfoWindowNotNew")
        StInfoWindowNotNew.resize(847, 469)
        self.centralwidget = QtWidgets.QWidget(StInfoWindowNotNew)
        self.centralwidget.setObjectName("centralwidget")
        self.StName_label = QtWidgets.QLabel(self.centralwidget)
        self.StName_label.setGeometry(QtCore.QRect(560, 190, 111, 41))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(13)
        self.StName_label.setFont(font)
        self.StName_label.setAlignment(QtCore.Qt.AlignCenter)
        self.StName_label.setObjectName("StName_label")
        self.StAge_label = QtWidgets.QLabel(self.centralwidget)
        self.StAge_label.setGeometry(QtCore.QRect(560, 280, 51, 41))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(13)
        self.StAge_label.setFont(font)
        self.StAge_label.setAlignment(QtCore.Qt.AlignCenter)
        self.StAge_label.setObjectName("StAge_label")
        self.StMjr_label = QtWidgets.QLabel(self.centralwidget)
        self.StMjr_label.setGeometry(QtCore.QRect(220, 100, 111, 41))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(13)
        self.StMjr_label.setFont(font)
        self.StMjr_label.setAlignment(QtCore.Qt.AlignCenter)
        self.StMjr_label.setObjectName("StMjr_label")
        self.StLev_label = QtWidgets.QLabel(self.centralwidget)
        self.StLev_label.setGeometry(QtCore.QRect(230, 190, 101, 41))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(13)
        self.StLev_label.setFont(font)
        self.StLev_label.setAlignment(QtCore.Qt.AlignCenter)
        self.StLev_label.setObjectName("StLev_label")
        self.StNum_label = QtWidgets.QLabel(self.centralwidget)
        self.StNum_label.setGeometry(QtCore.QRect(560, 100, 141, 41))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(13)
        self.StNum_label.setFont(font)
        self.StNum_label.setAlignment(QtCore.Qt.AlignCenter)
        self.StNum_label.setObjectName("StNum_label")
        self.StStatus_label = QtWidgets.QLabel(self.centralwidget)
        self.StStatus_label.setGeometry(QtCore.QRect(230, 280, 111, 41))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(13)
        self.StStatus_label.setFont(font)
        self.StStatus_label.setAlignment(QtCore.Qt.AlignCenter)
        self.StStatus_label.setObjectName("StStatus_label")
        self.SubmitButton = QtWidgets.QPushButton(self.centralwidget)
        self.SubmitButton.setGeometry(QtCore.QRect(390, 340, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.SubmitButton.setFont(font)
        self.SubmitButton.setObjectName("SubmitButton")
        self.SubmitButton.clicked.connect(self.Delete_ST)
        self.StAge_show = QtWidgets.QLabel(self.centralwidget)
        self.StAge_show.setGeometry(QtCore.QRect(400, 280, 141, 41))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(13)
        self.StAge_show.setFont(font)
        self.StAge_show.setText(self.AGE)
        self.StAge_show.setAlignment(QtCore.Qt.AlignCenter)
        self.StAge_show.setObjectName("StAge_show")
        self.StName_show = QtWidgets.QLabel(self.centralwidget)
        self.StName_show.setGeometry(QtCore.QRect(400, 190, 141, 41))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(13)
        self.StName_show.setFont(font)
        self.StName_show.setText(self.STNAME)
        self.StName_show.setAlignment(QtCore.Qt.AlignCenter)
        self.StName_show.setObjectName("StName_show")
        self.StNum_show = QtWidgets.QLabel(self.centralwidget)
        self.StNum_show.setGeometry(QtCore.QRect(400, 100, 141, 41))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(13)
        self.StNum_show.setFont(font)
        self.StNum_show.setText(self.STID)
        self.StNum_show.setAlignment(QtCore.Qt.AlignCenter)
        self.StNum_show.setObjectName("StNum_show")
        self.StStatus_show = QtWidgets.QLabel(self.centralwidget)
        self.StStatus_show.setGeometry(QtCore.QRect(60, 280, 141, 41))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(13)
        self.StStatus_show.setFont(font)
        self.StStatus_show.setText(self.STATUS)
        self.StStatus_show.setAlignment(QtCore.Qt.AlignCenter)
        self.StStatus_show.setObjectName("StStatus_show")
        self.StLev_show = QtWidgets.QLabel(self.centralwidget)
        self.StLev_show.setGeometry(QtCore.QRect(60, 190, 141, 41))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(13)
        self.StLev_show.setFont(font)
        self.StLev_show.setText(self.STLEV)
        self.StLev_show.setAlignment(QtCore.Qt.AlignCenter)
        self.StLev_show.setObjectName("StLev_show")
        self.StMjr_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.StMjr_label_2.setGeometry(QtCore.QRect(60, 100, 141, 41))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(13)
        self.StMjr_label_2.setFont(font)
        self.StMjr_label_2.setText(self.STMJR)
        self.StMjr_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.StMjr_label_2.setObjectName("StMjr_label_2")
        self.StNum_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.StNum_label_3.setGeometry(QtCore.QRect(370, 30, 171, 41))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.StNum_label_3.setFont(font)
        self.StNum_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.StNum_label_3.setObjectName("StNum_label_3")
        StInfoWindowNotNew.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StInfoWindowNotNew)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 847, 26))
        self.menubar.setObjectName("menubar")
        StInfoWindowNotNew.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(StInfoWindowNotNew)
        self.statusbar.setObjectName("statusbar")
        StInfoWindowNotNew.setStatusBar(self.statusbar)

        self.retranslateUi(StInfoWindowNotNew)
        QtCore.QMetaObject.connectSlotsByName(StInfoWindowNotNew)

    def retranslateUi(self, StInfoWindowNotNew):
        _translate = QtCore.QCoreApplication.translate
        StInfoWindowNotNew.setWindowTitle(_translate("StInfoWindowNotNew", "Student Info"))
        self.StName_label.setText(_translate("StInfoWindowNotNew", ":Name"))
        self.StAge_label.setText(_translate("StInfoWindowNotNew", ":Age"))
        self.StMjr_label.setText(_translate("StInfoWindowNotNew", ":Major"))
        self.StLev_label.setText(_translate("StInfoWindowNotNew", ":Level"))
        self.StNum_label.setText(_translate("StInfoWindowNotNew", ":St Id"))
        self.StStatus_label.setText(_translate("StInfoWindowNotNew", "Still Edu:"))
        self.SubmitButton.setText(_translate("StInfoWindowNotNew", "Delete St"))
        self.StNum_label_3.setText(_translate("StInfoWindowNotNew", "Student Info"))
        
    def popup_error(self):
        msg = QMessageBox()
        msg.setWindowTitle("Not Found")
        msg.setText("Student Deleted")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StInfoWindowNotNew = QtWidgets.QMainWindow()
    ui = Ui_StInfoWindowNotNew()
    ui.setupStinfo(StInfoWindowNotNew)
    StInfoWindowNotNew.show()
    sys.exit(app.exec_())
