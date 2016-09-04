# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'led13.ui'
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
        MainWindow.setEnabled(True)
        MainWindow.resize(692, 553)
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setStyleSheet(_fromUtf8("QMainWindow{\n"
" \n"
"    background-image: url(:/newPrefix/imagen/robot.png);\n"
"    \n"
"background-color:  rgb(0, 85, 127);\n"
"}  \n"
"\n"
"\n"
"/*Estilos para el botón*/\n"
"    QPushButton{\n"
"        background-color: #ff5722;\n"
"        border-radius: 4px;\n"
"        color: #fff;\n"
"        font-family: \'Roboto\';\n"
"        font-size: 12px;\n"
"    }\n"
"\n"
"\n"
"estadoled{\n"
"     \n"
" \n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Titulo = QtGui.QLabel(self.centralwidget)
        self.Titulo.setGeometry(QtCore.QRect(80, 30, 491, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Titulo.setFont(font)
        self.Titulo.setObjectName(_fromUtf8("Titulo"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(520, 160, 111, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.estadoLed = QtGui.QLineEdit(self.centralwidget)
        self.estadoLed.setEnabled(False)
        self.estadoLed.setGeometry(QtCore.QRect(470, 190, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.estadoLed.setFont(font)
        self.estadoLed.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.estadoLed.setAlignment(QtCore.Qt.AlignCenter)
        self.estadoLed.setObjectName(_fromUtf8("estadoLed"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 480, 271, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.cArduino = QtGui.QLineEdit(self.centralwidget)
        self.cArduino.setGeometry(QtCore.QRect(300, 390, 211, 26))
        self.cArduino.setAlignment(QtCore.Qt.AlignCenter)
        self.cArduino.setObjectName(_fromUtf8("cArduino"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 390, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(20, 190, 177, 27))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.btn_onLed = QtGui.QPushButton(self.splitter)
        self.btn_onLed.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_onLed.setObjectName(_fromUtf8("btn_onLed"))
        self.btn_offLed = QtGui.QPushButton(self.splitter)
        self.btn_offLed.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_offLed.setObjectName(_fromUtf8("btn_offLed"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 692, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        self.menuLed13 = QtGui.QMenu(self.menuMenu)
        self.menuLed13.setObjectName(_fromUtf8("menuLed13"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionApagar = QtGui.QAction(MainWindow)
        self.actionApagar.setObjectName(_fromUtf8("actionApagar"))
        self.actionEncender = QtGui.QAction(MainWindow)
        self.actionEncender.setObjectName(_fromUtf8("actionEncender"))
        self.menuLed13.addAction(self.actionApagar)
        self.menuLed13.addAction(self.actionEncender)
        self.menuLed13.addSeparator()
        self.menuMenu.addAction(self.menuLed13.menuAction())
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Control Led 13", None))
        self.Titulo.setText(_translate("MainWindow", "Sistema de Control led para Arduino", None))
        self.label.setText(_translate("MainWindow", "Estado del Led 13", None))
        self.estadoLed.setText(_translate("MainWindow", "NEUTRO", None))
        self.label_2.setText(_translate("MainWindow", "Realizado por : Luis Americo Auyadermont", None))
        self.cArduino.setText(_translate("MainWindow", "¡En espera!", None))
        self.label_3.setText(_translate("MainWindow", "Arduino está:", None))
        self.btn_onLed.setText(_translate("MainWindow", "ON Led  13", None))
        self.btn_offLed.setText(_translate("MainWindow", "OFF Led  13", None))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu", None))
        self.menuLed13.setTitle(_translate("MainWindow", "Led13", None))
        self.actionApagar.setText(_translate("MainWindow", "Apagar", None))
        self.actionEncender.setText(_translate("MainWindow", "Encender", None))

import imagenes_rc
