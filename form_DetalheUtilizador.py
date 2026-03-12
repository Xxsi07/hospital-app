from PyQt5 import QtWidgets
from interfaces.formDetalheUtilizador import Ui_Form_DetalheUtilizador
from base_dados import ligacao_BD, listagem_BD, consultaUmValor, operacao_DML


class FormDetalheUtilizador(QtWidgets.QMainWindow, Ui_Form_DetalheUtilizador):
    def __init__(self, form_administrador):
        super().__init__()
        self.setupUi(self)
        
        self.form_administrador = form_administrador
        self.opcao = None
        
        self.pushButton_Voltar.clicked.connect(self.voltar)
        self.pushButton_Gravar.clicked.connect(self.gravar)
        
        # Carregar cargos no combobox
        self.carregar_cargos()
    
    def carregar_cargos(self):
        try:
            conn_BD = ligacao_BD()
            if conn_BD and conn_BD != -1:
                cmd_sql = "SELECT Id, Designacao FROM cargos ORDER BY Designacao;"
                dados = listagem_BD(conn_BD, cmd_sql)
                
                self.comboBox_Cargo.clear()
                
                if dados and dados != -1:
                    for cargo in dados:
                        self.comboBox_Cargo.addItem(cargo[1], cargo[0])
                
                conn_BD.close()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao carregar cargos: {e}")
    
    def inicializar_novo(self):
        self.label_Titulo.setText("Novo Utilizador")
        self.lineEdit_Id.setText("")
        self.lineEdit_Username.setText("")
        self.lineEdit_Password.setText("")
        self.lineEdit_Nome.setText("")
        self.lineEdit_Email.setText("")
        self.lineEdit_Telefone.setText("")
        self.comboBox_Cargo.setCurrentIndex(0)
        self.lineEdit_Id.setEnabled(False)
    
    def inicializar_alterar(self, selecao):
        self.label_Titulo.setText("Editar Utilizador")
        linha = selecao[0].row()
        modelo = self.form_administrador.tableView_Utilizadores.model()
        
        id_utilizador = modelo.data(modelo.index(linha, 0))
        
        # Buscar dados completos do utilizador
        try:
            conn_BD = ligacao_BD()
            if conn_BD and conn_BD != -1:
                cmd_sql = f"SELECT Id, Username, Password, Nome, Email, Telefone, Cargos FROM utilizador WHERE Id = {id_utilizador};"
                dados = listagem_BD(conn_BD, cmd_sql)
                
                if dados and dados != -1 and len(dados) > 0:
                    utilizador = dados[0]
                    self.lineEdit_Id.setText(str(utilizador[0]))
                    self.lineEdit_Username.setText(str(utilizador[1]) if utilizador[1] else "")
                    self.lineEdit_Password.setText(str(utilizador[2]) if utilizador[2] else "")
                    self.lineEdit_Nome.setText(str(utilizador[3]) if utilizador[3] else "")
                    self.lineEdit_Email.setText(str(utilizador[4]) if utilizador[4] else "")
                    self.lineEdit_Telefone.setText(str(utilizador[5]) if utilizador[5] else "")
                    
                    # Selecionar cargo no combobox
                    id_cargo = utilizador[6]
                    index = self.comboBox_Cargo.findData(id_cargo)
                    if index >= 0:
                        self.comboBox_Cargo.setCurrentIndex(index)
                
                self.lineEdit_Id.setEnabled(False)
                conn_BD.close()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao carregar dados do utilizador: {e}")
    
    def gravar(self):
        username = self.lineEdit_Username.text().strip()
        password = self.lineEdit_Password.text().strip()
        nome = self.lineEdit_Nome.text().strip()
        email = self.lineEdit_Email.text().strip()
        telefone = self.lineEdit_Telefone.text().strip()
        id_cargo = self.comboBox_Cargo.currentData()
        
        # Validações
        if not username or not password or not nome:
            QtWidgets.QMessageBox.warning(self, "Aviso", "Os campos Username, Password e Nome são obrigatórios!")
            return
        
        if self.opcao == "novo":
            try:
                conn_BD = ligacao_BD()
                if not conn_BD or conn_BD == -1:
                    QtWidgets.QMessageBox.critical(self, "Erro", "A ligação à BD não está estabelecida")
                    return
                
                # Verificar se username já existe
                cmd_sql = "SELECT COUNT(*) FROM utilizador WHERE Username = %s;"
                num_registos = consultaUmValor(conn_BD, cmd_sql, (username,))
                if num_registos > 0:
                    QtWidgets.QMessageBox.warning(self, "Aviso", "Já existe um utilizador com este username!")
                    conn_BD.close()
                    return
                
                # Verificar se email já existe (se foi preenchido)
                if email:
                    cmd_sql = "SELECT COUNT(*) FROM utilizador WHERE Email = %s;"
                    num_registos = consultaUmValor(conn_BD, cmd_sql, (email,))
                    if num_registos > 0:
                        QtWidgets.QMessageBox.warning(self, "Aviso", "Já existe um utilizador com este email!")
                        conn_BD.close()
                        return
                
                cmd_sql = "INSERT INTO utilizador(Username, Password, Cargos, Nome, Email, Telefone) VALUES(%s, %s, %s, %s, %s, %s);"
                resultado = operacao_DML(conn_BD, cmd_sql, (username, password, id_cargo, nome, email if email else None, telefone if telefone else None))
                
                if resultado == -1:
                    QtWidgets.QMessageBox.critical(self, "Erro", "Ocorreu um erro ao inserir o utilizador")
                    conn_BD.close()
                    return
                
                resposta = QtWidgets.QMessageBox.question(self, "Sucesso", "Utilizador adicionado com sucesso!\nPretende inserir outro utilizador?")
                if resposta == QtWidgets.QMessageBox.Yes:
                    self.inicializar_novo()
                else:
                    self.voltar()
                
                conn_BD.close()
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Erro", f"Erro: {e}")
        
        elif self.opcao == "editar":
            try:
                id_utilizador = self.lineEdit_Id.text()
                
                conn_BD = ligacao_BD()
                if not conn_BD or conn_BD == -1:
                    QtWidgets.QMessageBox.critical(self, "Erro", "A ligação à BD não está estabelecida")
                    return
                
                # Verificar se username já existe (para outro utilizador)
                cmd_sql = "SELECT COUNT(*) FROM utilizador WHERE Username = %s AND Id != %s;"
                num_registos = consultaUmValor(conn_BD, cmd_sql, (username, id_utilizador))
                if num_registos > 0:
                    QtWidgets.QMessageBox.warning(self, "Aviso", "Já existe outro utilizador com este username!")
                    conn_BD.close()
                    return
                
                # Verificar se email já existe (para outro utilizador)
                if email:
                    cmd_sql = "SELECT COUNT(*) FROM utilizador WHERE Email = %s AND Id != %s;"
                    num_registos = consultaUmValor(conn_BD, cmd_sql, (email, id_utilizador))
                    if num_registos > 0:
                        QtWidgets.QMessageBox.warning(self, "Aviso", "Já existe outro utilizador com este email!")
                        conn_BD.close()
                        return
                
                cmd_sql = "UPDATE utilizador SET Username = %s, Password = %s, Cargos = %s, Nome = %s, Email = %s, Telefone = %s WHERE Id = %s;"
                resultado = operacao_DML(conn_BD, cmd_sql, (username, password, id_cargo, nome, email if email else None, telefone if telefone else None, id_utilizador))
                
                QtWidgets.QMessageBox.information(self, "Sucesso", "Utilizador alterado com sucesso!")
                self.voltar()
                
                conn_BD.close()
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Erro", f"Erro: {e}")
    
    def voltar(self):
        self.close()
        self.form_administrador.show()
        self.form_administrador.listar_utilizadores()
