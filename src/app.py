from mimetypes import init
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic
import requests


class app():
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.cantina = uic.loadUi("tela_cantina.ui")
        self.cantina.pushButton.clicked.connect(self.adicionar_produto)

        self.cantina.show()
        self.app.exec()
    def adicionar_produto(self):
        self.nome_produto = self.cantina.lineEdit.text()
        self.preço = self.cantina.lineEdit_2.text()
        self.quantidade = self.cantina.lineEdit_3.text()
        ulr = "http://localhost:8040/produto/add"
        resposta = {
            "Nome": self.nome_produto,
            "Preço": self.preço,
            "Quantidade": self.quantidade
        }
        requests.post(url=ulr, json=resposta)
        self.cantina.lineEdit.clear()
        self.cantina.lineEdit_2.clear()
        self.cantina.lineEdit_3.clear()
        QMessageBox.warning(self.cantina,"aviso", "Produto adicionado com sucesso")





app()
        


