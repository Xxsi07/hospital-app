from PyQt5 import QtWidgets, QtGui, QtCore
from interfaces.formReceitasUtente import Ui_Form_ReceitasUtente
from base_dados import ligacao_BD, listagem_BD
import datetime


class FormReceitasUtente(QtWidgets.QMainWindow, Ui_Form_ReceitasUtente):
    def __init__(self, form_utente, id_utente):
        super().__init__()
        self.setupUi(self)
        
        self.form_utente = form_utente
        self.id_utente = id_utente
        
        # Configurar timer para atualizar data/hora
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.atualizar_data_hora)
        self.timer.start(1000)  # Atualiza a cada segundo
        self.atualizar_data_hora()
        
        self.pushButton_Voltar.clicked.connect(self.voltar)
        
        self.carregar_receitas_ativas()
    
    def atualizar_data_hora(self):
        agora = datetime.datetime.now()
        self.label_DataHora.setText(f"Data/Hora Atual: {agora.strftime('%d/%m/%Y %H:%M:%S')}")
    
    def carregar_receitas_ativas(self):
        try:
            conn_BD = ligacao_BD()
            if conn_BD and conn_BD != -1:
                # Obter data e hora atual do PC
                agora = datetime.datetime.now()
                data_atual = agora.strftime("%Y-%m-%d")
                
                cmd_sql = f"""
                    SELECT r.Id AS 'Receita', m.Nome AS 'Medicamento', rm.Observacoes, 
                           rm.DataInicio AS 'Data Início', rm.DataFim AS 'Data Fim', 
                           c.Data AS 'Data Consulta', c.TipoConsulta AS 'Tipo Consulta',
                           med.Nome AS 'Médico'
                    FROM receitas r
                    JOIN receitas_medicamentos rm ON r.Id = rm.IdReceita
                    JOIN medicamentos m ON rm.IdMedicamento = m.Id
                    JOIN consultas c ON r.IdConsulta = c.Id
                    JOIN utilizador med ON c.IdMedico = med.Id
                    WHERE r.IdUtente = {self.id_utente}
                      AND rm.DataInicio <= '{data_atual}'
                      AND (rm.DataFim IS NULL OR rm.DataFim >= '{data_atual}')
                    ORDER BY r.Id, rm.DataInicio DESC;
                """
                dados = listagem_BD(conn_BD, cmd_sql)
                
                if dados == -1:
                    dados = []
                
                modelo = QtGui.QStandardItemModel(len(dados), 8)
                modelo.setHorizontalHeaderLabels(["Receita", "Medicamento", "Observações", "Data Início", "Data Fim", "Data Consulta", "Tipo Consulta", "Médico"])
                
                for row_idx, row_data in enumerate(dados):
                    for col_idx, col_data in enumerate(row_data):
                        item = QtGui.QStandardItem(str(col_data) if col_data else "")
                        modelo.setItem(row_idx, col_idx, item)
                
                self.tableView_Receitas.setModel(modelo)
                self.tableView_Receitas.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
                self.tableView_Receitas.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                self.tableView_Receitas.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
                self.tableView_Receitas.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
                
                conn_BD.close()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao carregar receitas: {e}")
    
    def voltar(self):
        self.timer.stop()
        self.close()
        self.form_utente.show()
