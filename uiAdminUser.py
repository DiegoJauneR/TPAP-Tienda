# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'administracionUsuario.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class admin(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 720))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1291, 701))
        self.frame.setMinimumSize(QtCore.QSize(1291, 701))
        self.frame.setMaximumSize(QtCore.QSize(1291, 701))
        self.frame.setStyleSheet("background-color: rgb(38, 87, 165);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.labelTitulo = QtWidgets.QLabel(self.frame)
        self.labelTitulo.setGeometry(QtCore.QRect(376, 45, 528, 55))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setStyleSheet("background-color: rgb(226, 226, 226);\n"
"border-radius: 27px;")
        self.labelTitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitulo.setObjectName("labelTitulo")
        self.btnCrearUsuario = QtWidgets.QPushButton(self.frame)
        self.btnCrearUsuario.setGeometry(QtCore.QRect(52, 610, 205, 55))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnCrearUsuario.setFont(font)
        self.btnCrearUsuario.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCrearUsuario.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"border-radius: 27px")
        self.btnCrearUsuario.setObjectName("btnCrearUsuario")
        self.btnVerUsuario = QtWidgets.QPushButton(self.frame)
        self.btnVerUsuario.setGeometry(QtCore.QRect(361, 610, 205, 55))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnVerUsuario.setFont(font)
        self.btnVerUsuario.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnVerUsuario.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"border-radius: 27px")
        self.btnVerUsuario.setObjectName("btnVerUsuario")
        self.btnModificar = QtWidgets.QPushButton(self.frame)
        self.btnModificar.setGeometry(QtCore.QRect(670, 610, 205, 55))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnModificar.setFont(font)
        self.btnModificar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnModificar.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"border-radius: 27px")
        self.btnModificar.setObjectName("btnModificar")
        self.btnEliminar = QtWidgets.QPushButton(self.frame)
        self.btnEliminar.setGeometry(QtCore.QRect(979, 610, 205, 55))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnEliminar.setFont(font)
        self.btnEliminar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnEliminar.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"border-radius: 27px")
        self.btnEliminar.setObjectName("btnEliminar")
        self.listaUsuario = QtWidgets.QTableWidget(self.frame)
        self.listaUsuario.setGeometry(QtCore.QRect(37, 115, 1170, 485))
        self.listaUsuario.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listaUsuario.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.listaUsuario.setAutoScrollMargin(16)
        self.listaUsuario.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listaUsuario.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listaUsuario.setShowGrid(True)
        self.listaUsuario.setGridStyle(QtCore.Qt.SolidLine)
        self.listaUsuario.setWordWrap(True)
        self.listaUsuario.setCornerButtonEnabled(True)
        self.listaUsuario.setRowCount(0)
        self.listaUsuario.setObjectName("listaUsuario")
        self.listaUsuario.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.listaUsuario.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.listaUsuario.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.listaUsuario.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.listaUsuario.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.listaUsuario.setHorizontalHeaderItem(4, item)
        self.listaUsuario.horizontalHeader().setCascadingSectionResizes(False)
        self.listaUsuario.horizontalHeader().setDefaultSectionSize(233)
        self.listaUsuario.horizontalHeader().setSortIndicatorShown(False)
        self.listaUsuario.horizontalHeader().setStretchLastSection(False)
        self.listaUsuario.verticalHeader().setVisible(False)
        self.listaUsuario.verticalHeader().setCascadingSectionResizes(False)
        self.listaUsuario.verticalHeader().setHighlightSections(True)
        self.listaUsuario.verticalHeader().setStretchLastSection(False)
        self.labelAtras = QtWidgets.QLabel(self.centralwidget)
        self.labelAtras.setGeometry(QtCore.QRect(30, 24, 66, 49))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.labelAtras.setFont(font)
        self.labelAtras.setStyleSheet("")
        self.labelAtras.setText("")
        self.labelAtras.setPixmap(QtGui.QPixmap("imagenes/Logo Atras.png"))
        self.labelAtras.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAtras.setObjectName("labelAtras")
        self.btnAtras = QtWidgets.QPushButton(self.centralwidget)
        self.btnAtras.setGeometry(QtCore.QRect(30, 24, 66, 49))
        self.btnAtras.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAtras.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btnAtras.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.btnAtras.setText("")
        self.btnAtras.setObjectName("btnAtras")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelTitulo.setText(_translate("MainWindow", "ADMINISTRACION USUARIOS"))
        self.btnCrearUsuario.setText(_translate("MainWindow", "Crear Usuario"))
        self.btnVerUsuario.setText(_translate("MainWindow", "Ver Usuario"))
        self.btnModificar.setText(_translate("MainWindow", "Modificar Usuario"))
        self.btnEliminar.setText(_translate("MainWindow", "Eliminar Usuario"))
        self.listaUsuario.setSortingEnabled(False)
        item = self.listaUsuario.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.listaUsuario.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Rut"))
        item = self.listaUsuario.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nombres"))
        item = self.listaUsuario.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Apellidos"))
        item = self.listaUsuario.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Cargo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = admin()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())