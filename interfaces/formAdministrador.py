# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_Administrador(object):
    def setupUi(self, MainWindow_Administrador):
        MainWindow_Administrador.setObjectName("MainWindow_Administrador")
        MainWindow_Administrador.resize(1000, 700)
        MainWindow_Administrador.setWindowIcon(QtGui.QIcon("UI/imagens/logo.png"))
        
        self.centralwidget = QtWidgets.QWidget(MainWindow_Administrador)
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

QLineEdit {
    background-color: white;
    color: #2C3E50;
    border: 2px solid #B8D4E3;
    border-radius: 8px;
    padding: 8px;
    min-height: 25px;
}

QLineEdit:focus {
    border: 2px solid #14919B;
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

QComboBox {
    background-color: white;
    color: #2C3E50;
    border: 2px solid #B8D4E3;
    border-radius: 8px;
    padding: 5px;
    min-height: 25px;
}

QComboBox:focus {
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
        
        # === TÍTULO: Gestão de Utilizadores ===
        self.label_Utilizadores = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setItalic(True)
        self.label_Utilizadores.setFont(font)
        self.label_Utilizadores.setObjectName("label_Utilizadores")
        self.mainLayout.addWidget(self.label_Utilizadores)
        
        # === FILTROS ===
        self.filterLayout = QtWidgets.QHBoxLayout()
        self.filterLayout.setSpacing(10)
        
        self.lineEdit_Filtro = QtWidgets.QLineEdit()
        self.lineEdit_Filtro.setMinimumWidth(200)
        self.lineEdit_Filtro.setPlaceholderText("Filtrar por nome...")
        self.lineEdit_Filtro.setObjectName("lineEdit_Filtro")
        self.filterLayout.addWidget(self.lineEdit_Filtro)
        
        self.comboBox_Cargo = QtWidgets.QComboBox()
        self.comboBox_Cargo.setMinimumWidth(150)
        self.comboBox_Cargo.setObjectName("comboBox_Cargo")
        self.filterLayout.addWidget(self.comboBox_Cargo)
        
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        
        self.pushButton_Filtrar = QtWidgets.QPushButton()
        self.pushButton_Filtrar.setFont(font)
        self.pushButton_Filtrar.setMinimumWidth(100)
        self.pushButton_Filtrar.setObjectName("pushButton_Filtrar")
        self.filterLayout.addWidget(self.pushButton_Filtrar)
        
        self.pushButton_Limpar = QtWidgets.QPushButton()
        self.pushButton_Limpar.setFont(font)
        self.pushButton_Limpar.setMinimumWidth(100)
        self.pushButton_Limpar.setObjectName("pushButton_Limpar")
        self.filterLayout.addWidget(self.pushButton_Limpar)
        
        self.filterLayout.addStretch()
        
        self.mainLayout.addLayout(self.filterLayout)
        
        # === ÁREA CENTRAL: Tabela + Botões ===
        self.centerLayout = QtWidgets.QHBoxLayout()
        self.centerLayout.setSpacing(20)
        
        # Tabela de utilizadores
        self.tableView_Utilizadores = QtWidgets.QTableView()
        self.tableView_Utilizadores.setMinimumWidth(500)
        self.tableView_Utilizadores.setObjectName("tableView_Utilizadores")
        self.centerLayout.addWidget(self.tableView_Utilizadores, stretch=3)
        
        # Coluna de botões
        self.buttonsLayout = QtWidgets.QVBoxLayout()
        self.buttonsLayout.setSpacing(10)
        
        # Botão Novo
        self.pushButton_Novo = QtWidgets.QPushButton()
        self.pushButton_Novo.setFont(font)
        self.pushButton_Novo.setMinimumWidth(150)
        self.pushButton_Novo.setObjectName("pushButton_Novo")
        self.buttonsLayout.addWidget(self.pushButton_Novo)
        
        # Botão Editar
        self.pushButton_Editar = QtWidgets.QPushButton()
        self.pushButton_Editar.setFont(font)
        self.pushButton_Editar.setMinimumWidth(150)
        self.pushButton_Editar.setObjectName("pushButton_Editar")
        self.buttonsLayout.addWidget(self.pushButton_Editar)
        
        # Botão Eliminar
        self.pushButton_Eliminar = QtWidgets.QPushButton()
        self.pushButton_Eliminar.setFont(font)
        self.pushButton_Eliminar.setMinimumWidth(150)
        self.pushButton_Eliminar.setObjectName("pushButton_Eliminar")
        self.buttonsLayout.addWidget(self.pushButton_Eliminar)
        
        self.buttonsLayout.addStretch()
        
        # Botão Sair
        self.pushButton_Sair = QtWidgets.QPushButton()
        self.pushButton_Sair.setFont(font)
        self.pushButton_Sair.setMinimumWidth(150)
        self.pushButton_Sair.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #C0392B, stop:1 #E74C3C);
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #E74C3C, stop:1 #C0392B);
            }
        """)
        self.pushButton_Sair.setObjectName("pushButton_Sair")
        self.buttonsLayout.addWidget(self.pushButton_Sair)
        
        self.centerLayout.addLayout(self.buttonsLayout)
        self.mainLayout.addLayout(self.centerLayout, stretch=1)
        
        MainWindow_Administrador.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_Administrador)
        self.statusbar.setObjectName("statusbar")
        MainWindow_Administrador.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow_Administrador)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_Administrador)

    def retranslateUi(self, MainWindow_Administrador):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_Administrador.setWindowTitle(_translate("MainWindow_Administrador", "OmniCare - Administração"))
        self.label_NomeUtilizador.setText(_translate("MainWindow_Administrador", "Bem vindo Administrador"))
        self.label_Utilizadores.setText(_translate("MainWindow_Administrador", "Gestão de Utilizadores:"))
        self.pushButton_Filtrar.setText(_translate("MainWindow_Administrador", "Filtrar"))
        self.pushButton_Limpar.setText(_translate("MainWindow_Administrador", "Limpar"))
        self.pushButton_Novo.setText(_translate("MainWindow_Administrador", "Novo"))
        self.pushButton_Editar.setText(_translate("MainWindow_Administrador", "Editar"))
        self.pushButton_Eliminar.setText(_translate("MainWindow_Administrador", "Eliminar"))
        self.pushButton_Sair.setText(_translate("MainWindow_Administrador", "Sair"))
