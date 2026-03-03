from PyQt5 import QtWidgets
import sys
from form_Login import FormLogin

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    janela = FormLogin()
    janela.show()
    sys.exit(app.exec_())
