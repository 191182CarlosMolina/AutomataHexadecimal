from importlib.resources import path
from msilib.schema import Class
from queue import Empty
from PySide2.QtWidgets import QWidget, QFileDialog, QTableWidget, QTableWidgetItem
from views.Ui_main_window import Form
import re
from PySide2 import QtCore
import aspose.words as aw
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from collections import Counter


class MainFormWindow (QWidget,Form):

    reg_exp = "[{a-f}{A-F}{0-9}]"
    eInicial = '#'

    def __init__(self):
        super().__init__()
        self.ui = Form()
        self.setupUi(self)

        self.btnCargarArchivo.clicked.connect(self.abrirArchivo)
        self.pushButtonCvGn.clicked.connect(self.mostrarGrafica)
        #self.verticalLayout.addWidget(self.generarGrafica)
        # self.grafica = GenerarGrafica()

    def abrirArchivo(self):
        self.limpiarTabla()
        file_path = QFileDialog.getOpenFileName()[0]
        self.lineEditCargarArchivo.setText(file_path)
        self.analizarArchivo(file_path)

    def analizarArchivo(self,file_path):
        textfile = open(file_path, 'r', encoding='utf-8')
        filetext = textfile.read()
        matches = re.findall(r'#\S{0}[a-fA-F0-9]{6}', filetext)
        #matches = re.findall(r'#\b\w*', filetext)
        print(matches)
        self.validarColores(matches)
        
        
    def generarGrafica(self, matches):

        contador = Counter(matches)
        listCValues = list(contador.values())
        listCKeys = list(contador.keys())

        tamanio = listCValues
        nombreColor = listCKeys
        colores = listCKeys

        plt.pie(tamanio, labels= nombreColor,autopct="%0.1f %%", colors=colores)
        plt.axis("equal")

    def generarTabla(self,matches):

        contador = Counter(matches)
        listCValues = list(contador.values())
        listCKeys = list(contador.keys())
        listCValueS = [str(x)for x in listCValues]
        
        fila = 0
        for dato in listCKeys:
            columna = 0
            self.tbl_Colores.insertRow(fila)
            celda = QTableWidgetItem(dato)
            self.tbl_Colores.setItem(fila, columna, celda)
            columna += 1
            fila += 1

        fila2 = 0
        for dato2 in listCValueS:
            columna2 = 0
            self.tbl_Colores_2.insertRow(fila2)
            celda2 = QTableWidgetItem(dato2)
            self.tbl_Colores_2.setItem(fila2, columna2, celda2)
            columna2 += 1
            fila2 += 1
        

    def mostrarGrafica(self):
        plt.show()

    
    def validarColores(self, matches):


        print('Tamanio i: ',len(matches))
        if len(matches):

            for i in range(len(matches)):

                color = matches[i]

                for x in range(1,7):
                    try:
                        bandera = self.verificar(self.reg_exp, color[x])
                        print('try:',bandera)
                    except IndexError:
                        bandera = False
                        print('except:', bandera)
                        break
                    if bandera is False:
                        break

            if bandera:
                self.generarTabla(matches)
                self.generarGrafica(matches)
            else:
                self.invalido()
        else:
            self.invalido()

    def verificar(self, exp, num):

        print('exp',exp)
        print('num',num)
        if re.match(exp, num) is not None:
            print('entro al match')
            return True
        return False

    def invalido(self):
        self.label.setText('No se encontraron colores hexadecimales')

    def limpiarTabla(self):
        self.tbl_Colores.clearContents()
        self.tbl_Colores_2.clearContents()

