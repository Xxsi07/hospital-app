from PyQt5 import QtWidgets, QtGui
from interfaces.formReceitasConsulta import Ui_Form_ReceitasConsulta
from base_dados import ligacao_BD, listagem_BD, operacao_DML


class FormReceitasConsulta(QtWidgets.QMainWindow, Ui_Form_ReceitasConsulta):
    def __init__(self, form_medicos, id_consulta, info_consulta=""):
        super().__init__()
        self.setupUi(self)
        
        self.form_medicos = form_medicos
        self.id_consulta = id_consulta
        
        self.label_InfoConsulta.setText(f"Consulta: {info_consulta}")
        
        self.pushButton_Voltar.clicked.connect(self.voltar)
        self.pushButton_Eliminar.clicked.connect(self.eliminar_medicamento)
        
        self.carregar_receitas()
    
    def carregar_receitas(self):
        try:
            conn_BD = ligacao_BD()
            if conn_BD and conn_BD != -1:
                cmd_sql = f"""
                    SELECT rm.Id, r.Id AS 'ID Receita', m.Nome AS 'Medicamento', rm.Observacoes, 
                           rm.DataInicio AS 'Data Início', rm.DataFim AS 'Data Fim'
                    FROM receitas r
                    JOIN receitas_medicamentos rm ON r.Id = rm.IdReceita
                    JOIN medicamentos m ON rm.IdMedicamento = m.Id
                    WHERE r.IdConsulta = {self.id_consulta}
                    ORDER BY r.Id, rm.DataInicio DESC;
                """
                dados = listagem_BD(conn_BD, cmd_sql)
                
                if dados == -1:
                    dados = []
                
                self.modelo = QtGui.QStandardItemModel(len(dados), 6)
                self.modelo.setHorizontalHeaderLabels(["ID", "Receita", "Medicamento", "Observações", "Data Início", "Data Fim"])
                
                for row_idx, row_data in enumerate(dados):
                    for col_idx, col_data in enumerate(row_data):
                        item = QtGui.QStandardItem(str(col_data) if col_data else "")
                        self.modelo.setItem(row_idx, col_idx, item)
                
                self.tableView_Receitas.setModel(self.modelo)
                self.tableView_Receitas.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
                self.tableView_Receitas.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                self.tableView_Receitas.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
                self.tableView_Receitas.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
                
                # Esconder coluna do ID do medicamento na receita
                self.tableView_Receitas.setColumnHidden(0, True)
                
                conn_BD.close()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao carregar receitas: {e}")
    
    def eliminar_medicamento(self):
        selecionados = self.tableView_Receitas.selectionModel().selectedRows()
        if not selecionados:
            QtWidgets.QMessageBox.warning(self, "Aviso", "Selecione um medicamento para eliminar!")
            return
        
        linha = selecionados[0].row()
        id_receita_med = self.modelo.data(self.modelo.index(linha, 0))
        nome_medicamento = self.modelo.data(self.modelo.index(linha, 2))
        
        resposta = QtWidgets.QMessageBox.question(
            self, "Confirmação", 
            f"Tem certeza que deseja eliminar o medicamento '{nome_medicamento}' desta receita?"
        )
        
        if resposta == QtWidgets.QMessageBox.Yes:
            try:
                conn_BD = ligacao_BD()
                if conn_BD and conn_BD != -1:
                    cmd_sql = "DELETE FROM receitas_medicamentos WHERE Id = %s;"
                    resultado = operacao_DML(conn_BD, cmd_sql, (id_receita_med,))
                    
                    if resultado > 0:
                        QtWidgets.QMessageBox.information(self, "Sucesso", "Medicamento eliminado com sucesso!")
                        self.carregar_receitas()
                    else:
                        QtWidgets.QMessageBox.warning(self, "Aviso", "Não foi possível eliminar o medicamento.")
                    
                    conn_BD.close()
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao eliminar medicamento: {e}")
    
    def voltar(self):
        self.close()
        self.form_medicos.show()
