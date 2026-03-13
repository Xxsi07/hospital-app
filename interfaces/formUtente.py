# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        MainWindow.setWindowIcon(QtGui.QIcon(os.path.join(os.path.dirname(__file__), "imagens", "logo.png")))
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("""
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
    padding: 10px 20px;
    font-weight: bold;
    min-height: 35px;
}

QPushButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #14919B, stop:1 #0D7377);
}

QPushButton:pressed {
    background: #0A5D60;
}

QLabel {
    color: #0D7377;
    background: transparent;
}

QLCDNumber {
    border: 2px solid #14919B;
    border-radius: 10px;
    background-color: #0D7377;
    color: #00FF88;
}

QTableView {
    border: 2px solid #B8D4E3;
    border-radius: 8px;
    gridline-color: #E0E0E0;
    background-color: white;
    selection-background-color: #B2EBF2;
    alternate-background-color: #F5FAFA;
}

QHeaderView::section {
    background-color: #0D7377;
    color: white;
    padding: 8px;
    border: none;
    font-weight: bold;
}
""")
        self.centralwidget.setObjectName("centralwidget")
        
        # Layout principal
        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainLayout.setContentsMargins(30, 20, 30, 20)
        self.mainLayout.setSpacing(15)
        
        # === TOPO: Nome + Relógio ===
        self.topLayout = QtWidgets.QHBoxLayout()
        
        self.label_NomeUtilizador = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        self.label_NomeUtilizador.setFont(font)
        self.label_NomeUtilizador.setObjectName("label_NomeUtilizador")
        self.topLayout.addWidget(self.label_NomeUtilizador)
        
        self.topLayout.addStretch()
        
        self.RelogioLCD = QtWidgets.QLCDNumber()
        self.RelogioLCD.setMinimumSize(80, 35)
        self.RelogioLCD.setMaximumSize(100, 40)
        self.RelogioLCD.setObjectName("RelogioLCD")
        self.topLayout.addWidget(self.RelogioLCD)
        
        self.mainLayout.addLayout(self.topLayout)
        
        # === TÍTULO: Consultas de Hoje ===
        self.label_Consultas = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setItalic(True)
        self.label_Consultas.setFont(font)
        self.label_Consultas.setObjectName("label_Consultas")
        self.mainLayout.addWidget(self.label_Consultas)
        
        # === ÁREA CENTRAL: Tabela + Botões ===
        self.centerLayout = QtWidgets.QHBoxLayout()
        self.centerLayout.setSpacing(20)
        
        # Tabela de consultas
        self.tableView_Consultas = QtWidgets.QTableView()
        self.tableView_Consultas.setMinimumWidth(500)
        self.tableView_Consultas.setObjectName("tableView_Consultas")
        self.centerLayout.addWidget(self.tableView_Consultas, stretch=3)
        
        # Coluna de botões
        self.buttonsLayout = QtWidgets.QVBoxLayout()
        self.buttonsLayout.setSpacing(10)
        
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        
        # Botão Receitas
        self.pushButton_Receitas = QtWidgets.QPushButton()
        self.pushButton_Receitas.setFont(font)
        self.pushButton_Receitas.setMinimumWidth(180)
        self.pushButton_Receitas.setObjectName("pushButton_Receitas")
        self.buttonsLayout.addWidget(self.pushButton_Receitas)
        
        # Layout horizontal para Consultas de Hoje e Todas as Consultas
        self.consultasLayout = QtWidgets.QHBoxLayout()
        self.consultasLayout.setSpacing(10)
        
        # Botão Consultas de Hoje
        self.pushButton_ConsultasHoje = QtWidgets.QPushButton()
        self.pushButton_ConsultasHoje.setFont(font)
        self.pushButton_ConsultasHoje.setObjectName("pushButton_ConsultasHoje")
        self.consultasLayout.addWidget(self.pushButton_ConsultasHoje)
        
        # Botão Todas as Consultas
        self.pushButton_TodasConsultas = QtWidgets.QPushButton()
        self.pushButton_TodasConsultas.setFont(font)
        self.pushButton_TodasConsultas.setObjectName("pushButton_TodasConsultas")
        self.consultasLayout.addWidget(self.pushButton_TodasConsultas)
        
        self.buttonsLayout.addLayout(self.consultasLayout)
        
        self.buttonsLayout.addStretch()
        
        # Botão Logout
        self.pushButton_Logout = QtWidgets.QPushButton()
        self.pushButton_Logout.setFont(font)
        self.pushButton_Logout.setMinimumWidth(180)
        self.pushButton_Logout.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #C0392B, stop:1 #E74C3C);
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #E74C3C, stop:1 #C0392B);
            }
        """)
        self.pushButton_Logout.setObjectName("pushButton_Logout")
        self.buttonsLayout.addWidget(self.pushButton_Logout)
        
        self.centerLayout.addLayout(self.buttonsLayout)
        self.mainLayout.addLayout(self.centerLayout, stretch=1)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OmniCare - Área do Utente"))
        self.label_NomeUtilizador.setText(_translate("MainWindow", "Nome"))
        self.label_Consultas.setText(_translate("MainWindow", "Consultas de Hoje:"))
        self.pushButton_Receitas.setText(_translate("MainWindow", "Receitas"))
        self.pushButton_ConsultasHoje.setText(_translate("MainWindow", "Consultas de Hoje"))
        self.pushButton_TodasConsultas.setText(_translate("MainWindow", "Todas as Consultas"))
        self.pushButton_Logout.setText(_translate("MainWindow", "Logout"))
