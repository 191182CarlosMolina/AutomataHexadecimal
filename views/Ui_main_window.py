# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(783, 585)
        Form.setStyleSheet(u"background-color: rgb(207, 207, 207);\n"
"background-color: rgb(232, 232, 232);")
        self.lineEditCargarArchivo = QLineEdit(Form)
        self.lineEditCargarArchivo.setObjectName(u"lineEditCargarArchivo")
        self.lineEditCargarArchivo.setGeometry(QRect(10, 10, 381, 41))
        font = QFont()
        font.setPointSize(9)
        self.lineEditCargarArchivo.setFont(font)
        self.lineEditCargarArchivo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btnCargarArchivo = QPushButton(Form)
        self.btnCargarArchivo.setObjectName(u"btnCargarArchivo")
        self.btnCargarArchivo.setGeometry(QRect(430, 10, 321, 41))
        self.btnCargarArchivo.setFont(font)
        self.btnCargarArchivo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButtonCvGn = QPushButton(Form)
        self.pushButtonCvGn.setObjectName(u"pushButtonCvGn")
        self.pushButtonCvGn.setGeometry(QRect(430, 70, 321, 41))
        self.pushButtonCvGn.setFont(font)
        self.pushButtonCvGn.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelArchivos = QLabel(Form)
        self.labelArchivos.setObjectName(u"labelArchivos")
        self.labelArchivos.setEnabled(True)
        self.labelArchivos.setGeometry(QRect(20, 60, 92, 18))
        self.labelArchivos.setFont(font)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 130, 371, 41))
        font1 = QFont()
        font1.setPointSize(13)
        self.label.setFont(font1)
        self.tbl_Colores = QTableWidget(Form)
        if (self.tbl_Colores.columnCount() < 1):
            self.tbl_Colores.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_Colores.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tbl_Colores.setObjectName(u"tbl_Colores")
        self.tbl_Colores.setGeometry(QRect(270, 180, 121, 371))
        self.tbl_Colores_2 = QTableWidget(Form)
        if (self.tbl_Colores_2.columnCount() < 1):
            self.tbl_Colores_2.setColumnCount(1)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_Colores_2.setHorizontalHeaderItem(0, __qtablewidgetitem1)
        self.tbl_Colores_2.setObjectName(u"tbl_Colores_2")
        self.tbl_Colores_2.setGeometry(QRect(390, 180, 121, 371))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btnCargarArchivo.setText(QCoreApplication.translate("Form", u"Buscar y Cargar archivo", None))
        self.pushButtonCvGn.setText(QCoreApplication.translate("Form", u"Generar Paleta de Coleres", None))
        self.labelArchivos.setText(QCoreApplication.translate("Form", u"Archivos .html", None))
        self.label.setText(QCoreApplication.translate("Form", u"TABLA DE FRECUENCIA DE COLORES", None))
        ___qtablewidgetitem = self.tbl_Colores.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Color", None));
        ___qtablewidgetitem1 = self.tbl_Colores_2.horizontalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Frecuencia", None));
    # retranslateUi

