# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_Medicos(object):
    def setupUi(self, MainWindow_Medicos):
        MainWindow_Medicos.setObjectName("MainWindow_Medicos")
        MainWindow_Medicos.resize(1000, 700)
        MainWindow_Medicos.setWindowIcon(QtGui.QIcon("UI/imagens/logo.png"))
        
        self.centralwidget = QtWidgets.QWidget(MainWindow_Medicos)
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

QDateTimeEdit, QDateEdit, QTimeEdit {
    background-color: white;
    color: #2C3E50;
    border: 2px solid #B8D4E3;
    border-radius: 8px;
    padding: 5px;
    min-height: 25px;
}

QComboBox {
    background-color: white;
    color: #2C3E50;
    border: 2px solid #B8D4E3;
    border-radius: 8px;
    padding: 5px;
}

QComboBox:focus, QDateTimeEdit:focus, QDateEdit:focus, QTimeEdit:focus {
    border: 2px solid #14919B;
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
        
        # Botão Nova Consulta
        self.pushButton_NovaConsulta = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton_NovaConsulta.setFont(font)
        self.pushButton_NovaConsulta.setMinimumWidth(180)
        self.pushButton_NovaConsulta.setObjectName("pushButton_NovaConsulta")
        self.buttonsLayout.addWidget(self.pushButton_NovaConsulta)
        
        # Botão Concluir Consulta
        self.pushButton_ConcluirConsulta = QtWidgets.QPushButton()
        self.pushButton_ConcluirConsulta.setFont(font)
        self.pushButton_ConcluirConsulta.setMinimumWidth(180)
        self.pushButton_ConcluirConsulta.setObjectName("pushButton_ConcluirConsulta")
        self.buttonsLayout.addWidget(self.pushButton_ConcluirConsulta)
        
        # Botão Adiar Consulta
        self.pushButton_AdiarConsulta = QtWidgets.QPushButton()
        self.pushButton_AdiarConsulta.setFont(font)
        self.pushButton_AdiarConsulta.setMinimumWidth(180)
        self.pushButton_AdiarConsulta.setObjectName("pushButton_AdiarConsulta")
        self.buttonsLayout.addWidget(self.pushButton_AdiarConsulta)
        
        # Botão Cancelar Consulta
        self.pushButton_RemoverConsulta = QtWidgets.QPushButton()
        self.pushButton_RemoverConsulta.setFont(font)
        self.pushButton_RemoverConsulta.setMinimumWidth(180)
        self.pushButton_RemoverConsulta.setObjectName("pushButton_RemoverConsulta")
        self.buttonsLayout.addWidget(self.pushButton_RemoverConsulta)
        
        self.buttonsLayout.addSpacing(20)
        
        # Botão Nova Receita
        self.pushButton_NovaReceita = QtWidgets.QPushButton()
        self.pushButton_NovaReceita.setFont(font)
        self.pushButton_NovaReceita.setMinimumWidth(180)
        self.pushButton_NovaReceita.setObjectName("pushButton_NovaReceita")
        self.buttonsLayout.addWidget(self.pushButton_NovaReceita)
        
        # Botão Receitas
        self.pushButton_Receitas = QtWidgets.QPushButton()
        self.pushButton_Receitas.setFont(font)
        self.pushButton_Receitas.setMinimumWidth(180)
        self.pushButton_Receitas.setObjectName("pushButton_Receitas")
        self.buttonsLayout.addWidget(self.pushButton_Receitas)
        
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
        
        # === RODAPÉ: Filtros ===
        self.filterLayout = QtWidgets.QHBoxLayout()
        self.filterLayout.setSpacing(10)
        
        self.label_FiltroData = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.label_FiltroData.setFont(font)
        self.label_FiltroData.setObjectName("label_FiltroData")
        self.filterLayout.addWidget(self.label_FiltroData)
        
        self.dateTimeEdit_Consultas1 = QtWidgets.QDateTimeEdit()
        self.dateTimeEdit_Consultas1.setMinimumWidth(150)
        self.dateTimeEdit_Consultas1.setObjectName("dateTimeEdit_Consultas1")
        self.filterLayout.addWidget(self.dateTimeEdit_Consultas1)
        
        self.dateTimeEdit_Consultas2 = QtWidgets.QDateTimeEdit()
        self.dateTimeEdit_Consultas2.setMinimumWidth(150)
        self.dateTimeEdit_Consultas2.setObjectName("dateTimeEdit_Consultas2")
        self.filterLayout.addWidget(self.dateTimeEdit_Consultas2)
        
        self.filterLayout.addStretch()
        
        self.pushButton_ConsultasHoje = QtWidgets.QPushButton()
        self.pushButton_ConsultasHoje.setFont(font)
        self.pushButton_ConsultasHoje.setMinimumWidth(150)
        self.pushButton_ConsultasHoje.setObjectName("pushButton_ConsultasHoje")
        self.filterLayout.addWidget(self.pushButton_ConsultasHoje)
        
        self.pushButton_TodasConsultas = QtWidgets.QPushButton()
        self.pushButton_TodasConsultas.setFont(font)
        self.pushButton_TodasConsultas.setMinimumWidth(160)
        self.pushButton_TodasConsultas.setObjectName("pushButton_TodasConsultas")
        self.filterLayout.addWidget(self.pushButton_TodasConsultas)
        
        self.mainLayout.addLayout(self.filterLayout)
        
        MainWindow_Medicos.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_Medicos)
        self.statusbar.setObjectName("statusbar")
        MainWindow_Medicos.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_Medicos)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_Medicos)

    def retranslateUi(self, MainWindow_Medicos):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_Medicos.setWindowTitle(_translate("MainWindow_Medicos", "OmniCare - Área Médica"))
        self.label_NomeUtilizador.setText(_translate("MainWindow_Medicos", "Nome"))
        self.label_Consultas.setText(_translate("MainWindow_Medicos", "Consultas de Hoje:"))
        self.pushButton_NovaConsulta.setText(_translate("MainWindow_Medicos", "Nova Consulta"))
        self.pushButton_ConcluirConsulta.setText(_translate("MainWindow_Medicos", "Concluir Consulta"))
        self.pushButton_AdiarConsulta.setText(_translate("MainWindow_Medicos", "Adiar Consulta"))
        self.pushButton_RemoverConsulta.setText(_translate("MainWindow_Medicos", "Cancelar Consulta"))
        self.pushButton_NovaReceita.setText(_translate("MainWindow_Medicos", "Nova Receita"))
        self.pushButton_Receitas.setText(_translate("MainWindow_Medicos", "Receitas"))
        self.pushButton_Logout.setText(_translate("MainWindow_Medicos", "Logout"))
        self.label_FiltroData.setText(_translate("MainWindow_Medicos", "Entre:"))
        self.pushButton_ConsultasHoje.setText(_translate("MainWindow_Medicos", "Consultas de hoje"))
        self.pushButton_TodasConsultas.setText(_translate("MainWindow_Medicos", "Todas as Consultas"))

