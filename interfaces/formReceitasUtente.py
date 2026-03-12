# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_ReceitasUtente(object):
    def setupUi(self, Form_ReceitasUtente):
        Form_ReceitasUtente.setObjectName("Form_ReceitasUtente")
        Form_ReceitasUtente.resize(800, 550)
        Form_ReceitasUtente.setWindowIcon(QtGui.QIcon("UI/imagens/logo.png"))
        Form_ReceitasUtente.setStyleSheet("""
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
        
        self.centralwidget = QtWidgets.QWidget(Form_ReceitasUtente)
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
        
        self.label_DataHora = QtWidgets.QLabel(self.centralwidget)
        self.label_DataHora.setGeometry(QtCore.QRect(550, 15, 230, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_DataHora.setFont(font)
        self.label_DataHora.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.label_DataHora.setObjectName("label_DataHora")
        
        self.tableView_Receitas = QtWidgets.QTableView(self.centralwidget)
        self.tableView_Receitas.setGeometry(QtCore.QRect(20, 50, 760, 430))
        self.tableView_Receitas.setObjectName("tableView_Receitas")
        
        self.pushButton_Voltar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Voltar.setGeometry(QtCore.QRect(660, 490, 120, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Voltar.setFont(font)
        self.pushButton_Voltar.setObjectName("pushButton_Voltar")
        
        Form_ReceitasUtente.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(Form_ReceitasUtente)
        QtCore.QMetaObject.connectSlotsByName(Form_ReceitasUtente)

    def retranslateUi(self, Form_ReceitasUtente):
        _translate = QtCore.QCoreApplication.translate
        Form_ReceitasUtente.setWindowTitle(_translate("Form_ReceitasUtente", "OmniCare - Minhas Receitas"))
        self.label_Titulo.setText(_translate("Form_ReceitasUtente", "Receitas Ativas"))
        self.label_DataHora.setText(_translate("Form_ReceitasUtente", "Data/Hora Atual:"))
        self.pushButton_Voltar.setText(_translate("Form_ReceitasUtente", "Voltar"))
