# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_ReceitasConsulta(object):
    def setupUi(self, Form_ReceitasConsulta):
        Form_ReceitasConsulta.setObjectName("Form_ReceitasConsulta")
        Form_ReceitasConsulta.resize(700, 500)
        Form_ReceitasConsulta.setWindowIcon(QtGui.QIcon("UI/imagens/logo.png"))
        Form_ReceitasConsulta.setStyleSheet("""
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

QTableView {
    border: 2px solid #B8D4E3;
    border-radius: 8px;
    gridline-color: #E0E0E0;
    background-color: white;
    selection-background-color: #B2EBF2;
}

QHeaderView::section {
    background-color: #0D7377;
    color: white;
    padding: 8px;
    border: none;
    font-weight: bold;
}
""")
        
        self.centralwidget = QtWidgets.QWidget(Form_ReceitasConsulta)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label_Titulo = QtWidgets.QLabel(self.centralwidget)
        self.label_Titulo.setGeometry(QtCore.QRect(20, 10, 500, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_Titulo.setFont(font)
        self.label_Titulo.setObjectName("label_Titulo")
        
        self.label_InfoConsulta = QtWidgets.QLabel(self.centralwidget)
        self.label_InfoConsulta.setGeometry(QtCore.QRect(20, 50, 500, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_InfoConsulta.setFont(font)
        self.label_InfoConsulta.setObjectName("label_InfoConsulta")
        
        self.tableView_Receitas = QtWidgets.QTableView(self.centralwidget)
        self.tableView_Receitas.setGeometry(QtCore.QRect(20, 80, 560, 350))
        self.tableView_Receitas.setObjectName("tableView_Receitas")
        
        self.pushButton_Eliminar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Eliminar.setGeometry(QtCore.QRect(590, 80, 90, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Eliminar.setFont(font)
        self.pushButton_Eliminar.setObjectName("pushButton_Eliminar")
        
        self.pushButton_Voltar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Voltar.setGeometry(QtCore.QRect(560, 450, 120, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Voltar.setFont(font)
        self.pushButton_Voltar.setObjectName("pushButton_Voltar")
        
        Form_ReceitasConsulta.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(Form_ReceitasConsulta)
        QtCore.QMetaObject.connectSlotsByName(Form_ReceitasConsulta)

    def retranslateUi(self, Form_ReceitasConsulta):
        _translate = QtCore.QCoreApplication.translate
        Form_ReceitasConsulta.setWindowTitle(_translate("Form_ReceitasConsulta", "OmniCare - Receitas da Consulta"))
        self.label_Titulo.setText(_translate("Form_ReceitasConsulta", "Receitas da Consulta"))
        self.label_InfoConsulta.setText(_translate("Form_ReceitasConsulta", "Consulta:"))
        self.pushButton_Eliminar.setText(_translate("Form_ReceitasConsulta", "Eliminar"))
        self.pushButton_Voltar.setText(_translate("Form_ReceitasConsulta", "Voltar"))
