from PyQt5 import QtWidgets, QtGui, QtCore
from interfaces.formMedicos import Ui_MainWindow_Medicos
from base_dados import ligacao_BD, listagem_BD
import datetime

class FormMedicos(QtWidgets.QMainWindow, Ui_MainWindow_Medicos):
    def __init__(self, id_utilizador=-1, nome_utilizador="Médico", parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.id_utilizador = id_utilizador
        
        # Coloca o nome do utilizador na label
        self.label_NomeUtilizador.setText(f"Bem vindo {nome_utilizador}")
        self.label_NomeUtilizador.adjustSize() # Garante que o texto não fica cortado
        
        self.pushButton_ConsultasHoje.clicked.connect(lambda: self.carregar_consultas("hoje"))
        self.pushButton_TodasConsultas.clicked.connect(lambda: self.carregar_consultas("todas"))
        
        if hasattr(self, 'dateTimeEdit_Consultas1') and hasattr(self, 'dateTimeEdit_Consultas2'):
            self.dateTimeEdit_Consultas1.dateChanged.connect(lambda: self.carregar_consultas("data"))
            self.dateTimeEdit_Consultas2.dateChanged.connect(lambda: self.carregar_consultas("data"))
            hoje = QtCore.QDate.currentDate()
            self.dateTimeEdit_Consultas1.setDate(hoje)
            self.dateTimeEdit_Consultas2.setDate(hoje)

        self.carregar_consultas("hoje")
        
    def carregar_consultas(self, tipo_filtro):
        conn = ligacao_BD()
        if conn != -1:
            sql = f"""
                SELECT c.Data, c.Hora, u.Nome AS 'Nome Utente', c.TipoConsulta, c.Estado, c.Observacoes
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
            
            self.modelo_consultas = QtGui.QStandardItemModel(len(resultados) if resultados else 0, 6)
            self.modelo_consultas.setHorizontalHeaderLabels(["Data", "Hora", "Utente", "Tipo", "Estado", "Observações"])
            
            if resultados:
                for row_idx, row_data in enumerate(resultados):
                    for col_idx, col_data in enumerate(row_data):
                        item = QtGui.QStandardItem(str(col_data))
                        self.modelo_consultas.setItem(row_idx, col_idx, item)
            
            self.tableView_Consultas.setModel(self.modelo_consultas)
            self.tableView_Consultas.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            self.tableView_Consultas.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        
    def sair(self):
        self.close()
