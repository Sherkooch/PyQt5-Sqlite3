from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3 as sql

class Ui_CourseWindow(object):
    def loadData(self):
        conn = sql.connect("Database Address in your PC")
        c = conn.cursor()
        result = c.execute("SELECT * FROM tbl_cort")
        self.tableWidget.setRowCount(0)
        
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        conn.close()
        
    def setupCORT(self, CourseWindow):
        CourseWindow.setObjectName("CourseWindow")
        CourseWindow.resize(644, 676)
        self.centralwidget = QtWidgets.QWidget(CourseWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 641, 501))
        self.tableWidget.setRowCount(7)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(155)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(59)
        self.tableWidget.verticalHeader().setDefaultSectionSize(66)
        self.LoadButton = QtWidgets.QPushButton(self.centralwidget)
        self.LoadButton.setGeometry(QtCore.QRect(270, 550, 121, 41))
        self.LoadButton.setObjectName("LoadButton")
        self.LoadButton.clicked.connect(self.loadData)
        CourseWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CourseWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 644, 26))
        self.menubar.setObjectName("menubar")
        CourseWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CourseWindow)
        self.statusbar.setObjectName("statusbar")
        CourseWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CourseWindow)
        QtCore.QMetaObject.connectSlotsByName(CourseWindow)

    def retranslateUi(self, CourseWindow):
        _translate = QtCore.QCoreApplication.translate
        CourseWindow.setWindowTitle(_translate("CourseWindow", "MainWindow"))
        self.LoadButton.setText(_translate("CourseWindow", "Click"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CourseWindow = QtWidgets.QMainWindow()
    ui = Ui_CourseWindow()
    ui.setupCORT(CourseWindow)
    CourseWindow.show()
    sys.exit(app.exec_())
