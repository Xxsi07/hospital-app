from PyQt5 import QtWidgets
from interfaces.formNovaReceita import Ui_FormNovaReceita
from form_AdicionarMedicamento import FormAdicionarMedicamento
from base_dados import ligacao_BD, operacao_DML, consultaUmValor

class FormNovaReceita(QtWidgets.QMainWindow, Ui_FormNovaReceita):
    def __init__(self, form_medicos):
        super().__init__()
        self.setupUi(self)
        
        self.form_medicos = form_medicos
        self.medicamentos = [] # Lista em memória com os medicamentos a adicionar

        self.pushButton_Cancelar.clicked.connect(self.cancelar)
        self.pushButton_AdicionarMedicamento.clicked.connect(self.abrir_adicionar_medicamento)
        self.pushButton_Gravar.clicked.connect(self.gravar_receita)

        self.configurar_tabela()

    def inicializar_novo(self, id_utente, id_consulta):
        self.lineEdit_IdUtente.setText(str(id_utente))
        self.lineEdit_IdConsulta.setText(str(id_consulta))
        self.medicamentos.clear()
        self.tableWidget_Medicamentos.setRowCount(0)

    def configurar_tabela(self):
        self.tableWidget_Medicamentos.setColumnCount(5)
        self.tableWidget_Medicamentos.setHorizontalHeaderLabels(
            ["Medicamento", "Data Início", "Data Fim", "Observações", "ID"]
        )

    def abrir_adicionar_medicamento(self):
        self.form_adicionar = FormAdicionarMedicamento(self)
        self.form_adicionar.show()

    def adicionar_medicamento_lista(self, id_med, nome, dt_inicio, dt_fim, obs):
        self.medicamentos.append({
            'id': id_med,
            'nome': nome,
            'data_inicioc': dt_inicio,
            'data_fim': dt_fim,
            'observacoes': obs
        })
        self.atualizar_tabela()

    def atualizar_tabela(self):
        self.tableWidget_Medicamentos.setRowCount(0)
        for i, med in enumerate(self.medicamentos):
            self.tableWidget_Medicamentos.insertRow(i)
            self.tableWidget_Medicamentos.setItem(i, 0, QtWidgets.QTableWidgetItem(med['nome']))
            self.tableWidget_Medicamentos.setItem(i, 1, QtWidgets.QTableWidgetItem(med['data_inicioc']))
            self.tableWidget_Medicamentos.setItem(i, 2, QtWidgets.QTableWidgetItem(med['data_fim']))
            self.tableWidget_Medicamentos.setItem(i, 3, QtWidgets.QTableWidgetItem(med['observacoes']))
            self.tableWidget_Medicamentos.setItem(i, 4, QtWidgets.QTableWidgetItem(str(med['id'])))

    def gravar_receita(self):
        try:
            id_utente = self.lineEdit_IdUtente.text()
            id_consulta = self.lineEdit_IdConsulta.text()

            if len(self.medicamentos) == 0:
                QtWidgets.QMessageBox.warning(self, "Aviso", "A receita deve ter pelo menos um medicamento.")
                return

            conn_BD = ligacao_BD()
            if not conn_BD:
                QtWidgets.QMessageBox.critical(self, "Erro", "A ligação à BD não está estabelecida.")
                return

            # INSERIR a Receita Master (Mestre)
            cmd_sql_receita = "INSERT INTO receitas(IdUtente, IdConsulta) VALUES (%s, %s);"
            res = operacao_DML(conn_BD, cmd_sql_receita, (id_utente, id_consulta))
            if res == -1:
                QtWidgets.QMessageBox.critical(self, "Erro", "Ocorreu um erro ao inserir a receita principal.")
                return
            
            # Obter o último ID Inserido
            cmd_sql_last_id = "SELECT LAST_INSERT_ID();"
            id_receita_gerada = consultaUmValor(conn_BD, cmd_sql_last_id)
            if id_receita_gerada == -1:
                 QtWidgets.QMessageBox.critical(self, "Erro", "Deu erro ao obter ID gerado da nova receita.")
                 return
            
            # INSERIR os Medicamentos na tabela de Detalhe
            for med in self.medicamentos:
                cmd_sql_linha = "INSERT INTO receitas_medicamentos(IdReceita, IdMedicamento, Observacoes, DataInicio, DataFim) VALUES (%s, %s, %s, %s, %s);"
                res_linha = operacao_DML(conn_BD, cmd_sql_linha, (
                    id_receita_gerada, 
                    med['id'], 
                    med['observacoes'], 
                    med['data_inicioc'], 
                    med['data_fim']
                ))

            conn_BD.close()
            QtWidgets.QMessageBox.information(self, "Sucesso", "Receita gerada e medicamentos inseridos com sucesso!")
            self.close()

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Erro", f"Erro: {e}")

    def cancelar(self):
        self.close()
