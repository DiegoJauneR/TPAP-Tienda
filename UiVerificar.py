# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'verificarStock.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
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
        self.labelTitulo.setGeometry(QtCore.QRect(362, 45, 528, 55))
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
        self.btnAtras = QtWidgets.QPushButton(self.frame)
        self.btnAtras.setGeometry(QtCore.QRect(30, 24, 66, 49))
        self.btnAtras.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAtras.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btnAtras.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.btnAtras.setText("")
        self.btnAtras.setObjectName("btnAtras")
        self.labelAtras = QtWidgets.QLabel(self.frame)
        self.labelAtras.setGeometry(QtCore.QRect(30, 24, 66, 49))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.labelAtras.setFont(font)
        self.labelAtras.setStyleSheet("")
        self.labelAtras.setText("")
        self.labelAtras.setPixmap(QtGui.QPixmap("../imagenes/Logo Atras.png"))
        self.labelAtras.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAtras.setObjectName("labelAtras")
        self.labelid2 = QtWidgets.QLabel(self.frame)
        self.labelid2.setGeometry(QtCore.QRect(61, 127, 174, 33))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.labelid2.setFont(font)
        self.labelid2.setStyleSheet("background-color: rgb(226, 226, 226);\n"
"border-radius: 16px;")
        self.labelid2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelid2.setObjectName("labelid2")
        self.labelFondo = QtWidgets.QLabel(self.frame)
        self.labelFondo.setGeometry(QtCore.QRect(360, 130, 533, 503))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.labelFondo.setFont(font)
        self.labelFondo.setStyleSheet("")
        self.labelFondo.setText("")
        self.labelFondo.setPixmap(QtGui.QPixmap("../imagenes/Icono Fondo.png"))
        self.labelFondo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelFondo.setObjectName("labelFondo")
        self.labelNombre2_2 = QtWidgets.QLabel(self.frame)
        self.labelNombre2_2.setGeometry(QtCore.QRect(61, 178, 174, 33))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.labelNombre2_2.setFont(font)
        self.labelNombre2_2.setStyleSheet("background-color: rgb(226, 226, 226);\n"
"border-radius: 16px;")
        self.labelNombre2_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNombre2_2.setObjectName("labelNombre2_2")
        self.labelMascota2_2 = QtWidgets.QLabel(self.frame)
        self.labelMascota2_2.setGeometry(QtCore.QRect(61, 229, 174, 33))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.labelMascota2_2.setFont(font)
        self.labelMascota2_2.setStyleSheet("background-color: rgb(226, 226, 226);\n"
"border-radius: 16px;")
        self.labelMascota2_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMascota2_2.setObjectName("labelMascota2_2")
        self.labelMarca2_2 = QtWidgets.QLabel(self.frame)
        self.labelMarca2_2.setGeometry(QtCore.QRect(61, 280, 174, 33))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.labelMarca2_2.setFont(font)
        self.labelMarca2_2.setStyleSheet("background-color: rgb(226, 226, 226);\n"
"border-radius: 16px;")
        self.labelMarca2_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMarca2_2.setObjectName("labelMarca2_2")
        self.labelCategoria2 = QtWidgets.QLabel(self.frame)
        self.labelCategoria2.setGeometry(QtCore.QRect(61, 331, 174, 33))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.labelCategoria2.setFont(font)
        self.labelCategoria2.setStyleSheet("background-color: rgb(226, 226, 226);\n"
"border-radius: 16px;")
        self.labelCategoria2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCategoria2.setObjectName("labelCategoria2")
        self.labelPrecio2 = QtWidgets.QLabel(self.frame)
        self.labelPrecio2.setGeometry(QtCore.QRect(61, 382, 174, 33))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.labelPrecio2.setFont(font)
        self.labelPrecio2.setStyleSheet("background-color: rgb(226, 226, 226);\n"
"border-radius: 16px;")
        self.labelPrecio2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPrecio2.setObjectName("labelPrecio2")
        self.labelPrecioLote2 = QtWidgets.QLabel(self.frame)
        self.labelPrecioLote2.setGeometry(QtCore.QRect(61, 433, 174, 33))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.labelPrecioLote2.setFont(font)
        self.labelPrecioLote2.setStyleSheet("background-color: rgb(226, 226, 226);\n"
"border-radius: 16px;")
        self.labelPrecioLote2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPrecioLote2.setObjectName("labelPrecioLote2")
        self.labelStock = QtWidgets.QLabel(self.frame)
        self.labelStock.setGeometry(QtCore.QRect(61, 484, 174, 33))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.labelStock.setFont(font)
        self.labelStock.setStyleSheet("background-color: rgb(226, 226, 226);\n"
"border-radius: 16px;")
        self.labelStock.setAlignment(QtCore.Qt.AlignCenter)
        self.labelStock.setObjectName("labelStock")
        self.labelMarca = QtWidgets.QLabel(self.frame)
        self.labelMarca.setGeometry(QtCore.QRect(254, 280, 646, 34))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.labelMarca.setFont(font)
        self.labelMarca.setStyleSheet("background-color: rgb(193, 193, 193);")
        self.labelMarca.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMarca.setObjectName("labelMarca")
        self.labelid = QtWidgets.QLabel(self.frame)
        self.labelid.setGeometry(QtCore.QRect(254, 127, 646, 34))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.labelid.setFont(font)
        self.labelid.setStyleSheet("background-color: rgb(193, 193, 193);")
        self.labelid.setAlignment(QtCore.Qt.AlignCenter)
        self.labelid.setObjectName("labelid")
        self.labelCategoria = QtWidgets.QLabel(self.frame)
        self.labelCategoria.setGeometry(QtCore.QRect(254, 331, 646, 34))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.labelCategoria.setFont(font)
        self.labelCategoria.setStyleSheet("background-color: rgb(193, 193, 193);")
        self.labelCategoria.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCategoria.setObjectName("labelCategoria")
        self.labelPrecio = QtWidgets.QLabel(self.frame)
        self.labelPrecio.setGeometry(QtCore.QRect(254, 382, 331, 34))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.labelPrecio.setFont(font)
        self.labelPrecio.setStyleSheet("background-color: rgb(193, 193, 193);")
        self.labelPrecio.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPrecio.setObjectName("labelPrecio")
        self.labelStockEditable = QtWidgets.QLabel(self.frame)
        self.labelStockEditable.setGeometry(QtCore.QRect(254, 484, 331, 34))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.labelStockEditable.setFont(font)
        self.labelStockEditable.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.labelStockEditable.setStyleSheet("background-color: rgb(193, 193, 193);")
        self.labelStockEditable.setAlignment(QtCore.Qt.AlignCenter)
        self.labelStockEditable.setObjectName("labelStockEditable")
        self.inputStock = QtWidgets.QLineEdit(self.frame)
        self.inputStock.setGeometry(QtCore.QRect(254, 484, 331, 34))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.inputStock.setFont(font)
        self.inputStock.setStyleSheet("background-color: rgb(193, 193, 193);\n"
"border: 2px solid #c1c1c1")
        self.inputStock.setMaxLength(999)
        self.inputStock.setAlignment(QtCore.Qt.AlignCenter)
        self.inputStock.setObjectName("inputStock")
        self.labelFondo.raise_()
        self.labelAtras.raise_()
        self.labelTitulo.raise_()
        self.btnAtras.raise_()
        self.labelid2.raise_()
        self.labelNombre2_2.raise_()
        self.labelMascota2_2.raise_()
        self.labelMarca2_2.raise_()
        self.labelCategoria2.raise_()
        self.labelPrecio2.raise_()
        self.labelPrecioLote2.raise_()
        self.labelStock.raise_()
        self.labelMarca.raise_()
        self.labelid.raise_()
        self.labelCategoria.raise_()
        self.labelPrecio.raise_()
        self.labelStockEditable.raise_()
        self.inputStock.raise_()
        self.botonGuardar = QtWidgets.QPushButton(self.centralwidget)
        self.botonGuardar.setGeometry(QtCore.QRect(983, 620, 247, 48))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.botonGuardar.setFont(font)
        self.botonGuardar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botonGuardar.setStyleSheet("border-color: rgb(0, 74, 173);")
        self.botonGuardar.setObjectName("botonGuardar")
        self.labelNombre = QtWidgets.QLabel(self.centralwidget)
        self.labelNombre.setGeometry(QtCore.QRect(254, 178, 646, 34))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.labelNombre.setFont(font)
        self.labelNombre.setStyleSheet("background-color: rgb(193, 193, 193);")
        self.labelNombre.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNombre.setObjectName("labelNombre")
        self.labelMascota = QtWidgets.QLabel(self.centralwidget)
        self.labelMascota.setGeometry(QtCore.QRect(254, 229, 646, 34))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.labelMascota.setFont(font)
        self.labelMascota.setStyleSheet("background-color: rgb(193, 193, 193);")
        self.labelMascota.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMascota.setObjectName("labelMascota")
        self.labelPrecioLote = QtWidgets.QLabel(self.centralwidget)
        self.labelPrecioLote.setGeometry(QtCore.QRect(254, 433, 331, 34))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.labelPrecioLote.setFont(font)
        self.labelPrecioLote.setStyleSheet("background-color: rgb(193, 193, 193);")
        self.labelPrecioLote.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPrecioLote.setObjectName("labelPrecioLote")
        self.botonAgregar = QtWidgets.QPushButton(self.centralwidget)
        self.botonAgregar.setGeometry(QtCore.QRect(700, 620, 247, 48))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.botonAgregar.setFont(font)
        self.botonAgregar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botonAgregar.setStyleSheet("border-color: rgb(0, 74, 173);")
        self.botonAgregar.setObjectName("botonAgregar")
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
        self.labelTitulo.setText(_translate("MainWindow", "VERIFICAR STOCK"))
        self.labelid2.setText(_translate("MainWindow", "ID"))
        self.labelNombre2_2.setText(_translate("MainWindow", "Nombre"))
        self.labelMascota2_2.setText(_translate("MainWindow", "Mascota"))
        self.labelMarca2_2.setText(_translate("MainWindow", "Marca"))
        self.labelCategoria2.setText(_translate("MainWindow", "Categoria"))
        self.labelPrecio2.setText(_translate("MainWindow", "Precio"))
        self.labelPrecioLote2.setText(_translate("MainWindow", "Precio Lote"))
        self.labelStock.setText(_translate("MainWindow", "Stock"))
        self.labelMarca.setText(_translate("MainWindow", "Marca"))
        self.labelid.setText(_translate("MainWindow", "ID"))
        self.labelCategoria.setText(_translate("MainWindow", "Categoria"))
        self.labelPrecio.setText(_translate("MainWindow", "Precio"))
        self.labelStockEditable.setText(_translate("MainWindow", "Stock"))
        self.inputStock.setPlaceholderText(_translate("MainWindow", "Stock"))
        self.botonGuardar.setText(_translate("MainWindow", "Guardar"))
        self.labelNombre.setText(_translate("MainWindow", "Nombre"))
        self.labelMascota.setText(_translate("MainWindow", "Mascota"))
        self.labelPrecioLote.setText(_translate("MainWindow", "Precio por Lote"))
        self.botonAgregar.setText(_translate("MainWindow", "Agregar Stock"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())