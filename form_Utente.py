from PyQt5 import QtWidgets, QtGui, QtCore
from interfaces.formUtente import Ui_MainWindow
from base_dados import ligacao_BD, listagem_BD
import datetime

class FormUtente(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, id_utilizador=-1, nome_utilizador="Utente", parent=None):
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
        
        # Ligar o botão de receitas
        if hasattr(self, 'pushButton_Receitas'):
            self.pushButton_Receitas.clicked.connect(self.ver_receitas_ativas)
        
        # Ligar o botão de logout
        if hasattr(self, 'pushButton_Logout'):
            self.pushButton_Logout.clicked.connect(self.logout)
        
        self.carregar_consultas("hoje")
    
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
    
    def ver_receitas_ativas(self):
        from form_ReceitasUtente import FormReceitasUtente
        self.form_receitas = FormReceitasUtente(self, self.id_utilizador)
        self.form_receitas.show()
        
    def carregar_consultas(self, tipo_filtro):
        conn = ligacao_BD()
        if conn != -1:
            sql = f"""
                SELECT c.Data, c.Hora, u.Nome AS 'Nome Médico', c.TipoConsulta, c.Estado, c.Observacoes
                FROM consultas c
                JOIN utilizador u ON c.IdMedico = u.Id
                WHERE c.IdUtente = {self.id_utilizador}
            """
            
            hoje = datetime.date.today().strftime("%Y-%m-%d")
            
            if tipo_filtro == "hoje":
                sql += f" AND c.Data = '{hoje}'"
                self.label_Consultas.setText("Consultas de Hoje:")
            elif tipo_filtro == "todas":
                self.label_Consultas.setText("Todas as Consultas:")
                
            sql += " ORDER BY c.Data DESC, c.Hora ASC"
                
            resultados = listagem_BD(conn, sql)
            
            self.modelo_consultas = QtGui.QStandardItemModel(len(resultados) if resultados else 0, 6)
            self.modelo_consultas.setHorizontalHeaderLabels(["Data", "Hora", "Médico", "Tipo", "Estado", "Observações"])
            
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
