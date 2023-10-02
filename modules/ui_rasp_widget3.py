# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_rasp_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_rasp_widget(object):
    def setupUi(self, rasp_widget):
        rasp_widget.setObjectName("rasp_widget")
        rasp_widget.resize(363, 65)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(rasp_widget.sizePolicy().hasHeightForWidth())
        rasp_widget.setSizePolicy(sizePolicy)
        rasp_widget.setMinimumSize(QtCore.QSize(0, 0))
        rasp_widget.setStyleSheet("QGroupBox#infotimerasp{\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QGroupBox{\n"
"    border: 2px 2solid rgb(61, 70, 86);\n"
"}\n"
"")
        self.horizontalLayout = QtWidgets.QHBoxLayout(rasp_widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.infotimerasp = QtWidgets.QGroupBox(rasp_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infotimerasp.sizePolicy().hasHeightForWidth())
        self.infotimerasp.setSizePolicy(sizePolicy)
        self.infotimerasp.setMinimumSize(QtCore.QSize(0, 65))
        self.infotimerasp.setTitle("")
        self.infotimerasp.setObjectName("infotimerasp")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.infotimerasp)
        self.verticalLayout_2.setContentsMargins(5, 0, 9, 7)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.date = QtWidgets.QLabel(self.infotimerasp)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date.sizePolicy().hasHeightForWidth())
        self.date.setSizePolicy(sizePolicy)
        self.date.setStyleSheet("font: 14pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);")
        self.date.setObjectName("date")
        self.verticalLayout_2.addWidget(self.date)
        self.day = QtWidgets.QLabel(self.infotimerasp)
        self.day.setStyleSheet("\n"
"color: rgb(126, 126, 126);")
        self.day.setObjectName("day")
        self.verticalLayout_2.addWidget(self.day)
        self.raspitemcontainer = QtWidgets.QVBoxLayout()
        self.raspitemcontainer.setContentsMargins(0, 0, 0, 0)
        self.raspitemcontainer.setSpacing(0)
        self.raspitemcontainer.setObjectName("raspitemcontainer")
        self.verticalLayout_2.addLayout(self.raspitemcontainer)
        self.verticalLayout_2.setStretch(2, 2)
        self.horizontalLayout.addWidget(self.infotimerasp)

        self.retranslateUi(rasp_widget)
        QtCore.QMetaObject.connectSlotsByName(rasp_widget)

    def retranslateUi(self, rasp_widget):
        _translate = QtCore.QCoreApplication.translate
        rasp_widget.setWindowTitle(_translate("rasp_widget", "Form"))
        self.date.setText(_translate("rasp_widget", "20 Декабря"))
        self.day.setText(_translate("rasp_widget", "Понедельник"))
from . resources_rc import *