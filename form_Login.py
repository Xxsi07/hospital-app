from PyQt5 import QtWidgets, QtCore
from interfaces.formLogin import Ui_MainWindow_Login
from base_dados import ligacao_BD, listagem_BD
from form_Medicos import FormMedicos
from form_Utente import FormUtente
from form_Administrador import FormAdministrador

class FormLogin(QtWidgets.QMainWindow, Ui_MainWindow_Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lineEdit_Utilizador.setMinimumHeight(28)
        self.lineEdit_Utilizador.setMaximumHeight(28)
        self.lineEdit_Passe.setMinimumHeight(28)
        self.lineEdit_Passe.setMaximumHeight(28)
        
        # Ocultar o texto da password digitada
        self.lineEdit_Passe.setEchoMode(QtWidgets.QLineEdit.Password)
        
        # Ligar Enter (Return) nos campos de texto ao login
        self.lineEdit_Utilizador.returnPressed.connect(self.efetuar_login)
        self.lineEdit_Passe.returnPressed.connect(self.efetuar_login)
        
        self.pushButton_Entrar.clicked.connect(self.efetuar_login)
        
        # Configurar relógio em tempo real
        self.timer_relogio = QtCore.QTimer(self)
        self.timer_relogio.timeout.connect(self.atualizar_relogio)
        self.timer_relogio.start(1000)  # Atualiza a cada 1 segundo
        self.atualizar_relogio()  # Chama imediatamente para mostrar a hora
    
    def atualizar_relogio(self):
        """Atualiza o LCD com a hora atual"""
        hora_atual = QtCore.QTime.currentTime().toString("HH:mm")
        if hasattr(self, 'relogioLCD'):
            self.relogioLCD.display(hora_atual)
        
    def efetuar_login(self):
        username = self.lineEdit_Utilizador.text()
        password = self.lineEdit_Passe.text()

        conn = ligacao_BD()
        if conn != -1:
            # Junta com a tabela cargos para saber a designação e pega o Nome e o Id
            sql = f"""
                SELECT c.Designacao, u.Nome, u.Id
                FROM utilizador u 
                JOIN cargos c ON u.Cargos = c.Id 
                WHERE u.Username='{username}' AND u.Password='{password}'
            """
            utilizador = listagem_BD(conn, sql)
            
            if utilizador:
                cargo = utilizador[0][0].lower() # O cargo da base de dados, ex: 'medico' ou 'utente'
                nome_utilizador = utilizador[0][1] # O nome da pessoa
                id_utilizador = utilizador[0][2] # O Id do utilizador
                
                if "medico" in cargo or "médico" in cargo:
                    self.hide() # esconde a janela atual
                    self.janela_medicos = FormMedicos(id_utilizador, nome_utilizador)
                    self.janela_medicos.showMaximized()
                elif "utente" in cargo:
                    self.hide() # esconde a janela atual
                    self.janela_utente = FormUtente(id_utilizador, nome_utilizador)
                    self.janela_utente.showMaximized()
                elif "admin" in cargo or "administrador" in cargo:
                    self.hide() # esconde a janela atual
                    self.janela_admin = FormAdministrador(id_utilizador, nome_utilizador)
                    self.janela_admin.showMaximized()
                else:
                    QtWidgets.QMessageBox.warning(self, "Aviso", f"Cargo não suportado ({cargo}).")
            else:
                QtWidgets.QMessageBox.warning(self, "Erro", "Utilizador ou Password incorretos!")
