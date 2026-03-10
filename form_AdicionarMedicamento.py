from PyQt5 import QtWidgets, QtCore
from interfaces.formAdicionarMedicamento import Ui_FormAdicionarMedicamento
from base_dados import ligacao_BD, listagem_BD

class FormAdicionarMedicamento(QtWidgets.QMainWindow, Ui_FormAdicionarMedicamento):
    def __init__(self, form_nova_receita):
        super().__init__()
        self.setupUi(self)
        self.form_nova_receita = form_nova_receita

        # Preencher a combobox com os medicamentos da base de dados
        self.carregar_medicamentos()

        self.pushButton_Cancelar.clicked.connect(self.cancelar)
        self.pushButton_Adicionar.clicked.connect(self.adicionar)

        # Configurar datas padrao
        self.dateEdit_DataInicio.setDate(QtCore.QDate.currentDate())
        self.dateEdit_DataFim.setDate(QtCore.QDate.currentDate().addDays(7))

    def carregar_medicamentos(self):
        conn_BD = ligacao_BD()
        if not conn_BD:
            QtWidgets.QMessageBox.critical(self, "Erro", "A ligaçao a BD não está estabelecida")
            return
        
        cmd_sql = "SELECT Id, Nome FROM medicamentos"
        resultados = listagem_BD(conn_BD, cmd_sql)
        self.comboBox_Medicamentos.clear()
        
        if resultados != -1:
            for id_medicamento, nome in resultados:
                # Armazenar o objeto ID associado ao texto
                self.comboBox_Medicamentos.addItem(nome, userData=id_medicamento)
        
        conn_BD.close()

    def adicionar(self):
        # Obter os dados selecionados
        index = self.comboBox_Medicamentos.currentIndex()
        if index < 0:
            QtWidgets.QMessageBox.warning(self, "Aviso", "Selecione um medicamento válido!")
            return
        
        id_medicamento = self.comboBox_Medicamentos.itemData(index)
        nome_medicamento = self.comboBox_Medicamentos.itemText(index)
        data_inicio = self.dateEdit_DataInicio.date().toString("yyyy-MM-dd")
        data_fim = self.dateEdit_DataFim.date().toString("yyyy-MM-dd")
        observacoes = self.plainTextEdit_Observacoes.toPlainText()

        # Enviar de volta para a tabela em FormNovaReceita
        self.form_nova_receita.adicionar_medicamento_lista(id_medicamento, nome_medicamento, data_inicio, data_fim, observacoes)
        
        self.close()

    def cancelar(self):
        self.close()
