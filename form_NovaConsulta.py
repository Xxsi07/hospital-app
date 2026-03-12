# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore
from interfaces.formNovaConsulta import Ui_Dialog_NovaConsulta
from base_dados import ligacao_BD, listagem_BD, operacao_DML


class FormNovaConsulta(QtWidgets.QDialog, Ui_Dialog_NovaConsulta):
    consulta_marcada = QtCore.pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.id_medico = None
        self.lista_utentes = {}  # Dicionário: nome -> id
        
        # Conectar botões
        self.pushButton_Guardar.clicked.connect(self.guardar_consulta)
        self.pushButton_Cancelar.clicked.connect(self.close)
        
        # Configurar data mínima (hoje)
        self.dateEdit_Data.setDate(QtCore.QDate.currentDate())
        self.dateEdit_Data.setMinimumDate(QtCore.QDate.currentDate())
        
        # Configurar hora
        self.timeEdit_Hora.setTime(QtCore.QTime(9, 0))
        
        # Configurar combobox de utentes para pesquisa
        self.comboBox_Utente.setEditable(True)
        self.comboBox_Utente.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox_Utente.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        self.comboBox_Utente.completer().setFilterMode(QtCore.Qt.MatchContains)
    
    def inicializar(self, id_medico):
        """Inicializa o formulário com o ID do médico logado"""
        self.id_medico = id_medico
        self.carregar_utentes()
        self.carregar_tipos_consulta()
    
    def carregar_utentes(self):
        """Carrega a lista de utentes no combobox"""
        try:
            conn_BD = ligacao_BD()
            if conn_BD and conn_BD != -1:
                # Cargo de utente = 2
                cmd_sql = "SELECT Id, Nome FROM utilizador WHERE Cargos = 2 ORDER BY Nome;"
                resultados = listagem_BD(conn_BD, cmd_sql)
                
                self.comboBox_Utente.clear()
                self.lista_utentes = {}  # Dicionário: nome -> id
                
                if resultados and resultados != -1:
                    for utente in resultados:
                        self.lista_utentes[utente[1]] = utente[0]
                        self.comboBox_Utente.addItem(utente[1])
                
                conn_BD.close()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao carregar utentes: {e}")
    
    def carregar_tipos_consulta(self):
        """Carrega os tipos de consulta disponíveis"""
        tipos = [
            "Consulta Geral",
            "Consulta de Rotina",
            "Consulta de Urgência",
            "Consulta de Especialidade",
            "Consulta de Acompanhamento",
            "Primeira Consulta",
            "Consulta de Retorno"
        ]
        
        self.comboBox_TipoConsulta.clear()
        for tipo in tipos:
            self.comboBox_TipoConsulta.addItem(tipo)
    
    def guardar_consulta(self):
        """Guarda a nova consulta na base de dados"""
        # Validações
        nome_utente = self.comboBox_Utente.currentText().strip()
        
        if not nome_utente or nome_utente not in self.lista_utentes:
            QtWidgets.QMessageBox.warning(self, "Aviso", "Por favor, selecione um utente válido da lista.")
            return
        
        if self.comboBox_TipoConsulta.currentIndex() < 0:
            QtWidgets.QMessageBox.warning(self, "Aviso", "Por favor, selecione o tipo de consulta.")
            return
        
        # Obter dados
        id_utente = self.lista_utentes[nome_utente]
        data = self.dateEdit_Data.date().toString("yyyy-MM-dd")
        hora = self.timeEdit_Hora.time().toString("HH:mm:ss")
        tipo_consulta = self.comboBox_TipoConsulta.currentText()
        observacoes = self.textEdit_Observacoes.toPlainText().strip()
        
        # Verificar se já existe consulta no mesmo horário para o médico
        try:
            conn_BD = ligacao_BD()
            if conn_BD and conn_BD != -1:
                cmd_verificar = """
                    SELECT COUNT(*) FROM consultas 
                    WHERE IdMedico = %s AND Data = %s AND Hora = %s AND Estado != 'Cancelada';
                """
                cursor = conn_BD.cursor()
                cursor.execute(cmd_verificar, (self.id_medico, data, hora))
                resultado = cursor.fetchone()
                
                if resultado and resultado[0] > 0:
                    QtWidgets.QMessageBox.warning(
                        self, "Aviso", 
                        "Já existe uma consulta marcada para este horário!"
                    )
                    conn_BD.close()
                    return
                
                # Inserir nova consulta
                cmd_sql = """
                    INSERT INTO consultas (Data, Hora, IdUtente, IdMedico, TipoConsulta, Estado, Observacoes)
                    VALUES (%s, %s, %s, %s, %s, 'Marcada', %s);
                """
                resultado = operacao_DML(conn_BD, cmd_sql, (data, hora, id_utente, self.id_medico, tipo_consulta, observacoes if observacoes else None))
                
                if resultado > 0:
                    QtWidgets.QMessageBox.information(self, "Sucesso", "Consulta marcada com sucesso!")
                    self.consulta_marcada.emit()
                    self.close()
                else:
                    QtWidgets.QMessageBox.warning(self, "Aviso", "Não foi possível marcar a consulta.")
                
                conn_BD.close()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao marcar consulta: {e}")
