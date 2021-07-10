from PyQt5 import QtCore, QtGui, QtWidgets
from GradeSub import *
import sqlite3 as sql

class Ui_SCPTWindow(object):
    def loadData(self):
        conn = sql.connect("Database Address in your PC")
        c = conn.cursor()
        result = c.execute("SELECT * FROM tbl_scpt")
        self.tableWidget.setRowCount(0)
        
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        conn.commit
        c.close()
    
    def subpage(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_GradeSub()
        self.ui.setupGSub(self.window)
        self.window.show()
    
    def setupSCPT(self, SCPTWindow):
        SCPTWindow.setObjectName("SCPTWindow")
        SCPTWindow.resize(985, 729)
        self.centralwidget = QtWidgets.QWidget(SCPTWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 0, 971, 551))
        self.tableWidget.setAutoScrollMargin(16)
        self.tableWidget.setRowCount(15)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(133)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(47)
        self.tableWidget.verticalHeader().setDefaultSectionSize(34)
        self.ShowButton = QtWidgets.QPushButton(self.centralwidget)
        self.ShowButton.setGeometry(QtCore.QRect(480, 590, 93, 28))
        self.ShowButton.setObjectName("ShowButton")
        self.ShowButton.clicked.connect(self.loadData)
        self.SubScore = QtWidgets.QPushButton(self.centralwidget)
        self.SubScore.setGeometry(QtCore.QRect(480, 640, 93, 28))
        self.SubScore.setObjectName("SubScore")
        self.SubScore.clicked.connect(self.subpage)
        SCPTWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SCPTWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 985, 26))
        self.menubar.setObjectName("menubar")
        SCPTWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SCPTWindow)
        self.statusbar.setObjectName("statusbar")
        SCPTWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SCPTWindow)
        QtCore.QMetaObject.connectSlotsByName(SCPTWindow)

    def retranslateUi(self, SCPTWindow):
        _translate = QtCore.QCoreApplication.translate
        SCPTWindow.setWindowTitle(_translate("SCPTWindow", "SCPT"))
        self.ShowButton.setText(_translate("SCPTWindow", "Show"))
        self.SubScore.setText(_translate("SCPTWindow", "Submit Scores"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SCPTWindow = QtWidgets.QMainWindow()
    ui = Ui_SCPTWindow()
    ui.setupSCPT(SCPTWindow)
    SCPTWindow.show()
    sys.exit(app.exec_())
