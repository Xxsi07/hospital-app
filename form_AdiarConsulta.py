from PyQt5 import QtWidgets, QtCore
from interfaces.formAdiarConsulta import Ui_FormAdiarConsulta
from base_dados import ligacao_BD, operacao_DML


class FormAdiarConsulta(QtWidgets.QMainWindow, Ui_FormAdiarConsulta):
    def __init__(self, form_medicos):
        super().__init__()
        self.setupUi(self)
        
        self.form_medicos = form_medicos
        self.id_consulta = None
        
        self.pushButton_Cancelar.clicked.connect(self.cancelar)
        self.pushButton_Aplicar.clicked.connect(self.aplicar)
    
    def inicializar(self, id_consulta, data_atual, hora_atual):
        self.id_consulta = id_consulta
        self.lineEdit_IdConsulta.setText(str(id_consulta))
        
        # Configurar data/hora atual
        data_hora_atual = QtCore.QDateTime.fromString(f"{data_atual} {hora_atual}", "yyyy-MM-dd HH:mm:ss")
        self.dateTimeEdit_DataAtual.setDateTime(data_hora_atual)
        
        # Configurar data/hora adiada (por defeito, amanhã à mesma hora)
        data_hora_adiada = data_hora_atual.addDays(1)
        self.dateTimeEdit_DataAdiada.setDateTime(data_hora_adiada)
        self.dateTimeEdit_DataAdiada.setMinimumDateTime(QtCore.QDateTime.currentDateTime())
    
    def aplicar(self):
        nova_data = self.dateTimeEdit_DataAdiada.date().toString("yyyy-MM-dd")
        nova_hora = self.dateTimeEdit_DataAdiada.time().toString("HH:mm:ss")
        
        # Verificar se a nova data é posterior à atual
        if self.dateTimeEdit_DataAdiada.dateTime() <= QtCore.QDateTime.currentDateTime():
            QtWidgets.QMessageBox.warning(self, "Aviso", "A nova data deve ser posterior à data/hora atual!")
            return
        
        try:
            conn_BD = ligacao_BD()
            if conn_BD and conn_BD != -1:
                cmd_sql = "UPDATE consultas SET Data = %s, Hora = %s, Estado = 'Adiada' WHERE Id = %s;"
                resultado = operacao_DML(conn_BD, cmd_sql, (nova_data, nova_hora, self.id_consulta))
                
                if resultado > 0:
                    QtWidgets.QMessageBox.information(self, "Sucesso", f"Consulta adiada para {nova_data} às {nova_hora}!")
                    self.close()
                    self.form_medicos.carregar_consultas("todas")
                else:
                    QtWidgets.QMessageBox.warning(self, "Aviso", "Não foi possível adiar a consulta.")
                
                conn_BD.close()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao adiar consulta: {e}")
    
    def cancelar(self):
        self.close()
