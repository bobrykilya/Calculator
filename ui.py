# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Python34\graf.interface\calc.ui'
#
# Created: Sat Nov 30 16:40:56 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(670, 491)
        font = QtGui.QFont()
        font.setPointSize(8)
        Form.setFont(font)
        Form.setStyleSheet("QPushButton{\n"
"    background-color: white;\n"
"    width: 75px;\n"
"    height: 50px;\n"
"    font-sixe: 14px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: silver;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: pink;\n"
"}")
        self.gridLayoutWidget = QtGui.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(100, 100, 239, 251))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_7 = QtGui.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 0, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        self.pushButton_8 = QtGui.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 0, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 1, 1, 1)
        self.pushButton_9 = QtGui.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 0, 2, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 2, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 1, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 0, 1, 1)
        self.pushButton_6 = QtGui.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)
        self.pushButton_10 = QtGui.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 3, 1, 1, 1)
        self.pushButton_20 = QtGui.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout.addWidget(self.pushButton_20, 3, 0, 1, 1)
        self.pushButton_21 = QtGui.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setObjectName("pushButton_21")
        self.gridLayout.addWidget(self.pushButton_21, 3, 2, 1, 1)
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(100, 50, 231, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(350, 100, 81, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_13 = QtGui.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout.addWidget(self.pushButton_13)
        self.pushButton_15 = QtGui.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setObjectName("pushButton_15")
        self.verticalLayout.addWidget(self.pushButton_15)
        self.pushButton_12 = QtGui.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout.addWidget(self.pushButton_12)
        self.pushButton_11 = QtGui.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout.addWidget(self.pushButton_11)
        self.horizontalLayoutWidget = QtGui.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(100, 370, 241, 52))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_16 = QtGui.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setObjectName("pushButton_16")
        self.horizontalLayout.addWidget(self.pushButton_16)
        self.pushButton_17 = QtGui.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setObjectName("pushButton_17")
        self.horizontalLayout.addWidget(self.pushButton_17)
        self.pushButton_18 = QtGui.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setObjectName("pushButton_18")
        self.horizontalLayout.addWidget(self.pushButton_18)
        self.verticalLayoutWidget_2 = QtGui.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(350, 370, 81, 52))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_19 = QtGui.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setObjectName("pushButton_19")
        self.verticalLayout_2.addWidget(self.pushButton_19)
        self.verticalLayoutWidget_3 = QtGui.QWidget(Form)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(350, 40, 81, 52))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_14 = QtGui.QPushButton(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.verticalLayout_3.addWidget(self.pushButton_14)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_7.setText(QtGui.QApplication.translate("Form", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_8.setText(QtGui.QApplication.translate("Form", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Form", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_9.setText(QtGui.QApplication.translate("Form", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Form", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("Form", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("Form", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setText(QtGui.QApplication.translate("Form", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_10.setText(QtGui.QApplication.translate("Form", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_20.setText(QtGui.QApplication.translate("Form", "del", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_21.setText(QtGui.QApplication.translate("Form", "del", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_13.setText(QtGui.QApplication.translate("Form", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_15.setText(QtGui.QApplication.translate("Form", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_12.setText(QtGui.QApplication.translate("Form", "*", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_11.setText(QtGui.QApplication.translate("Form", "/", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_16.setText(QtGui.QApplication.translate("Form", "Х²", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_17.setText(QtGui.QApplication.translate("Form", "√x", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_18.setText(QtGui.QApplication.translate("Form", ",", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_19.setText(QtGui.QApplication.translate("Form", "=", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_14.setText(QtGui.QApplication.translate("Form", "C", None, QtGui.QApplication.UnicodeUTF8))



