# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_Form_DetalheUtilizador(object):
    def setupUi(self, Form_DetalheUtilizador):
        Form_DetalheUtilizador.setObjectName("Form_DetalheUtilizador")
        Form_DetalheUtilizador.resize(450, 400)
        Form_DetalheUtilizador.setWindowIcon(QtGui.QIcon(os.path.join(os.path.dirname(__file__), "imagens", "logo.png")))
        Form_DetalheUtilizador.setStyleSheet("""
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

QLineEdit:focus {
    border: 2px solid #14919B;
}

QComboBox {
    background-color: white;
    color: #2C3E50;
    border: 2px solid #B8D4E3;
    border-radius: 8px;
    padding: 2px 8px;
    min-height: 26px;
}

QComboBox:focus {
    border: 2px solid #14919B;
}
""")
        
        self.centralwidget = QtWidgets.QWidget(Form_DetalheUtilizador)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label_Titulo = QtWidgets.QLabel(self.centralwidget)
        self.label_Titulo.setGeometry(QtCore.QRect(20, 10, 300, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_Titulo.setFont(font)
        self.label_Titulo.setObjectName("label_Titulo")
        
        # ID
        self.label_Id = QtWidgets.QLabel(self.centralwidget)
        self.label_Id.setGeometry(QtCore.QRect(20, 60, 100, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_Id.setFont(font)
        self.label_Id.setObjectName("label_Id")
        
        self.lineEdit_Id = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Id.setGeometry(QtCore.QRect(130, 60, 100, 30))
        self.lineEdit_Id.setReadOnly(True)
        self.lineEdit_Id.setObjectName("lineEdit_Id")
        
        # Username
        self.label_Username = QtWidgets.QLabel(self.centralwidget)
        self.label_Username.setGeometry(QtCore.QRect(20, 100, 100, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_Username.setFont(font)
        self.label_Username.setObjectName("label_Username")
        
        self.lineEdit_Username = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Username.setGeometry(QtCore.QRect(130, 100, 290, 30))
        self.lineEdit_Username.setObjectName("lineEdit_Username")
        
        # Password
        self.label_Password = QtWidgets.QLabel(self.centralwidget)
        self.label_Password.setGeometry(QtCore.QRect(20, 140, 100, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_Password.setFont(font)
        self.label_Password.setObjectName("label_Password")
        
        self.lineEdit_Password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Password.setGeometry(QtCore.QRect(130, 140, 290, 30))
        self.lineEdit_Password.setObjectName("lineEdit_Password")
        
        # Nome
        self.label_Nome = QtWidgets.QLabel(self.centralwidget)
        self.label_Nome.setGeometry(QtCore.QRect(20, 180, 100, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_Nome.setFont(font)
        self.label_Nome.setObjectName("label_Nome")
        
        self.lineEdit_Nome = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Nome.setGeometry(QtCore.QRect(130, 180, 290, 30))
        self.lineEdit_Nome.setObjectName("lineEdit_Nome")
        
        # Email
        self.label_Email = QtWidgets.QLabel(self.centralwidget)
        self.label_Email.setGeometry(QtCore.QRect(20, 220, 100, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_Email.setFont(font)
        self.label_Email.setObjectName("label_Email")
        
        self.lineEdit_Email = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Email.setGeometry(QtCore.QRect(130, 220, 290, 30))
        self.lineEdit_Email.setObjectName("lineEdit_Email")
        
        # Telefone
        self.label_Telefone = QtWidgets.QLabel(self.centralwidget)
        self.label_Telefone.setGeometry(QtCore.QRect(20, 260, 100, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_Telefone.setFont(font)
        self.label_Telefone.setObjectName("label_Telefone")
        
        self.lineEdit_Telefone = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Telefone.setGeometry(QtCore.QRect(130, 260, 290, 30))
        self.lineEdit_Telefone.setObjectName("lineEdit_Telefone")
        
        # Cargo
        self.label_Cargo = QtWidgets.QLabel(self.centralwidget)
        self.label_Cargo.setGeometry(QtCore.QRect(20, 300, 100, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_Cargo.setFont(font)
        self.label_Cargo.setObjectName("label_Cargo")
        
        self.comboBox_Cargo = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Cargo.setGeometry(QtCore.QRect(130, 300, 200, 30))
        self.comboBox_Cargo.setObjectName("comboBox_Cargo")
        
        # Botões
        self.pushButton_Gravar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Gravar.setGeometry(QtCore.QRect(200, 350, 100, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Gravar.setFont(font)
        self.pushButton_Gravar.setObjectName("pushButton_Gravar")
        
        self.pushButton_Voltar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Voltar.setGeometry(QtCore.QRect(320, 350, 100, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Voltar.setFont(font)
        self.pushButton_Voltar.setObjectName("pushButton_Voltar")
        
        Form_DetalheUtilizador.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(Form_DetalheUtilizador)
        QtCore.QMetaObject.connectSlotsByName(Form_DetalheUtilizador)

    def retranslateUi(self, Form_DetalheUtilizador):
        _translate = QtCore.QCoreApplication.translate
        Form_DetalheUtilizador.setWindowTitle(_translate("Form_DetalheUtilizador", "OmniCare - Utilizador"))
        self.label_Titulo.setText(_translate("Form_DetalheUtilizador", "Detalhes do Utilizador"))
        self.label_Id.setText(_translate("Form_DetalheUtilizador", "ID:"))
        self.label_Username.setText(_translate("Form_DetalheUtilizador", "Username:"))
        self.label_Password.setText(_translate("Form_DetalheUtilizador", "Password:"))
        self.label_Nome.setText(_translate("Form_DetalheUtilizador", "Nome:"))
        self.label_Email.setText(_translate("Form_DetalheUtilizador", "Email:"))
        self.label_Telefone.setText(_translate("Form_DetalheUtilizador", "Telefone:"))
        self.label_Cargo.setText(_translate("Form_DetalheUtilizador", "Cargo:"))
        self.pushButton_Gravar.setText(_translate("Form_DetalheUtilizador", "Gravar"))
        self.pushButton_Voltar.setText(_translate("Form_DetalheUtilizador", "Voltar"))
