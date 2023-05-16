# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crearUsuario.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class uiCrear(object):
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
        self.labelAtras.setPixmap(QtGui.QPixmap("imagenes/Logo Atras.png"))
        self.labelAtras.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAtras.setObjectName("labelAtras")
        self.labelNombre = QtWidgets.QLabel(self.frame)
        self.labelNombre.setGeometry(QtCore.QRect(61, 127, 174, 33))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.labelNombre.setFont(font)
        self.labelNombre.setStyleSheet("background-color: rgb(226, 226, 226);\n"
"border-radius: 16px;")
        self.labelNombre.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNombre.setObjectName("labelNombre")
        self.labelLogo = QtWidgets.QLabel(self.frame)
        self.labelLogo.setGeometry(QtCore.QRect(360, 130, 533, 503))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.labelLogo.setFont(font)
        self.labelLogo.setStyleSheet("")
        self.labelLogo.setText("")
        self.labelLogo.setPixmap(QtGui.QPixmap("imagenes/Icono Fondo.png"))
        self.labelLogo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLogo.setObjectName("labelLogo")
        self.inputNombre = QtWidgets.QLineEdit(self.frame)
        self.inputNombre.setGeometry(QtCore.QRect(254, 127, 646, 33))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(14)
        self.inputNombre.setFont(font)
        self.inputNombre.setStyleSheet("border: 2px solid #000000;\n"
"background-color: rgb(255, 255, 255);")
        self.inputNombre.setText("")
        self.inputNombre.setObjectName("inputNombre")
        self.labelApellidoP = QtWidgets.QLabel(self.frame)
        self.labelApellidoP.setGeometry(QtCore.QRect(61, 178, 174, 33))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.labelApellidoP.setFont(font)
        self.labelApellidoP.setStyleSheet("background-color: rgb(226, 226, 226);\n"
"border-radius: 16px;")
        self.labelApellidoP.setAlignment(QtCore.Qt.AlignCenter)
        self.labelApellidoP.setObjectName("labelApellidoP")
        self.inputApellidoP = QtWidgets.QLineEdit(self.frame)
        self.inputApellidoP.setGeometry(QtCore.QRect(254, 178, 646, 33))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(14)
        self.inputApellidoP.setFont(font)
        self.inputApellidoP.setStyleSheet("border: 2px solid #000000;\n"
"background-color: rgb(255, 255, 255);")
        self.inputApellidoP.setText("")
        self.inputApellidoP.setObjectName("inputApellidoP")
        self.labelApellidoM = QtWidgets.QLabel(self.frame)
        self.labelApellidoM.setGeometry(QtCore.QRect(61, 229, 174, 33))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.labelApellidoM.setFont(font)
        self.labelApellidoM.setStyleSheet("background-color: rgb(226, 226, 226);\n"
"border-radius: 16px;")
        self.labelApellidoM.setAlignment(QtCore.Qt.AlignCenter)
        self.labelApellidoM.setObjectName("labelApellidoM")
        self.labelFechaN = QtWidgets.QLabel(self.frame)
        self.labelFechaN.setGeometry(QtCore.QRect(61, 280, 174, 33))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.labelFechaN.setFont(font)
        self.labelFechaN.setStyleSheet("background-color: rgb(226, 226, 226);\n"
"border-radius: 16px;")
        self.labelFechaN.setAlignment(QtCore.Qt.AlignCenter)
        self.labelFechaN.setObjectName("labelFechaN")
        self.labelCorreo = QtWidgets.QLabel(self.frame)
        self.labelCorreo.setGeometry(QtCore.QRect(61, 331, 174, 33))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.labelCorreo.setFont(font)
        self.labelCorreo.setStyleSheet("background-color: rgb(226, 226, 226);\n"
"border-radius: 16px;")
        self.labelCorreo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCorreo.setObjectName("labelCorreo")
        self.labelCargo = QtWidgets.QLabel(self.frame)
        self.labelCargo.setGeometry(QtCore.QRect(61, 382, 174, 33))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.labelCargo.setFont(font)
        self.labelCargo.setStyleSheet("background-color: rgb(226, 226, 226);\n"
"border-radius: 16px;")
        self.labelCargo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCargo.setObjectName("labelCargo")
        self.labelGenero = QtWidgets.QLabel(self.frame)
        self.labelGenero.setGeometry(QtCore.QRect(61, 433, 174, 33))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.labelGenero.setFont(font)
        self.labelGenero.setStyleSheet("background-color: rgb(226, 226, 226);\n"
"border-radius: 16px;")
        self.labelGenero.setAlignment(QtCore.Qt.AlignCenter)
        self.labelGenero.setObjectName("labelGenero")
        self.labelRut = QtWidgets.QLabel(self.frame)
        self.labelRut.setGeometry(QtCore.QRect(61, 484, 174, 33))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.labelRut.setFont(font)
        self.labelRut.setStyleSheet("background-color: rgb(226, 226, 226);\n"
"border-radius: 16px;")
        self.labelRut.setAlignment(QtCore.Qt.AlignCenter)
        self.labelRut.setObjectName("labelRut")
        self.labelContra = QtWidgets.QLabel(self.frame)
        self.labelContra.setGeometry(QtCore.QRect(61, 535, 174, 33))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.labelContra.setFont(font)
        self.labelContra.setStyleSheet("background-color: rgb(226, 226, 226);\n"
"border-radius: 16px;")
        self.labelContra.setAlignment(QtCore.Qt.AlignCenter)
        self.labelContra.setObjectName("labelContra")
        self.inputApellidoM = QtWidgets.QLineEdit(self.frame)
        self.inputApellidoM.setGeometry(QtCore.QRect(254, 229, 646, 33))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(14)
        self.inputApellidoM.setFont(font)
        self.inputApellidoM.setStyleSheet("border: 2px solid #000000;\n"
"background-color: rgb(255, 255, 255);")
        self.inputApellidoM.setText("")
        self.inputApellidoM.setObjectName("inputApellidoM")
        self.inputCorreo = QtWidgets.QLineEdit(self.frame)
        self.inputCorreo.setGeometry(QtCore.QRect(254, 331, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(14)
        self.inputCorreo.setFont(font)
        self.inputCorreo.setStyleSheet("border: 2px solid #000000;\n"
"background-color: rgb(255, 255, 255);")
        self.inputCorreo.setText("")
        self.inputCorreo.setObjectName("inputCorreo")
        self.inputRut = QtWidgets.QLineEdit(self.frame)
        self.inputRut.setGeometry(QtCore.QRect(254, 484, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(14)
        self.inputRut.setFont(font)
        self.inputRut.setStyleSheet("border: 2px solid #000000;\n"
"background-color: rgb(255, 255, 255);")
        self.inputRut.setText("")
        self.inputRut.setMaxLength(8)
        self.inputRut.setObjectName("inputRut")
        self.inputPassword = QtWidgets.QLineEdit(self.frame)
        self.inputPassword.setGeometry(QtCore.QRect(254, 535, 601, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(14)
        self.inputPassword.setFont(font)
        self.inputPassword.setStyleSheet("border: 2px solid #000000;\n"
"background-color: rgb(255, 255, 255);")
        self.inputPassword.setText("")
        self.inputPassword.setMaxLength(30)
        self.inputPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputPassword.setObjectName("inputPassword")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(573, 331, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border: 2px solid #000000;\n"
"background-color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.inputDominio = QtWidgets.QLineEdit(self.frame)
        self.inputDominio.setGeometry(QtCore.QRect(611, 331, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(14)
        self.inputDominio.setFont(font)
        self.inputDominio.setStyleSheet("border: 2px solid #000000;\n"
"background-color: rgb(255, 255, 255);")
        self.inputDominio.setText("")
        self.inputDominio.setObjectName("inputDominio")
        self.dateNacimiento = QtWidgets.QDateEdit(self.frame)
        self.dateNacimiento.setGeometry(QtCore.QRect(254, 280, 141, 41))
        self.dateNacimiento.setStyleSheet("border: 2px solid #000000;\n"
"background-color: rgb(255, 255, 255);")
        self.dateNacimiento.setObjectName("dateNacimiento")
        self.comboBoxG = QtWidgets.QComboBox(self.frame)
        self.comboBoxG.setGeometry(QtCore.QRect(254, 433, 641, 31))
        self.comboBoxG.setStyleSheet("border: 2px solid #000000;\n"
"background-color: rgb(255, 255, 255);")
        self.comboBoxG.setObjectName("comboBoxG")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imagenes/Elegir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBoxG.addItem(icon, "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("imagenes/Masculino.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBoxG.addItem(icon1, "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("imagenes/Femenino.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBoxG.addItem(icon2, "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("imagenes/Otro.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBoxG.addItem(icon3, "")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(593, 484, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border: 2px solid #000000;\n"
"background-color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.inputDigito = QtWidgets.QLineEdit(self.frame)
        self.inputDigito.setGeometry(QtCore.QRect(632, 484, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(14)
        self.inputDigito.setFont(font)
        self.inputDigito.setStyleSheet("border: 2px solid #000000;\n"
"background-color: rgb(255, 255, 255);")
        self.inputDigito.setText("")
        self.inputDigito.setMaxLength(1)
        self.inputDigito.setObjectName("inputDigito")
        self.btnMostrar = QtWidgets.QPushButton(self.frame)
        self.btnMostrar.setGeometry(QtCore.QRect(855, 535, 51, 31))
        self.btnMostrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMostrar.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btnMostrar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btnMostrar.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("imagenes/Mostrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMostrar.setIcon(icon4)
        self.btnMostrar.setIconSize(QtCore.QSize(37, 33))
        self.btnMostrar.setObjectName("btnMostrar")
        self.btnOcultar = QtWidgets.QPushButton(self.frame)
        self.btnOcultar.setGeometry(QtCore.QRect(855, 535, 51, 31))
        self.btnOcultar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnOcultar.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btnOcultar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btnOcultar.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("imagenes/Esconder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOcultar.setIcon(icon5)
        self.btnOcultar.setIconSize(QtCore.QSize(37, 33))
        self.btnOcultar.setObjectName("btnOcultar")
        self.comboBoxC = QtWidgets.QComboBox(self.frame)
        self.comboBoxC.setGeometry(QtCore.QRect(254, 382, 641, 31))
        self.comboBoxC.setStyleSheet("border: 2px solid #000000;\n"
"background-color: rgb(255, 255, 255);")
        self.comboBoxC.setObjectName("comboBoxC")
        self.comboBoxC.addItem(icon, "")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("imagenes/Cajero.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBoxC.addItem(icon6, "")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("imagenes/Gerente.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBoxC.addItem(icon7, "")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("imagenes/Asistente.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBoxC.addItem(icon8, "")
        self.labelLogo.raise_()
        self.labelAtras.raise_()
        self.labelTitulo.raise_()
        self.btnAtras.raise_()
        self.labelNombre.raise_()
        self.inputNombre.raise_()
        self.labelApellidoP.raise_()
        self.inputApellidoP.raise_()
        self.labelApellidoM.raise_()
        self.labelFechaN.raise_()
        self.labelCorreo.raise_()
        self.labelCargo.raise_()
        self.labelGenero.raise_()
        self.labelRut.raise_()
        self.labelContra.raise_()
        self.inputApellidoM.raise_()
        self.inputCorreo.raise_()
        self.inputRut.raise_()
        self.inputPassword.raise_()
        self.label_2.raise_()
        self.inputDominio.raise_()
        self.dateNacimiento.raise_()
        self.comboBoxG.raise_()
        self.label_3.raise_()
        self.inputDigito.raise_()
        self.btnMostrar.raise_()
        self.btnOcultar.raise_()
        self.comboBoxC.raise_()
        self.btnRegistrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegistrar.setGeometry(QtCore.QRect(983, 620, 247, 48))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnRegistrar.setFont(font)
        self.btnRegistrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnRegistrar.setStyleSheet("border-color: rgb(0, 74, 173);")
        self.btnRegistrar.setObjectName("btnRegistrar")
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
        self.labelTitulo.setText(_translate("MainWindow", "CREAR USUARIO"))
        self.labelNombre.setText(_translate("MainWindow", "Nombre"))
        self.inputNombre.setPlaceholderText(_translate("MainWindow", "Nombre(s) del Usuario..."))
        self.labelApellidoP.setText(_translate("MainWindow", "Apellido Paterno"))
        self.inputApellidoP.setPlaceholderText(_translate("MainWindow", "Apellido Paterno del Usuario..."))
        self.labelApellidoM.setText(_translate("MainWindow", "Apellido Materno"))
        self.labelFechaN.setText(_translate("MainWindow", "Fecha Nacimiento"))
        self.labelCorreo.setText(_translate("MainWindow", "Correo Electronico"))
        self.labelCargo.setText(_translate("MainWindow", "Cargo"))
        self.labelGenero.setText(_translate("MainWindow", "Genero"))
        self.labelRut.setText(_translate("MainWindow", "Rut"))
        self.labelContra.setText(_translate("MainWindow", "Contraseña"))
        self.inputApellidoM.setPlaceholderText(_translate("MainWindow", "Apellido Materno del Usuario..."))
        self.inputCorreo.setPlaceholderText(_translate("MainWindow", "Correo del usuario..."))
        self.inputRut.setPlaceholderText(_translate("MainWindow", "Rut del Usuario sin puntos..."))
        self.inputPassword.setPlaceholderText(_translate("MainWindow", "Contraseña del usuario entre 2 a 30 caracteres..."))
        self.label_2.setText(_translate("MainWindow", "@"))
        self.inputDominio.setPlaceholderText(_translate("MainWindow", "Dominio correo, ej: gmail.com"))
        self.comboBoxG.setItemText(0, _translate("MainWindow", "Elegir"))
        self.comboBoxG.setItemText(1, _translate("MainWindow", "Masculino"))
        self.comboBoxG.setItemText(2, _translate("MainWindow", "Femenino"))
        self.comboBoxG.setItemText(3, _translate("MainWindow", "Otro"))
        self.label_3.setText(_translate("MainWindow", "-"))
        self.inputDigito.setPlaceholderText(_translate("MainWindow", "0-9 o K"))
        self.comboBoxC.setItemText(0, _translate("MainWindow", "Elegir"))
        self.comboBoxC.setItemText(1, _translate("MainWindow", "Cajero/a"))
        self.comboBoxC.setItemText(2, _translate("MainWindow", "Gerente"))
        self.comboBoxC.setItemText(3, _translate("MainWindow", "Asistente de Ventas"))
        self.btnRegistrar.setText(_translate("MainWindow", "Registrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = uiCrear()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())