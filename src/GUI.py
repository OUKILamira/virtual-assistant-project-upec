# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(861, 522)
        font = QtGui.QFont()
        font.setPointSize(7)
        MainWindow.setFont(font)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_left = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_left.setGeometry(QtCore.QRect(10, 10, 401, 481))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_left.setFont(font)
        self.groupBox_left.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_left.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_left.setObjectName("groupBox_left")
        self.Frame = QtWidgets.QFrame(self.groupBox_left)
        self.Frame.setGeometry(QtCore.QRect(10, 30, 381, 441))
        self.Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame.setObjectName("Frame")
        self.frame_3D = QtWidgets.QFrame(self.Frame)
        self.frame_3D.setGeometry(QtCore.QRect(0, 0, 381, 441))
        self.frame_3D.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3D.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3D.setObjectName("frame_3D")
        self.groupBox_right = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_right.setGeometry(QtCore.QRect(430, 10, 411, 481))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_right.setFont(font)
        self.groupBox_right.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_right.setObjectName("groupBox_right")
        self.groupBox_query = QtWidgets.QGroupBox(self.groupBox_right)
        self.groupBox_query.setGeometry(QtCore.QRect(9, 410, 391, 61))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_query.setFont(font)
        self.groupBox_query.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_query.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_query.setObjectName("groupBox_query")
        self.send_pushButton = QtWidgets.QPushButton(self.groupBox_query)
        self.send_pushButton.setGeometry(QtCore.QRect(320, 30, 51, 23))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.send_pushButton.setFont(font)
        self.send_pushButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.send_pushButton.setObjectName("send_pushButton")
        self.send_lineEdit = QtWidgets.QLineEdit(self.groupBox_query)
        self.send_lineEdit.setGeometry(QtCore.QRect(10, 30, 301, 21))
        self.send_lineEdit.setObjectName("send_lineEdit")
        self.room_textEdit = QtWidgets.QTextEdit(self.groupBox_right)
        self.room_textEdit.setGeometry(QtCore.QRect(10, 30, 391, 381))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.room_textEdit.setFont(font)
        self.room_textEdit.setObjectName("room_textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Virtual Assistant"))
        self.groupBox_left.setTitle(_translate("MainWindow", "Virtual Assistant"))
        self.groupBox_right.setTitle(_translate("MainWindow", "CHATBOT"))
        self.groupBox_query.setTitle(_translate("MainWindow", "Query"))
        self.send_pushButton.setText(_translate("MainWindow", "Send"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
