# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_FormAdiarConsulta(object):
    def setupUi(self, FormAdiarConsulta):
        FormAdiarConsulta.setObjectName("FormAdiarConsulta")
        FormAdiarConsulta.resize(393, 278)
        FormAdiarConsulta.setWindowIcon(QtGui.QIcon(os.path.join(os.path.dirname(__file__), "imagens", "logo.png")))
        FormAdiarConsulta.setStyleSheet("""
/* === OmniCare Hospital Theme === */
QWidget {
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

QLineEdit {
    background-color: white;
    color: #2C3E50;
    border: 2px solid #B8D4E3;
    border-radius: 8px;
    padding: 3px 8px;
    min-height: 26px;
}

QDateTimeEdit {
    background-color: white;
    color: #2C3E50;
    border: 2px solid #B8D4E3;
    border-radius: 8px;
    padding: 1px 8px;
    min-height: 30px;
}

QLineEdit:focus, QDateTimeEdit:focus {
    border: 2px solid #14919B;
}
""")
        
        self.centralwidget = QtWidgets.QWidget(FormAdiarConsulta)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label_Titulo = QtWidgets.QLabel(self.centralwidget)
        self.label_Titulo.setGeometry(QtCore.QRect(30, 10, 300, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        self.label_Titulo.setFont(font)
        self.label_Titulo.setObjectName("label_Titulo")
        
        self.label_IdConsulta = QtWidgets.QLabel(self.centralwidget)
        self.label_IdConsulta.setGeometry(QtCore.QRect(30, 50, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_IdConsulta.setFont(font)
        self.label_IdConsulta.setObjectName("label_IdConsulta")
        
        self.lineEdit_IdConsulta = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_IdConsulta.setGeometry(QtCore.QRect(160, 48, 100, 28))
        self.lineEdit_IdConsulta.setReadOnly(True)
        self.lineEdit_IdConsulta.setObjectName("lineEdit_IdConsulta")
        
        self.label_DataAtual = QtWidgets.QLabel(self.centralwidget)
        self.label_DataAtual.setGeometry(QtCore.QRect(30, 90, 100, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_DataAtual.setFont(font)
        self.label_DataAtual.setObjectName("label_DataAtual")
        
        self.dateTimeEdit_DataAtual = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit_DataAtual.setGeometry(QtCore.QRect(30, 110, 194, 32))
        self.dateTimeEdit_DataAtual.setReadOnly(True)
        self.dateTimeEdit_DataAtual.setObjectName("dateTimeEdit_DataAtual")
        
        self.label_DataAdiada = QtWidgets.QLabel(self.centralwidget)
        self.label_DataAdiada.setGeometry(QtCore.QRect(30, 150, 100, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_DataAdiada.setFont(font)
        self.label_DataAdiada.setObjectName("label_DataAdiada")
        
        self.dateTimeEdit_DataAdiada = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit_DataAdiada.setGeometry(QtCore.QRect(30, 170, 194, 32))
        self.dateTimeEdit_DataAdiada.setObjectName("dateTimeEdit_DataAdiada")
        
        self.pushButton_Aplicar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Aplicar.setGeometry(QtCore.QRect(288, 230, 87, 32))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton_Aplicar.setFont(font)
        self.pushButton_Aplicar.setObjectName("pushButton_Aplicar")
        
        self.pushButton_Cancelar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Cancelar.setGeometry(QtCore.QRect(190, 230, 92, 32))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton_Cancelar.setFont(font)
        self.pushButton_Cancelar.setObjectName("pushButton_Cancelar")
        
        FormAdiarConsulta.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(FormAdiarConsulta)
        QtCore.QMetaObject.connectSlotsByName(FormAdiarConsulta)

    def retranslateUi(self, FormAdiarConsulta):
        _translate = QtCore.QCoreApplication.translate
        FormAdiarConsulta.setWindowTitle(_translate("FormAdiarConsulta", "OmniCare - Adiar Consulta"))
        self.label_Titulo.setText(_translate("FormAdiarConsulta", "Adiar Consulta"))
        self.label_IdConsulta.setText(_translate("FormAdiarConsulta", "Id da Consulta:"))
        self.label_DataAtual.setText(_translate("FormAdiarConsulta", "Data Atual:"))
        self.label_DataAdiada.setText(_translate("FormAdiarConsulta", "Adiar Para:"))
        self.pushButton_Aplicar.setText(_translate("FormAdiarConsulta", "Aplicar"))
        self.pushButton_Cancelar.setText(_translate("FormAdiarConsulta", "Cancelar"))
