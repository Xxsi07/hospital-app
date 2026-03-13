from PyQt5 import QtWidgets, QtGui, QtCore
from interfaces.formAdministrador import Ui_MainWindow_Administrador
from base_dados import ligacao_BD, listagem_BD, consultaUmValor, operacao_DML
from form_DetalheUtilizador import FormDetalheUtilizador


class FormAdministrador(QtWidgets.QMainWindow, Ui_MainWindow_Administrador):
    def __init__(self, id_utilizador=-1, nome_utilizador="Administrador", parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.id_utilizador = id_utilizador
        self.modo_atual = "utilizadores"
        
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
        self.pushButton_Novo.clicked.connect(self.acao_novo)
        self.pushButton_Editar.clicked.connect(self.acao_editar)
        self.pushButton_Eliminar.clicked.connect(self.acao_eliminar)
        self.pushButton_EliminarConsultas.clicked.connect(self.eliminar_consultas_utilizador)
        self.pushButton_Medicamentos.clicked.connect(self.alternar_modo_dados)
        self.pushButton_Filtrar.clicked.connect(self.aplicar_filtro)
        self.pushButton_Limpar.clicked.connect(self.limpar_filtro)
        self.pushButton_Sair.clicked.connect(self.sair)
        self.lineEdit_Filtro.returnPressed.connect(self.aplicar_filtro)
        
        # Carregar utilizadores
        self.listar_utilizadores()

    def aplicar_filtro(self):
        if self.modo_atual == "utilizadores":
            self.listar_utilizadores()
        else:
            self.listar_medicamentos()

    def alternar_modo_dados(self):
        if self.modo_atual == "utilizadores":
            self.modo_atual = "medicamentos"
            self.pushButton_Medicamentos.setText("Utilizadores")
            self.label_Utilizadores.setText("Gestão de Medicamentos:")
            self.pushButton_EliminarConsultas.setVisible(False)
            self.comboBox_Cargo.setVisible(False)
            self.lineEdit_Filtro.setPlaceholderText("Filtrar por medicamento...")
            self.listar_medicamentos()
        else:
            self.modo_atual = "utilizadores"
            self.pushButton_Medicamentos.setText("Medicamentos")
            self.label_Utilizadores.setText("Gestão de Utilizadores:")
            self.pushButton_EliminarConsultas.setVisible(True)
            self.comboBox_Cargo.setVisible(True)
            self.lineEdit_Filtro.setPlaceholderText("Filtrar por nome...")
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

    def listar_medicamentos(self):
        try:
            conn_BD = ligacao_BD()
            if conn_BD and conn_BD != -1:
                filtro_nome = self.lineEdit_Filtro.text().strip()

                cmd_sql = """
                    SELECT Id, Nome, Descricao
                    FROM medicamentos
                    WHERE 1=1
                """

                if filtro_nome:
                    cmd_sql += f" AND Nome LIKE '%{filtro_nome}%'"

                cmd_sql += " ORDER BY Nome ASC;"

                dados = listagem_BD(conn_BD, cmd_sql)

                if dados == -1:
                    dados = []

                modelo = QtGui.QStandardItemModel()
                modelo.setHorizontalHeaderLabels(["ID", "Nome", "Descrição"])

                for linha in dados:
                    modelo.appendRow([QtGui.QStandardItem(str(celula) if celula else "") for celula in linha])

                self.tableView_Utilizadores.setModel(modelo)
                self.tableView_Utilizadores.resizeColumnsToContents()
                self.tableView_Utilizadores.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
                self.tableView_Utilizadores.setSelectionMode(QtWidgets.QTableView.SingleSelection)
                self.tableView_Utilizadores.setEditTriggers(QtWidgets.QTableView.NoEditTriggers)

                self.tableView_Utilizadores.setColumnHidden(0, True)

                conn_BD.close()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao listar medicamentos: {e}")

    def acao_novo(self):
        if self.modo_atual == "utilizadores":
            self.mostrar_form("novo")
        else:
            self.novo_medicamento()

    def acao_editar(self):
        if self.modo_atual == "utilizadores":
            self.mostrar_form("editar")
        else:
            self.editar_medicamento()

    def acao_eliminar(self):
        if self.modo_atual == "utilizadores":
            self.eliminar_utilizador()
        else:
            self.eliminar_medicamento()
    
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

    def eliminar_consultas_utilizador(self):
        selecionados = self.tableView_Utilizadores.selectionModel().selectedRows()
        if not selecionados:
            QtWidgets.QMessageBox.warning(self, "Aviso", "Selecione um utilizador para eliminar as consultas!")
            return

        linha = selecionados[0].row()
        modelo = self.tableView_Utilizadores.model()
        id_utilizador = modelo.data(modelo.index(linha, 0))
        nome_utilizador = modelo.data(modelo.index(linha, 2))

        try:
            conn_BD = ligacao_BD()
            if conn_BD and conn_BD != -1:
                cmd_sql = "SELECT COUNT(*) FROM consultas WHERE IdUtente = %s OR IdMedico = %s;"
                num_consultas = consultaUmValor(conn_BD, cmd_sql, (id_utilizador, id_utilizador))

                if not num_consultas or num_consultas <= 0:
                    QtWidgets.QMessageBox.information(self, "Informação", f"O utilizador '{nome_utilizador}' não tem consultas atribuídas.")
                    conn_BD.close()
                    return

                resposta = QtWidgets.QMessageBox.question(
                    self,
                    "Confirmação",
                    f"Vai eliminar {num_consultas} consulta(s) atribuída(s) ao utilizador '{nome_utilizador}'.\n\nDeseja continuar?"
                )

                if resposta == QtWidgets.QMessageBox.Yes:
                    cmd_sql = "DELETE FROM consultas WHERE IdUtente = %s OR IdMedico = %s;"
                    resultado = operacao_DML(conn_BD, cmd_sql, (id_utilizador, id_utilizador))

                    if resultado > 0:
                        QtWidgets.QMessageBox.information(self, "Sucesso", f"Foram eliminadas {resultado} consulta(s) com sucesso!")
                    else:
                        QtWidgets.QMessageBox.warning(self, "Aviso", "Não foi possível eliminar as consultas do utilizador.")

                conn_BD.close()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao eliminar consultas: {e}")

    def obter_dados_medicamento(self, nome_inicial="", descricao_inicial=""):
        dialog = QtWidgets.QDialog(self)
        dialog.setWindowTitle("Medicamento")
        layout = QtWidgets.QFormLayout(dialog)

        line_nome = QtWidgets.QLineEdit()
        line_nome.setText(nome_inicial)
        text_descricao = QtWidgets.QPlainTextEdit()
        text_descricao.setPlainText(descricao_inicial)
        text_descricao.setMaximumHeight(90)

        layout.addRow("Nome:", line_nome)
        layout.addRow("Descrição:", text_descricao)

        botoes = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        botoes.accepted.connect(dialog.accept)
        botoes.rejected.connect(dialog.reject)
        layout.addRow(botoes)

        if dialog.exec_() != QtWidgets.QDialog.Accepted:
            return None, None

        nome = line_nome.text().strip()
        descricao = text_descricao.toPlainText().strip()

        return nome, descricao

    def novo_medicamento(self):
        nome, descricao = self.obter_dados_medicamento()
        if nome is None:
            return

        if not nome:
            QtWidgets.QMessageBox.warning(self, "Aviso", "O nome do medicamento é obrigatório!")
            return

        try:
            conn_BD = ligacao_BD()
            if conn_BD and conn_BD != -1:
                cmd_sql = "SELECT COUNT(*) FROM medicamentos WHERE Nome = %s;"
                existe = consultaUmValor(conn_BD, cmd_sql, (nome,))

                if existe and existe > 0:
                    QtWidgets.QMessageBox.warning(self, "Aviso", "Já existe um medicamento com esse nome!")
                    conn_BD.close()
                    return

                cmd_sql = "INSERT INTO medicamentos (Nome, Descricao) VALUES (%s, %s);"
                resultado = operacao_DML(conn_BD, cmd_sql, (nome, descricao if descricao else None))

                if resultado > 0:
                    QtWidgets.QMessageBox.information(self, "Sucesso", "Medicamento adicionado com sucesso!")
                    self.listar_medicamentos()
                else:
                    QtWidgets.QMessageBox.warning(self, "Aviso", "Não foi possível adicionar o medicamento.")

                conn_BD.close()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao adicionar medicamento: {e}")

    def editar_medicamento(self):
        selecionados = self.tableView_Utilizadores.selectionModel().selectedRows()
        if not selecionados:
            QtWidgets.QMessageBox.warning(self, "Aviso", "Selecione um medicamento para editar!")
            return

        linha = selecionados[0].row()
        modelo = self.tableView_Utilizadores.model()
        id_medicamento = modelo.data(modelo.index(linha, 0))
        nome_atual = modelo.data(modelo.index(linha, 1))
        descricao_atual = modelo.data(modelo.index(linha, 2))

        nome, descricao = self.obter_dados_medicamento(nome_atual or "", descricao_atual or "")
        if nome is None:
            return

        if not nome:
            QtWidgets.QMessageBox.warning(self, "Aviso", "O nome do medicamento é obrigatório!")
            return

        try:
            conn_BD = ligacao_BD()
            if conn_BD and conn_BD != -1:
                cmd_sql = "SELECT COUNT(*) FROM medicamentos WHERE Nome = %s AND Id != %s;"
                existe = consultaUmValor(conn_BD, cmd_sql, (nome, id_medicamento))

                if existe and existe > 0:
                    QtWidgets.QMessageBox.warning(self, "Aviso", "Já existe outro medicamento com esse nome!")
                    conn_BD.close()
                    return

                cmd_sql = "UPDATE medicamentos SET Nome = %s, Descricao = %s WHERE Id = %s;"
                resultado = operacao_DML(conn_BD, cmd_sql, (nome, descricao if descricao else None, id_medicamento))

                if resultado > 0:
                    QtWidgets.QMessageBox.information(self, "Sucesso", "Medicamento alterado com sucesso!")
                    self.listar_medicamentos()
                else:
                    QtWidgets.QMessageBox.warning(self, "Aviso", "Não foi possível alterar o medicamento.")

                conn_BD.close()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao editar medicamento: {e}")

    def eliminar_medicamento(self):
        selecionados = self.tableView_Utilizadores.selectionModel().selectedRows()
        if not selecionados:
            QtWidgets.QMessageBox.warning(self, "Aviso", "Selecione um medicamento para eliminar!")
            return

        linha = selecionados[0].row()
        modelo = self.tableView_Utilizadores.model()
        id_medicamento = modelo.data(modelo.index(linha, 0))
        nome_medicamento = modelo.data(modelo.index(linha, 1))

        try:
            conn_BD = ligacao_BD()
            if conn_BD and conn_BD != -1:
                cmd_sql = "SELECT COUNT(*) FROM receitas_medicamentos WHERE IdMedicamento = %s;"
                em_uso = consultaUmValor(conn_BD, cmd_sql, (id_medicamento,))

                if em_uso and em_uso > 0:
                    QtWidgets.QMessageBox.warning(
                        self,
                        "Aviso",
                        f"Não é possível eliminar '{nome_medicamento}' porque está associado a receitas."
                    )
                    conn_BD.close()
                    return

                resposta = QtWidgets.QMessageBox.question(
                    self,
                    "Confirmação",
                    f"Tem certeza que deseja eliminar o medicamento '{nome_medicamento}'?"
                )

                if resposta == QtWidgets.QMessageBox.Yes:
                    cmd_sql = "DELETE FROM medicamentos WHERE Id = %s;"
                    resultado = operacao_DML(conn_BD, cmd_sql, (id_medicamento,))

                    if resultado > 0:
                        QtWidgets.QMessageBox.information(self, "Sucesso", "Medicamento eliminado com sucesso!")
                        self.listar_medicamentos()
                    else:
                        QtWidgets.QMessageBox.warning(self, "Aviso", "Não foi possível eliminar o medicamento.")

                conn_BD.close()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao eliminar medicamento: {e}")
    
    def limpar_filtro(self):
        self.lineEdit_Filtro.clear()
        if self.modo_atual == "utilizadores":
            self.comboBox_Cargo.setCurrentIndex(0)
            self.listar_utilizadores()
        else:
            self.listar_medicamentos()
    
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
