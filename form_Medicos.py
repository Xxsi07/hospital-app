from PyQt5 import QtWidgets, QtGui, QtCore
from interfaces.formMedicos import Ui_MainWindow_Medicos
from base_dados import ligacao_BD, listagem_BD, operacao_DML, consultaUmValor
import datetime

class FormMedicos(QtWidgets.QMainWindow, Ui_MainWindow_Medicos):
    def __init__(self, id_utilizador=-1, nome_utilizador="Médico", parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.id_utilizador = id_utilizador
        
        # Coloca o nome do utilizador na label
        self.label_NomeUtilizador.setText(f"Bem vindo {nome_utilizador}")
        self.label_NomeUtilizador.adjustSize() # Garante que o texto não fica cortado
        
        # Configurar relógio em tempo real
        self.timer_relogio = QtCore.QTimer(self)
        self.timer_relogio.timeout.connect(self.atualizar_relogio)
        self.timer_relogio.start(1000)  # Atualiza a cada 1 segundo
        self.atualizar_relogio()  # Chama imediatamente para mostrar a hora
        
        self.pushButton_ConsultasHoje.clicked.connect(lambda: self.carregar_consultas("hoje"))
        self.pushButton_TodasConsultas.clicked.connect(lambda: self.carregar_consultas("todas"))
        
        if hasattr(self, 'dateTimeEdit_Consultas1') and hasattr(self, 'dateTimeEdit_Consultas2'):
            self.dateTimeEdit_Consultas1.dateChanged.connect(lambda: self.carregar_consultas("data"))
            self.dateTimeEdit_Consultas2.dateChanged.connect(lambda: self.carregar_consultas("data"))
            hoje = QtCore.QDate.currentDate()
            self.dateTimeEdit_Consultas1.setDate(hoje)
            self.dateTimeEdit_Consultas2.setDate(hoje)

        self.carregar_consultas("hoje")

        # Ligar o botão à função de nova receita
        if hasattr(self, 'pushButton_NovaReceita'):
            self.pushButton_NovaReceita.clicked.connect(self.abrir_nova_receita)
        
        # Ligar o botão de ver receitas da consulta
        if hasattr(self, 'pushButton_Receitas'):
            self.pushButton_Receitas.clicked.connect(self.ver_receitas_consulta)
        
        # Ligar o botão de logout
        if hasattr(self, 'pushButton_Logout'):
            self.pushButton_Logout.clicked.connect(self.logout)
        
        # Ligar botões de gestão de consultas
        if hasattr(self, 'pushButton_ConcluirConsulta'):
            self.pushButton_ConcluirConsulta.clicked.connect(self.concluir_consulta)
        
        if hasattr(self, 'pushButton_AdiarConsulta'):
            self.pushButton_AdiarConsulta.clicked.connect(self.adiar_consulta)
        
        if hasattr(self, 'pushButton_RemoverConsulta'):
            self.pushButton_RemoverConsulta.clicked.connect(self.cancelar_consulta)
        
        # Ligar botão de nova consulta
        if hasattr(self, 'pushButton_NovaConsulta'):
            self.pushButton_NovaConsulta.clicked.connect(self.abrir_nova_consulta)

    def abrir_nova_consulta(self):
        """Abre o formulário para marcar uma nova consulta"""
        from form_NovaConsulta import FormNovaConsulta
        self.form_nova_consulta = FormNovaConsulta(self)
        self.form_nova_consulta.inicializar(self.id_utilizador)
        self.form_nova_consulta.consulta_marcada.connect(lambda: self.carregar_consultas("todas"))
        self.form_nova_consulta.show()

    def concluir_consulta(self):
        indexes = self.tableView_Consultas.selectionModel().selectedRows()
        if not indexes:
            QtWidgets.QMessageBox.warning(self, "Aviso", "Por favor, selecione uma consulta na tabela primeiro.")
            return
        
        row = indexes[0].row()
        id_consulta = self.modelo_consultas.index(row, 0).data()
        estado_atual = self.modelo_consultas.index(row, 6).data()
        
        if estado_atual == "Concluída":
            QtWidgets.QMessageBox.warning(self, "Aviso", "Esta consulta já está concluída!")
            return
        
        resposta = QtWidgets.QMessageBox.question(
            self, "Confirmação", 
            "Tem certeza que deseja marcar esta consulta como concluída?"
        )
        
        if resposta == QtWidgets.QMessageBox.Yes:
            try:
                conn_BD = ligacao_BD()
                if conn_BD and conn_BD != -1:
                    cmd_sql = "UPDATE consultas SET Estado = 'Concluída' WHERE Id = %s;"
                    resultado = operacao_DML(conn_BD, cmd_sql, (id_consulta,))
                    
                    if resultado > 0:
                        QtWidgets.QMessageBox.information(self, "Sucesso", "Consulta concluída com sucesso!")
                        self.carregar_consultas("todas")
                    else:
                        QtWidgets.QMessageBox.warning(self, "Aviso", "Não foi possível concluir a consulta.")
                    
                    conn_BD.close()
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao concluir consulta: {e}")
    
    def adiar_consulta(self):
        indexes = self.tableView_Consultas.selectionModel().selectedRows()
        if not indexes:
            QtWidgets.QMessageBox.warning(self, "Aviso", "Por favor, selecione uma consulta na tabela primeiro.")
            return
        
        row = indexes[0].row()
        id_consulta = self.modelo_consultas.index(row, 0).data()
        data_consulta = self.modelo_consultas.index(row, 2).data()
        hora_consulta = self.modelo_consultas.index(row, 3).data()
        estado_atual = self.modelo_consultas.index(row, 6).data()
        
        if estado_atual == "Concluída":
            QtWidgets.QMessageBox.warning(self, "Aviso", "Não é possível adiar uma consulta concluída!")
            return
        
        from form_AdiarConsulta import FormAdiarConsulta
        self.form_adiar = FormAdiarConsulta(self)
        self.form_adiar.inicializar(id_consulta, data_consulta, hora_consulta)
        self.form_adiar.show()
    
    def cancelar_consulta(self):
        indexes = self.tableView_Consultas.selectionModel().selectedRows()
        if not indexes:
            QtWidgets.QMessageBox.warning(self, "Aviso", "Por favor, selecione uma consulta na tabela primeiro.")
            return
        
        row = indexes[0].row()
        id_consulta = self.modelo_consultas.index(row, 0).data()
        nome_utente = self.modelo_consultas.index(row, 4).data()
        data_consulta = self.modelo_consultas.index(row, 2).data()
        
        # Verificar se existem receitas associadas
        try:
            conn_BD = ligacao_BD()
            if conn_BD and conn_BD != -1:
                cmd_sql = "SELECT COUNT(*) FROM receitas WHERE IdConsulta = %s;"
                num_receitas = consultaUmValor(conn_BD, cmd_sql, (id_consulta,))
                
                if num_receitas and num_receitas > 0:
                    QtWidgets.QMessageBox.warning(self, "Aviso", "Não é possível cancelar esta consulta pois existem receitas associadas!")
                    conn_BD.close()
                    return
                
                conn_BD.close()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao verificar receitas: {e}")
            return
        
        resposta = QtWidgets.QMessageBox.question(
            self, "Confirmação", 
            f"Tem certeza que deseja cancelar a consulta de {nome_utente} em {data_consulta}?\n\nEsta ação não pode ser desfeita!"
        )
        
        if resposta == QtWidgets.QMessageBox.Yes:
            try:
                conn_BD = ligacao_BD()
                if conn_BD and conn_BD != -1:
                    cmd_sql = "DELETE FROM consultas WHERE Id = %s;"
                    resultado = operacao_DML(conn_BD, cmd_sql, (id_consulta,))
                    
                    if resultado > 0:
                        QtWidgets.QMessageBox.information(self, "Sucesso", "Consulta cancelada com sucesso!")
                        self.carregar_consultas("todas")
                    else:
                        QtWidgets.QMessageBox.warning(self, "Aviso", "Não foi possível cancelar a consulta.")
                    
                    conn_BD.close()
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao cancelar consulta: {e}")

    def atualizar_relogio(self):
        """Atualiza o LCD com a hora atual"""
        hora_atual = QtCore.QTime.currentTime().toString("HH:mm")
        if hasattr(self, 'RelogioLCD'):
            self.RelogioLCD.display(hora_atual)

    def logout(self):
        from form_Login import FormLogin
        self.close()
        self.janela_login = FormLogin()
        self.janela_login.show()

    def ver_receitas_consulta(self):
        indexes = self.tableView_Consultas.selectionModel().selectedRows()
        if not indexes:
            QtWidgets.QMessageBox.warning(self, "Aviso", "Por favor, selecione uma consulta na tabela primeiro.")
            return
        
        row = indexes[0].row()
        id_consulta = self.modelo_consultas.index(row, 0).data()
        data_consulta = self.modelo_consultas.index(row, 2).data()
        nome_utente = self.modelo_consultas.index(row, 4).data()
        tipo_consulta = self.modelo_consultas.index(row, 5).data()
        
        info_consulta = f"{nome_utente} - {tipo_consulta} ({data_consulta})"
        
        from form_ReceitasConsulta import FormReceitasConsulta
        self.form_receitas = FormReceitasConsulta(self, id_consulta, info_consulta)
        self.form_receitas.show()

    def abrir_nova_receita(self):
        indexes = self.tableView_Consultas.selectionModel().selectedRows()
        if not indexes:
            QtWidgets.QMessageBox.warning(self, "Aviso", "Por favor, selecione uma consulta na tabela primeiro.")
            return
            
        row = indexes[0].row()
        id_consulta = self.modelo_consultas.index(row, 0).data()
        id_utente = self.modelo_consultas.index(row, 1).data()
        
        from form_NovaReceita import FormNovaReceita
        self.form_receita = FormNovaReceita(self)
        self.form_receita.inicializar_novo(id_utente, id_consulta)
        self.form_receita.show()

    def carregar_consultas(self, tipo_filtro):
        conn = ligacao_BD()
        if conn != -1:
            sql = f"""
                SELECT c.Id, c.IdUtente, c.Data, c.Hora, u.Nome AS 'Nome Utente', c.TipoConsulta, c.Estado, c.Observacoes
                FROM consultas c
                JOIN utilizador u ON c.IdUtente = u.Id
                WHERE c.IdMedico = {self.id_utilizador}
            """
            
            hoje = datetime.date.today().strftime("%Y-%m-%d")
            
            if tipo_filtro == "hoje":
                sql += f" AND c.Data = '{hoje}'"
                self.label_Consultas.setText("Consultas de Hoje:")
            elif tipo_filtro == "data":
                data1 = self.dateTimeEdit_Consultas1.date().toString("yyyy-MM-dd")
                data2 = self.dateTimeEdit_Consultas2.date().toString("yyyy-MM-dd")
                sql += f" AND c.Data BETWEEN '{data1}' AND '{data2}'"
                self.label_Consultas.setText("Consultas por Data:")
            elif tipo_filtro == "todas":
                self.label_Consultas.setText("Todas as Consultas:")
                
            sql += " ORDER BY c.Data DESC, c.Hora ASC"
                
            resultados = listagem_BD(conn, sql)
            
            self.modelo_consultas = QtGui.QStandardItemModel(len(resultados) if resultados else 0, 8)
            self.modelo_consultas.setHorizontalHeaderLabels(["ID", "IdUtente", "Data", "Hora", "Utente", "Tipo", "Estado", "Observações"])

            if resultados:
                for row_idx, row_data in enumerate(resultados):
                    for col_idx, col_data in enumerate(row_data):
                        item = QtGui.QStandardItem(str(col_data))
                        self.modelo_consultas.setItem(row_idx, col_idx, item)

            self.tableView_Consultas.setModel(self.modelo_consultas)
            self.tableView_Consultas.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            self.tableView_Consultas.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            
            # Esconder as colunas dos IDs
            self.tableView_Consultas.setColumnHidden(0, True)
            self.tableView_Consultas.setColumnHidden(1, True)
            
            # Permitir apenas a seleção de linhas inteiras para as receitas
            self.tableView_Consultas.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
            self.tableView_Consultas.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        
    def sair(self):
        self.close()
