from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3 as sql
from PyQt5.QtWidgets import QMessageBox

class Ui_GradeSub(object):
    def doAll(self):
        conn = sql.connect("DataBase Address in your PC")
        c = conn.cursor()
        self.Row = self.RowNum_input.text()
        self.Grade = self.Grade_input.text()
        result = c.execute("UPDATE tbl_scpt SET GRADE = (?) WHERE row_num = (?)",(self.Grade, self.Row))
        conn.commit()
        c.close()
        self.popup_error()
    
    def setupGSub(self, GradeSub):
        GradeSub.setObjectName("GradeSub")
        GradeSub.resize(426, 369)
        font = QtGui.QFont()
        font.setPointSize(11)
        GradeSub.setFont(font)
        self.centralwidget = QtWidgets.QWidget(GradeSub)
        self.centralwidget.setObjectName("centralwidget")
        self.RowNum_input = QtWidgets.QLineEdit(self.centralwidget)
        self.RowNum_input.setGeometry(QtCore.QRect(150, 110, 141, 31))
        self.RowNum_input.setObjectName("RowNum_input")
        self.Grade_input = QtWidgets.QLineEdit(self.centralwidget)
        self.Grade_input.setGeometry(QtCore.QRect(150, 210, 141, 31))
        self.Grade_input.setObjectName("Grade_input")
        self.RowNum_label = QtWidgets.QLabel(self.centralwidget)
        self.RowNum_label.setGeometry(QtCore.QRect(170, 60, 101, 31))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.RowNum_label.setFont(font)
        self.RowNum_label.setObjectName("RowNum_label")
        self.Grade_label = QtWidgets.QLabel(self.centralwidget)
        self.Grade_label.setGeometry(QtCore.QRect(190, 160, 51, 31))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Grade_label.setFont(font)
        self.Grade_label.setObjectName("Grade_label")
        self.SubmitButton = QtWidgets.QPushButton(self.centralwidget)
        self.SubmitButton.setGeometry(QtCore.QRect(180, 290, 81, 28))
        self.SubmitButton.setObjectName("SubmitButton")
        self.SubmitButton.clicked.connect(self.doAll)
        GradeSub.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(GradeSub)
        self.statusbar.setObjectName("statusbar")
        GradeSub.setStatusBar(self.statusbar)

        self.retranslateUi(GradeSub)
        QtCore.QMetaObject.connectSlotsByName(GradeSub)

    def retranslateUi(self, GradeSub):
        _translate = QtCore.QCoreApplication.translate
        GradeSub.setWindowTitle(_translate("GradeSub", "Grade Sub"))
        self.RowNum_label.setText(_translate("GradeSub", "Row Num"))
        self.Grade_label.setText(_translate("GradeSub", "Score"))
        self.SubmitButton.setText(_translate("GradeSub", "Sumbit"))

    def popup_error(self):
        msg = QMessageBox()
        msg.setWindowTitle("Not Found")
        msg.setText("Score Submited")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GradeSub = QtWidgets.QMainWindow()
    ui = Ui_GradeSub()
    ui.setupGSub(GradeSub)
    GradeSub.show()
    sys.exit(app.exec_())
