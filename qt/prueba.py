# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prueba.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 480)
        MainWindow.setStyleSheet(_fromUtf8("/*Cambiamos el color de la ventana*/\n"
"    #MainWindow{\n"
"        background-color: #3f51b5;\n"
"    }\n"
"\n"
"\n"
"  #Enviar{\n"
"\n"
"}\n"
"\n"
"/*Estilos para el botón*/\n"
"    QPushButton{\n"
"        background-color: #ff5722;\n"
"        border-radius: 4px;\n"
"        color: #fff;\n"
"        font-family: \'Roboto\';\n"
"        font-size: 17px;\n"
"    }\n"
"\n"
"\n"
"    /*Definimos los estilos para los QLineEdit*/\n"
"    QLineEdit{\n"
"        border-radius: 3px;\n"
"        border: 2px solid #303f9f;\n"
"         color: #212121;\n"
"    background-color: rgb(255, 255, 255);\n"
"    }\n"
"\n"
"QLCDNumber{\n"
" border-radius: 3px;\n"
"        border: 2px solid #303f9f;\n"
"         color: #212121;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QSlider{\n"
" border-radius: 3px;\n"
"        border: 2px solid #303f9f;\n"
"         color: #212121;\n"
"    background-color: #3f51b59f;\n"
"}"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 50, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 50, 113, 26))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.Enviar = QtGui.QPushButton(self.centralwidget)
        self.Enviar.setGeometry(QtCore.QRect(420, 50, 91, 27))
        self.Enviar.setObjectName(_fromUtf8("Enviar"))
        self.verticalSlider = QtGui.QSlider(self.centralwidget)
        self.verticalSlider.setGeometry(QtCore.QRect(70, 180, 17, 160))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName(_fromUtf8("verticalSlider"))
        self.lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(40, 140, 64, 23))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 50, 121, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.verticalSlider, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.lcdNumber.display)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Cedula:", None))
        self.Enviar.setText(_translate("MainWindow", "Enviar", None))
        self.pushButton.setText(_translate("MainWindow", "Limpiar", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))

