from PyQt5 import QtWidgets, QtGui, QtCore
from interfaces.formAdministrador import Ui_MainWindow_Administrador
from base_dados import ligacao_BD, listagem_BD, consultaUmValor, operacao_DML
from form_DetalheUtilizador import FormDetalheUtilizador


class FormAdministrador(QtWidgets.QMainWindow, Ui_MainWindow_Administrador):
    def __init__(self, id_utilizador=-1, nome_utilizador="Administrador", parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.id_utilizador = id_utilizador
        
        self.label_NomeUtilizador.setText(f"Bem vindo {nome_utilizador}")
        self.label_NomeUtilizador.adjustSize()
        
        # Configurar relógio em tempo real
        self.timer_relogio = QtCore.QTimer(self)
        self.timer_relogio.timeout.connect(self.atualizar_relogio)
        self.timer_relogio.start(1000)  # Atualiza a cada 1 segundo
        self.atualizar_relogio()  # Chama imediatamente para mostrar a hora
        
        # Formulário de detalhes
        self.form_detalhe_utilizador = FormDetalheUtilizador(self)
        
        # Carregar cargos no combobox
        self.carregar_cargos()
        
        # Conectar botões
        self.pushButton_Novo.clicked.connect(lambda: self.mostrar_form("novo"))
        self.pushButton_Editar.clicked.connect(lambda: self.mostrar_form("editar"))
        self.pushButton_Eliminar.clicked.connect(self.eliminar_utilizador)
        self.pushButton_Filtrar.clicked.connect(self.listar_utilizadores)
        self.pushButton_Limpar.clicked.connect(self.limpar_filtro)
        self.pushButton_Sair.clicked.connect(self.sair)
        self.lineEdit_Filtro.returnPressed.connect(self.listar_utilizadores)
        
        # Carregar utilizadores
        self.listar_utilizadores()
    
    def carregar_cargos(self):
        try:
            conn_BD = ligacao_BD()
            if conn_BD and conn_BD != -1:
                cmd_sql = "SELECT Id, Designacao FROM cargos ORDER BY Designacao;"
                dados = listagem_BD(conn_BD, cmd_sql)
                
                self.comboBox_Cargo.clear()
                self.comboBox_Cargo.addItem("Todos", 0)
                
                if dados and dados != -1:
                    for cargo in dados:
                        self.comboBox_Cargo.addItem(cargo[1], cargo[0])
                
                conn_BD.close()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao carregar cargos: {e}")
    
    def listar_utilizadores(self):
        try:
            conn_BD = ligacao_BD()
            if conn_BD and conn_BD != -1:
                filtro_nome = self.lineEdit_Filtro.text()
                filtro_cargo = self.comboBox_Cargo.currentData()
                
                cmd_sql = """
                    SELECT u.Id, u.Username, u.Nome, u.Email, u.Telefone, c.Designacao AS 'Cargo'
                    FROM utilizador u
                    JOIN cargos c ON u.Cargos = c.Id
                    WHERE 1=1
                """
                
                if filtro_nome:
                    cmd_sql += f" AND u.Nome LIKE '%{filtro_nome}%'"
                
                if filtro_cargo and filtro_cargo != 0:
                    cmd_sql += f" AND u.Cargos = {filtro_cargo}"
                
                cmd_sql += " ORDER BY u.Nome ASC;"
                
                dados = listagem_BD(conn_BD, cmd_sql)
                
                if dados == -1:
                    dados = []
                
                modelo = QtGui.QStandardItemModel()
                modelo.setHorizontalHeaderLabels(["ID", "Username", "Nome", "Email", "Telefone", "Cargo"])
                
                for linha in dados:
                    modelo.appendRow([QtGui.QStandardItem(str(celula) if celula else "") for celula in linha])
                
                self.tableView_Utilizadores.setModel(modelo)
                self.tableView_Utilizadores.resizeColumnsToContents()
                self.tableView_Utilizadores.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
                self.tableView_Utilizadores.setSelectionMode(QtWidgets.QTableView.SingleSelection)
                self.tableView_Utilizadores.setEditTriggers(QtWidgets.QTableView.NoEditTriggers)
                
                # Esconder coluna ID
                self.tableView_Utilizadores.setColumnHidden(0, True)
                
                conn_BD.close()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao listar utilizadores: {e}")
    
    def mostrar_form(self, opcao):
        if opcao == "editar":
            selecionados = self.tableView_Utilizadores.selectionModel().selectedRows()
            if not selecionados:
                QtWidgets.QMessageBox.warning(self, "Aviso", "Selecione um utilizador para editar!")
                return
            self.form_detalhe_utilizador.inicializar_alterar(selecionados)
        else:
            self.form_detalhe_utilizador.inicializar_novo()
        
        self.form_detalhe_utilizador.opcao = opcao
        self.form_detalhe_utilizador.show()
    
    def eliminar_utilizador(self):
        selecionados = self.tableView_Utilizadores.selectionModel().selectedRows()
        if not selecionados:
            QtWidgets.QMessageBox.warning(self, "Aviso", "Selecione um utilizador para eliminar!")
            return
        
        linha = selecionados[0].row()
        modelo = self.tableView_Utilizadores.model()
        id_utilizador = modelo.data(modelo.index(linha, 0))
        nome_utilizador = modelo.data(modelo.index(linha, 2))
        
        # Não permitir eliminar o próprio utilizador
        if int(id_utilizador) == self.id_utilizador:
            QtWidgets.QMessageBox.warning(self, "Aviso", "Não pode eliminar o próprio utilizador!")
            return
        
        try:
            conn_BD = ligacao_BD()
            if conn_BD and conn_BD != -1:
                # Verificar se existem consultas ou receitas associadas
                cmd_sql = "SELECT COUNT(*) FROM consultas WHERE IdUtente = %s OR IdMedico = %s;"
                num_consultas = consultaUmValor(conn_BD, cmd_sql, (id_utilizador, id_utilizador))
                
                cmd_sql = "SELECT COUNT(*) FROM receitas WHERE IdUtente = %s;"
                num_receitas = consultaUmValor(conn_BD, cmd_sql, (id_utilizador,))
                
                if num_consultas > 0 or num_receitas > 0:
                    QtWidgets.QMessageBox.warning(self, "Aviso", f"Não é possível eliminar o utilizador '{nome_utilizador}' pois existem consultas ou receitas associadas.")
                    conn_BD.close()
                    return
                
                resposta = QtWidgets.QMessageBox.question(
                    self, "Confirmação", 
                    f"Tem certeza que deseja eliminar o utilizador '{nome_utilizador}'?"
                )
                
                if resposta == QtWidgets.QMessageBox.Yes:
                    cmd_sql = "DELETE FROM utilizador WHERE Id = %s;"
                    resultado = operacao_DML(conn_BD, cmd_sql, (id_utilizador,))
                    
                    if resultado > 0:
                        QtWidgets.QMessageBox.information(self, "Sucesso", "Utilizador eliminado com sucesso!")
                        self.listar_utilizadores()
                    else:
                        QtWidgets.QMessageBox.warning(self, "Aviso", "Não foi possível eliminar o utilizador.")
                
                conn_BD.close()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao eliminar utilizador: {e}")
    
    def limpar_filtro(self):
        self.lineEdit_Filtro.clear()
        self.comboBox_Cargo.setCurrentIndex(0)
        self.listar_utilizadores()
    
    def atualizar_relogio(self):
        """Atualiza o LCD com a hora atual"""
        hora_atual = QtCore.QTime.currentTime().toString("HH:mm")
        if hasattr(self, 'RelogioLCD'):
            self.RelogioLCD.display(hora_atual)

    def sair(self):
        from form_Login import FormLogin
        self.close()
        self.janela_login = FormLogin()
        self.janela_login.show()
