# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_Login(object):
    def setupUi(self, MainWindow_Login):
        MainWindow_Login.setObjectName("MainWindow_Login")
        MainWindow_Login.setEnabled(True)
        MainWindow_Login.resize(800, 600)
        MainWindow_Login.setWindowIcon(QtGui.QIcon("UI/imagens/logo.png"))
        
        self.centralwidget = QtWidgets.QWidget(MainWindow_Login)
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
    min-height: 40px;
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
    padding: 10px;
    min-height: 35px;
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
""")
        self.centralwidget.setObjectName("centralwidget")
        
        # Layout principal
        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainLayout.setContentsMargins(50, 30, 50, 30)
        self.mainLayout.setSpacing(20)
        
        # Relógio no topo direito
        self.topLayout = QtWidgets.QHBoxLayout()
        self.topLayout.addStretch()
        
        self.relogioLCD = QtWidgets.QLCDNumber()
        self.relogioLCD.setMinimumSize(80, 35)
        self.relogioLCD.setMaximumSize(100, 40)
        self.relogioLCD.setObjectName("relogioLCD")
        self.topLayout.addWidget(self.relogioLCD)
        
        self.mainLayout.addLayout(self.topLayout)
        
        # Espaço flexível superior
        self.mainLayout.addStretch()
        
        # Container central para o formulário
        self.formContainer = QtWidgets.QWidget()
        self.formContainer.setMaximumWidth(400)
        self.formLayout = QtWidgets.QVBoxLayout(self.formContainer)
        self.formLayout.setSpacing(15)
        
        # Título OmniCare
        self.label_LoginTitulo = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(42)
        font.setBold(True)
        self.label_LoginTitulo.setFont(font)
        self.label_LoginTitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_LoginTitulo.setObjectName("label_LoginTitulo")
        self.formLayout.addWidget(self.label_LoginTitulo)
        
        self.formLayout.addSpacing(30)
        
        # Label Utilizador
        self.label_Utilizador = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        self.label_Utilizador.setFont(font)
        self.label_Utilizador.setObjectName("label_Utilizador")
        self.formLayout.addWidget(self.label_Utilizador)
        
        # Campo Utilizador
        self.lineEdit_Utilizador = QtWidgets.QLineEdit()
        self.lineEdit_Utilizador.setStyleSheet("background-color: white; color: #2C3E50;")
        self.lineEdit_Utilizador.setObjectName("lineEdit_Utilizador")
        self.formLayout.addWidget(self.lineEdit_Utilizador)
        
        self.formLayout.addSpacing(10)
        
        # Label Palavra-Passe
        self.label_Passe = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        self.label_Passe.setFont(font)
        self.label_Passe.setObjectName("label_Passe")
        self.formLayout.addWidget(self.label_Passe)
        
        # Campo Palavra-Passe
        self.lineEdit_Passe = QtWidgets.QLineEdit()
        self.lineEdit_Passe.setStyleSheet("background-color: white; color: #2C3E50;")
        self.lineEdit_Passe.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_Passe.setObjectName("lineEdit_Passe")
        self.formLayout.addWidget(self.lineEdit_Passe)
        
        self.formLayout.addSpacing(20)
        
        # Layout para botão centralizado
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.buttonLayout.addStretch()
        
        # Botão Entrar
        self.pushButton_Entrar = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        self.pushButton_Entrar.setFont(font)
        self.pushButton_Entrar.setMinimumWidth(150)
        self.pushButton_Entrar.setObjectName("pushButton_Entrar")
        self.buttonLayout.addWidget(self.pushButton_Entrar)
        
        self.buttonLayout.addStretch()
        self.formLayout.addLayout(self.buttonLayout)
        
        # Centrar o formulário horizontalmente
        self.centerFormLayout = QtWidgets.QHBoxLayout()
        self.centerFormLayout.addStretch()
        self.centerFormLayout.addWidget(self.formContainer)
        self.centerFormLayout.addStretch()
        
        self.mainLayout.addLayout(self.centerFormLayout)
        
        # Espaço flexível inferior
        self.mainLayout.addStretch()
        
        MainWindow_Login.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_Login)
        self.statusbar.setObjectName("statusbar")
        MainWindow_Login.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_Login)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_Login)

    def retranslateUi(self, MainWindow_Login):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_Login.setWindowTitle(_translate("MainWindow_Login", "OmniCare - Login"))
        self.label_LoginTitulo.setText(_translate("MainWindow_Login", "OmniCare"))
        self.label_Utilizador.setText(_translate("MainWindow_Login", "Utilizador:"))
        self.label_Passe.setText(_translate("MainWindow_Login", "Palavra-Passe:"))
        self.pushButton_Entrar.setText(_translate("MainWindow_Login", "Entrar"))
