from PyQt5 import QtWidgets
from interfaces.formLogin import Ui_MainWindow_Login
from base_dados import ligacao_BD, listagem_BD
from form_Medicos import FormMedicos
from form_Utente import FormUtente

class FormLogin(QtWidgets.QMainWindow, Ui_MainWindow_Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Ocultar o texto da password digitada
        self.lineEdit_Passe.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.pushButton_Entrar.clicked.connect(self.efetuar_login)
        
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
                    self.janela_medicos.show()
                elif "utente" in cargo:
                    self.hide() # esconde a janela atual
                    self.janela_utente = FormUtente(id_utilizador, nome_utilizador)
                    self.janela_utente.show()
                else:
                    QtWidgets.QMessageBox.warning(self, "Aviso", f"Cargo não suportado ({cargo}).")
            else:
                QtWidgets.QMessageBox.warning(self, "Erro", "Utilizador ou Password incorretos!")
