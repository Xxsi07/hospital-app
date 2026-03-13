# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_Dialog_NovaConsulta(object):
    def setupUi(self, Dialog_NovaConsulta):
        Dialog_NovaConsulta.setObjectName("Dialog_NovaConsulta")
        Dialog_NovaConsulta.resize(400, 350)
        Dialog_NovaConsulta.setWindowIcon(QtGui.QIcon(os.path.join(os.path.dirname(__file__), "imagens", "logo.png")))
        Dialog_NovaConsulta.setStyleSheet("""
/* === OmniCare Hospital Theme === */
QDialog {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #E8F4F8, stop:1 #F0F8FF);
    font-family: 'Segoe UI', Arial;
}

QPushButton {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #0D7377, stop:1 #14919B);
    color: white;
    border-radius: 12px;
    border: none;
    padding: 8px 16px;
    font-weight: bold;
}

QPushButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #14919B, stop:1 #0D7377);
}

QLabel {
    color: #0D7377;
    background: transparent;
}

QComboBox, QDateEdit, QTimeEdit, QTextEdit {
    background-color: white;
    color: #2C3E50;
    border: 2px solid #B8D4E3;
    border-radius: 8px;
    padding: 5px;
}

QComboBox:focus, QDateEdit:focus, QTimeEdit:focus, QTextEdit:focus {
    border: 2px solid #14919B;
}
""")
        
        self.label_Titulo = QtWidgets.QLabel(Dialog_NovaConsulta)
        self.label_Titulo.setGeometry(QtCore.QRect(20, 10, 360, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_Titulo.setFont(font)
        self.label_Titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Titulo.setObjectName("label_Titulo")
        
        self.label_Utente = QtWidgets.QLabel(Dialog_NovaConsulta)
        self.label_Utente.setGeometry(QtCore.QRect(20, 60, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Utente.setFont(font)
        self.label_Utente.setObjectName("label_Utente")
        
        self.comboBox_Utente = QtWidgets.QComboBox(Dialog_NovaConsulta)
        self.comboBox_Utente.setGeometry(QtCore.QRect(130, 55, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.comboBox_Utente.setFont(font)
        self.comboBox_Utente.setObjectName("comboBox_Utente")
        
        self.label_Data = QtWidgets.QLabel(Dialog_NovaConsulta)
        self.label_Data.setGeometry(QtCore.QRect(20, 100, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Data.setFont(font)
        self.label_Data.setObjectName("label_Data")
        
        self.dateEdit_Data = QtWidgets.QDateEdit(Dialog_NovaConsulta)
        self.dateEdit_Data.setGeometry(QtCore.QRect(130, 95, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.dateEdit_Data.setFont(font)
        self.dateEdit_Data.setCalendarPopup(True)
        self.dateEdit_Data.setObjectName("dateEdit_Data")
        
        self.label_Hora = QtWidgets.QLabel(Dialog_NovaConsulta)
        self.label_Hora.setGeometry(QtCore.QRect(270, 100, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Hora.setFont(font)
        self.label_Hora.setObjectName("label_Hora")
        
        self.timeEdit_Hora = QtWidgets.QTimeEdit(Dialog_NovaConsulta)
        self.timeEdit_Hora.setGeometry(QtCore.QRect(320, 95, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.timeEdit_Hora.setFont(font)
        self.timeEdit_Hora.setObjectName("timeEdit_Hora")
        
        self.label_TipoConsulta = QtWidgets.QLabel(Dialog_NovaConsulta)
        self.label_TipoConsulta.setGeometry(QtCore.QRect(20, 140, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_TipoConsulta.setFont(font)
        self.label_TipoConsulta.setObjectName("label_TipoConsulta")
        
        self.comboBox_TipoConsulta = QtWidgets.QComboBox(Dialog_NovaConsulta)
        self.comboBox_TipoConsulta.setGeometry(QtCore.QRect(130, 135, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.comboBox_TipoConsulta.setFont(font)
        self.comboBox_TipoConsulta.setObjectName("comboBox_TipoConsulta")
        
        self.label_Observacoes = QtWidgets.QLabel(Dialog_NovaConsulta)
        self.label_Observacoes.setGeometry(QtCore.QRect(20, 180, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Observacoes.setFont(font)
        self.label_Observacoes.setObjectName("label_Observacoes")
        
        self.textEdit_Observacoes = QtWidgets.QTextEdit(Dialog_NovaConsulta)
        self.textEdit_Observacoes.setGeometry(QtCore.QRect(20, 205, 360, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_Observacoes.setFont(font)
        self.textEdit_Observacoes.setObjectName("textEdit_Observacoes")
        
        self.pushButton_Guardar = QtWidgets.QPushButton(Dialog_NovaConsulta)
        self.pushButton_Guardar.setGeometry(QtCore.QRect(80, 300, 100, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Guardar.setFont(font)
        self.pushButton_Guardar.setObjectName("pushButton_Guardar")
        
        self.pushButton_Cancelar = QtWidgets.QPushButton(Dialog_NovaConsulta)
        self.pushButton_Cancelar.setGeometry(QtCore.QRect(220, 300, 100, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Cancelar.setFont(font)
        self.pushButton_Cancelar.setObjectName("pushButton_Cancelar")

        self.retranslateUi(Dialog_NovaConsulta)
        QtCore.QMetaObject.connectSlotsByName(Dialog_NovaConsulta)

    def retranslateUi(self, Dialog_NovaConsulta):
        _translate = QtCore.QCoreApplication.translate
        Dialog_NovaConsulta.setWindowTitle(_translate("Dialog_NovaConsulta", "OmniCare - Nova Consulta"))
        self.label_Titulo.setText(_translate("Dialog_NovaConsulta", "Marcar Nova Consulta"))
        self.label_Utente.setText(_translate("Dialog_NovaConsulta", "Utente:"))
        self.label_Data.setText(_translate("Dialog_NovaConsulta", "Data:"))
        self.label_Hora.setText(_translate("Dialog_NovaConsulta", "Hora:"))
        self.label_TipoConsulta.setText(_translate("Dialog_NovaConsulta", "Tipo:"))
        self.label_Observacoes.setText(_translate("Dialog_NovaConsulta", "Observações:"))
        self.pushButton_Guardar.setText(_translate("Dialog_NovaConsulta", "Guardar"))
        self.pushButton_Cancelar.setText(_translate("Dialog_NovaConsulta", "Cancelar"))
