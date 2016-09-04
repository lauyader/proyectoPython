#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4.QtGui import QApplication, QMainWindow

from prueba import Ui_MainWindow


if __name__ == "__main__":
    app = QApplication([])
    window = QMainWindow()
    main_window = Ui_MainWindow()
    main_window.setupUi(window)
    window.show()
    app.exec_()