from ast import Delete, Try
from audioop import add
from cProfile import label
import enum
import re
from itertools import count
from classes.produtos.deletar_produto import del_prod
from classes.clientes.listar_clientes import listarClientes
from classes.clientes.adicionar_cliente import add_cliente
import icons.iconesCant2 as iconesCant2
from mimetypes import init
from turtle import width
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic
from PyQt5.QtCore import QPropertyAnimation, QPoint,QSize
import requests
import icons.iconesCant as iconesCant
from classes.produtos.adicionar_produto import add_prod
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from classes.produtos.listar_produtos import listar
from classes.produtos.pesquisar_produto import pesquisa
from classes.produtos.deletar_produto import del_prod
from classes.produtos.atualizar_produto import att_prod
from classes.clientes.adicionar_cliente import add_cliente
from classes.clientes.listar_clientes import listarClientes
from classes.clientes.atualizar_cliente import att_cliente
from classes.clientes.deletar_cliente import deletar_cli
from classes.clientes.pesquisar_cliente import pesquisarcliente
from classes.carrinho.Add_prod_cart import adicionar_Prod_cart
from classes.carrinho.Listar_prod_cart import listar_produto_cart
from classes.carrinho.Dele_prod_cart import dele_produto_cart
from classes.carrinho.Att_prod_cart import att_produto_cart
from classes.carrinho.id_produtos_cart import Id_produtos_cart
from classes.carrinho.efetuarvenda import EfetuarVenda
from classes.carrinho.deletarallcart import deletar_tudo
from classes.relatorios.jan import RelatorioJan
from classes.relatorios.nov import RelatorioNov
from classes.relatorios.abril import RelatorioAbril
from classes.relatorios.fev import RelatorioFev
from classes.relatorios.marc import RelatorioMarc
from classes.relatorios.maio import RelatorioMaio
from classes.relatorios.jun import RelatorioJunho
from classes.relatorios.jul import RelatorioJul
from classes.relatorios.agos import RelatorioAgosto
from classes.relatorios.set import RelatorioSetembro
from classes.relatorios.outu import RelatorioOut

from datetime import date
from classes.relatorios.dezem import RelatorioDez
counter = 0
ano = 0
receita = 0
class app():
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.cantina = uic.loadUi("./telas/tela_cantina.ui")
        self.carrega = uic.loadUi("./telas/tela_carregamento.ui")
        effect = QGraphicsDropShadowEffect(
        offset=QPoint(3, 3), blurRadius=25, color=QColor("#111")
        )
        effect2 = QGraphicsDropShadowEffect(
        offset=QPoint(3, 3), blurRadius=25, color=QColor("#111")
        )
        effect3 = QGraphicsDropShadowEffect(
        offset=QPoint(3, 3), blurRadius=25, color=QColor("#111")
        )
        effect4 = QGraphicsDropShadowEffect(
        offset=QPoint(3, 3), blurRadius=25, color=QColor("#111")
        )
        effect5 = QGraphicsDropShadowEffect(
        offset=QPoint(3, 3), blurRadius=25, color=QColor("#111")
        )
        effect6 = QGraphicsDropShadowEffect(
        offset=QPoint(3, 3), blurRadius=25, color=QColor("#111")
        )
        effect7 = QGraphicsDropShadowEffect(
        offset=QPoint(3, 3), blurRadius=25, color=QColor("#111")
        )
        effect8 = QGraphicsDropShadowEffect(
        offset=QPoint(3, 3), blurRadius=25, color=QColor("#111")
        )
        effect9 = QGraphicsDropShadowEffect(
        offset=QPoint(3, 3), blurRadius=25, color=QColor("#111")
        )
        effect10 = QGraphicsDropShadowEffect(
        offset=QPoint(3, 3), blurRadius=25, color=QColor("#111")
        )
        effect11 = QGraphicsDropShadowEffect(
        offset=QPoint(3, 3), blurRadius=25, color=QColor("#111")
        )
        effect12 = QGraphicsDropShadowEffect(
        offset=QPoint(3, 3), blurRadius=25, color=QColor("#111")
        )
        effect13 = QGraphicsDropShadowEffect(
        offset=QPoint(3, 3), blurRadius=25, color=QColor("#111")
        )
        effect14 = QGraphicsDropShadowEffect(
        offset=QPoint(3, 3), blurRadius=25, color=QColor("#111")
        )
        effect15 = QGraphicsDropShadowEffect(
        offset=QPoint(3, 3), blurRadius=25, color=QColor("#111")
        )
        self.cantina.frame_14.hide()
        self.cantina.frame_15.hide()
        self.cantina.pushButton_21.clicked.connect(self.adicionar_produto)
        self.cantina.pushButton_23.clicked.connect(self.cancelar)
        self.cantina.pushButton_20.clicked.connect(self.enviar_produto)
        self.cantina.pushButton.setGraphicsEffect(effect3)
        self.cantina.pushButton_56.setGraphicsEffect(effect13)
        self.cantina.pushButton_57.setGraphicsEffect(effect14)
        self.cantina.pushButton_58.setGraphicsEffect(effect15)
        self.cantina.pushButton_19.setGraphicsEffect(effect2)
        self.cantina.pushButton_21.setGraphicsEffect(effect)
        self.cantina.pushButton_23.setGraphicsEffect(effect5)
        self.cantina.pushButton_20.setGraphicsEffect(effect4)
        self.cantina.pushButton_34.setGraphicsEffect(effect6)
        self.cantina.pushButton_35.setGraphicsEffect(effect7)
        self.cantina.pushButton_52.setGraphicsEffect(effect8)
        self.cantina.pushButton_53.setGraphicsEffect(effect9)
        self.cantina.pushButton_54.setGraphicsEffect(effect10)
        self.cantina.pushButton_25.setGraphicsEffect(effect11)
        self.cantina.pushButton_26.setGraphicsEffect(effect12)
        
        self.cantina.pushButton_2.clicked.connect(lambda:self.anima(100, True))
        self.cantina.pushButton_3.clicked.connect(lambda:self.anima2(100, True))
        self.cantina.pushButton_18.clicked.connect(self.relatorio_janerio)
        self.cantina.pushButton_4.clicked.connect(lambda:self.anima3(100, True))
        self.cantina.pushButton_5.clicked.connect(lambda:self.anima4(100, True))
        self.cantina.pushButton_24.clicked.connect(self.fechar_tela_cadastro)
        self.cantina.pushButton_22.clicked.connect(self.pesquisa)
        self.cantina.pushButton_19.clicked.connect(self.deletar)
        self.cantina.pushButton.clicked.connect(self.atualizar)
        self.cantina.pushButton_36.clicked.connect(self.sair_atualizar)
        self.cantina.pushButton_35.clicked.connect(self.sair_atualizar)
        self.cantina.pushButton_34.clicked.connect(self.enviar_dados_atualizados)
        self.cantina.tableWidget_6.setColumnWidth(0,100)
        self.cantina.tableWidget_6.setColumnWidth(1,150)
        self.cantina.tableWidget_6.setColumnWidth(2,150)
        self.cantina.tableWidget_7.setColumnWidth(0,100)
        self.cantina.tableWidget_7.setColumnWidth(1,150)
        self.cantina.tableWidget_7.setColumnWidth(2,150)
        self.cantina.pushButton_54.clicked.connect(self.adicionar_cliente)
        self.cantina.pushButton_27.clicked.connect(self.sair_tela_cliente)
        self.cantina.pushButton_25.clicked.connect(self.adicionar_clienti)
        self.cantina.pushButton_52.clicked.connect(self.atualizar_cliente)
        self.cantina.pushButton_26.clicked.connect(self.sair_tela_cliente)
        self.cantina.pushButton_53.clicked.connect(self.deletarcliennte)
        self.cantina.pushButton_55.clicked.connect(self.pesqClietu)
        self.cantina.pushButton_59.clicked.connect(self.add_prod_cart)
        self.cantina.pushButton_57.clicked.connect(self.dele_prod_cart)
        self.cantina.pushButton_56.clicked.connect(self.atualizar_prod_cart)
        self.cantina.pushButton_58.clicked.connect(self.pegar_id_produtos_cart)
        self.cantina.pushButton_18.clicked.connect(self.Relatorios)
        self.cantina.pushButton_6.clicked.connect(self.tabela_jan)
        self.cantina.pushButton_7.clicked.connect(self.tabela_fev)
        self.cantina.pushButton_8.clicked.connect(self.tabela_marc)
        self.cantina.pushButton_9.clicked.connect(self.tabela_abril)
        self.cantina.pushButton_10.clicked.connect(self.tabela_maio)
        self.cantina.pushButton_11.clicked.connect(self.tabela_jun)
        self.cantina.pushButton_12.clicked.connect(self.tabela_jul)
        self.cantina.pushButton_13.clicked.connect(self.tabela_ago)
        self.cantina.pushButton_14.clicked.connect(self.tabela_set)
        self.cantina.pushButton_15.clicked.connect(self.tabela_out)
        self.cantina.pushButton_16.clicked.connect(self.tabela_nov)
        self.cantina.pushButton_17.clicked.connect(self.tabela_dez)
        self.cantina.frame_17.hide()
        self.listar_clientees()
        self.listar_prod_cart()
        self.load_scree()
        self.carrega.show()
        self.app.exec()
    def dele_prod_cart(self):
        linha = self.cantina.tableWidget_7.currentRow()
        if linha == -1:
            return QMessageBox.information(self.cantina, "aviso", "selecione um produto do carrinho antes de excluir")
        id = self.cantina.tableWidget_7.item(linha, 0).text()
        d = dele_produto_cart()
        d.delete(id)
        self.cantina.tableWidget_7.setCurrentCell(-1,-1)
        self.cantina.tableWidget_7.removeRow(linha)
       
        return QMessageBox.information(self.cantina,"aviso","Produto deletado do carrinho")
    def add_prod_cart(self):
        self.nomeProd = self.cantina.lineEdit_17.text()
        self.Quantidade = self.cantina.spinBox_2.value()
        if self.nomeProd == '' or self.Quantidade == 0:
            return QMessageBox.warning(self.cantina, "Erro", "Preencha os campos corretamente")
        a = adicionar_Prod_cart()
        a.add(self.nomeProd,self.Quantidade)  
        self.listar_prod_cart()
        self.cantina.lineEdit_17.clear()
        self.cantina.spinBox_2.setValue(0)
       
    #produtos
    def listar_prod_cart(self):
        l = listar_produto_cart()
        l.listar()
        lista = l.dados.json()
        keys = "id", "Nome", "Quantidade"
        self.cantina.tableWidget_7.setColumnCount(3)
        self.cantina.tableWidget_7.setRowCount(len(lista))
        for c in range(len(lista)):
            for i, k in enumerate(keys):
                self.cantina.tableWidget_7.setItem(c,i,QtWidgets.QTableWidgetItem(str(lista[c][k])))
    def atualizar_prod_cart(self):
        linha = self.cantina.tableWidget_7.currentRow()
        if linha == -1:
            return QMessageBox.information(self.cantina, "aviso", "selecione um  produto do carrinho antes de atualizar")
        l = listar_produto_cart()
        l.listar()
        lista = l.dados.json()
        for c in range(len(lista)):
            id = self.cantina.tableWidget_7.item(c, 0).text()
            nome = self.cantina.tableWidget_7.item(c,1).text()
            Quantidade = self.cantina.tableWidget_7.item(c,2).text()
            l = att_produto_cart()
            l.atualizar(id, nome, Quantidade)
        self.listar_prod_cart()
        self.cantina.tableWidget_7.setCurrentCell(-1,-1)
        return QMessageBox.information(self.cantina, "aviso", "produto do carrinho atualizado")

    def pegar_id_produtos_cart(self):
        mensagem =  QtWidgets.QMessageBox()
        mensagem.setIcon(QtWidgets.QMessageBox.Question)
        mensagem.setWindowTitle("Adicionar")
        mensagem.setText("Deseja realmente efetuar a venda?")
        mensagem.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        botaosim = mensagem.button(QtWidgets.QMessageBox.Yes)
        botaosim.setText("Sim")
        botaonao = mensagem.button(QtWidgets.QMessageBox.No)
        botaonao.setText("Não")
        mensagem.exec()
        if mensagem.clickedButton() == botaonao:
           return mensagem.close()
        l = listar_produto_cart()
        l.listar()
        dados = l.dados.json()
        produtos = []
        for c in range(len(dados)):
            nome = dados[c]['Nome']
            i = Id_produtos_cart()
            i.id_prod(nome)
            id =i.dados.json()['id']
            quantidade = dados[c]['Quantidade']
            produtos.append(id)
            produtos.append(quantidade)
        venda_data = {
            'produtos':[

            ]
        }
        for c in range (0, len(produtos), 2):
            venda_data["produtos"].append({"idProduto":produtos[c], 'quantidade':produtos[c+1]})
        e = EfetuarVenda()
        e.venda(venda_data)
        print(e.resp.json())
        d = deletar_tudo()
        d.deletar()
        l = listar_produto_cart()
        l.listar()
        lista = l.dados.json()
        keys = "id", "Nome", "Quantidade"
        self.cantina.tableWidget_7.setColumnCount(3)
        self.cantina.tableWidget_7.setRowCount(len(lista))
        for c in range(len(lista)):
            for i, k in enumerate(keys):
                self.cantina.tableWidget_7.setItem(c,i,QtWidgets.QTableWidgetItem(str(lista[c][k])))
        return QMessageBox.about(self.cantina, "aviso",f"valor da venda: {e.resp.json()['lucrototal']}R$")
        

       

        
    
        
            
            
    def deletar(self):
            linha = self.cantina.tableWidget_2.currentRow()
            
            if linha == -1:
                 return QMessageBox.about(self.cantina,"aviso","selecione um produto antes de deletar")
            id = self.cantina.tableWidget_2.item(linha,0).text()
            print(linha)
            
            
            
            
            d = del_prod()
            d.dele(id)
            l = listar()
            l.listando() 
            self.cantina.tableWidget_2.removeRow(linha)
            self.cantina.tableWidget_2.setCurrentCell(-1,-1)
            
       
            
            return QMessageBox.about(self.cantina,"aviso","produto deletado com sucesso")
             
    def adicionar_cliente(self):
        self.cantina.frame_3.show()
        self.cantina.frame_2.hide()
        self.cantina.frame_8.show()
        self.cantina.frame_11.show()
        self.cantina.frame_10.show()
        self.cantina.frame_14.show()
        self.cantina.frame_17.show()
    def sair_tela_cliente(self):
        self.cantina.frame_17.hide()
        self.cantina.frame_14.hide()
        self.cantina.frame_2.show()
        c = listarClientes()
        c.listarCli()
        listaaa = c.dados
        keys = "id", "Nome","Numero"
        self.cantina.tableWidget_6.setRowCount(len(listaaa))
        self.cantina.tableWidget_6.setColumnCount(3)
        for x in range(len(listaaa)):
            for i, k in enumerate(keys):
                self.cantina.tableWidget_6.setItem(x,i, QtWidgets.QTableWidgetItem(str(listaaa[x][k])))
    def deletarcliennte(self):
        linha = self.cantina.tableWidget_6.currentRow()
        if linha == -1:
            return QMessageBox.information(self.cantina, "aviso", "selecione um cliente antes de excluir")
        id = self.cantina.tableWidget_6.item(linha, 0).text()
        d = deletar_cli()
        d.del_cli(id)
        l = listarClientes()
        l.listarCli()
        self.cantina.tableWidget_6.setCurrentCell(-1, -1)
        self.cantina.tableWidget_6.removeRow(linha)
        return QMessageBox.about(self.cantina,"aviso","Cliente deletado com sucesso")


    def pesqClietu(self):
        try:
            self.campo_pesquisa2 = self.cantina.lineEdit_16.text()
            p = pesquisarcliente()
            p.pes_cli(self.campo_pesquisa2)
            dados = p.resp
            keys = "id", "Nome", "Telefone"
            self.cantina.tableWidget_6.setColumnCount(3)
            self.cantina.tableWidget_6.setRowCount(len(dados))
            for c in range(len(dados)):
                for i, k in enumerate(keys):
                    self.cantina.tableWidget_6.setItem(c,i,QtWidgets.QTableWidgetItem(str(dados[c][k])))
        except:
            return QMessageBox.warning(self.cantina,"aviso", "usuario não encontrado")

    def adicionar_clienti(self):
        self.nome_cliente = self.cantina.lineEdit_7.text()
        self.telefone = self.cantina.lineEdit_9.text()
        if self.nome_cliente == " " or self.telefone == " ":
            return QMessageBox.warning(self.cantina,"warning","informe os dados corretamente")
        try:
           a = add_cliente()
           a.Addcliente(self.nome_cliente,self.telefone)
           self.cantina.lineEdit_7.clear()
           self.cantina.lineEdit_9.clear()
           return QMessageBox.warning(self.cantina,"about","cliente cadastrado com sucesso")
        
        except:
            return QMessageBox.warning(self.cantina,"warning","informe os dados corretamente")
    def listar_clientees(self):
        c = listarClientes()
        c.listarCli()
        listaaa = c.dados
        keys = "id", "Nome","Numero"
        self.cantina.tableWidget_6.setRowCount(len(listaaa))
        self.cantina.tableWidget_6.setColumnCount(3)
        for x in range(len(listaaa)):
            for i, k in enumerate(keys):
                self.cantina.tableWidget_6.setItem(x,i, QtWidgets.QTableWidgetItem(str(listaaa[x][k])))
    def atualizar_cliente(self):
        linha = self.cantina.tableWidget_6.currentRow()
        if linha == -1:
              return QMessageBox.about(self.cantina,"aviso","selecione  um cliente antes de atualizar")
        c = listarClientes()
        c.listarCli()
        listaaa = c.dados
        for c in range(len(listaaa)):

            self.id_cliente = self.cantina.tableWidget_6.item(c,0).text()
            self.nome_cliente = self.cantina.tableWidget_6.item(c,1).text()
            self.telefone= self.cantina.tableWidget_6.item(c, 2).text()
            l = att_cliente()
            l.attcliente(self.id_cliente, self.nome_cliente, self.telefone)
        self.cantina.tableWidget_6.setCurrentCell(-1,-1)  
        return QMessageBox.about(self.cantina,"aviso", "cliente atualizado com sucesso")
         
            
    def atualizar(self):
        linha = self.cantina.tableWidget_2.currentRow()
        print(linha)   

 
        if linha == -1:
              return QMessageBox.about(self.cantina,"aviso","selecione um produto antes de atualizar")
        self.id = self.cantina.tableWidget_2.item(linha, 0).text()
        self.nome_prod = self.cantina.tableWidget_2.item(linha, 1).text()
        self.preço_prod = self.cantina.tableWidget_2.item(linha, 2).text()
        self.quant_prod = self.cantina.tableWidget_2.item(linha, 3).text()
        self.peso_prod = self.cantina.tableWidget_2.item(linha, 5).text()
        self.uni_med = self.cantina.tableWidget_2.item(linha,6).text()
        self.cat = self.cantina.tableWidget_2.item(linha, 7).text()
        self.valcomprtot = self.cantina.tableWidget_2.item(linha,8).text()
        self.cantina.frame_15.show()
        self.cantina.lineEdit_24.setText(self.nome_prod)
        self.cantina.lineEdit_25.setText(self.preço_prod)
        self.cantina.lineEdit_22.setText(self.peso_prod)
        self.cantina.lineEdit_23.setText(self.valcomprtot)
        self.cantina.spinBox_5.setValue(int(self.quant_prod))
        if(self.cat == "Comida"):
            self.cantina.comboBox_9.setItemText(0,self.cat )
            self.cantina.comboBox_9.setItemText(1,"Bebida")
        else:
              self.cantina.comboBox_9.setItemText(0,self.cat )
              self.cantina.comboBox_9.setItemText(1,"Comida")
        self.cantina.comboBox_10.setItemText(0,self.uni_med)
        self.cantina.frame_2.hide()
        self.cantina.tableWidget_2.setCurrentCell(-1,-1)
    def enviar_dados_atualizados(self):
        self.valcomprtota = self.cantina.lineEdit_23.text()
        self.quant_prode = self.cantina.spinBox_5.value()
        self.nomee_prod = self.cantina.lineEdit_24.text()
        self.preçoo_Prod = self.cantina.lineEdit_25.text()
        self.prode_cat = self.cantina.comboBox_9.currentText()
        self.prode_unimed = self.cantina.comboBox_10.currentText()
        self.prode_peso = self.cantina.lineEdit_22.text()
        self.valcomprunit= float(self.valcomprtota)/float(self.quant_prode)
        d = att_prod()
        d.atualizar(self.id,self.nomee_prod, self.preçoo_Prod, self.quant_prode, self.prode_peso, self.prode_unimed, self.prode_cat, self.valcomprtota, self.valcomprunit)
        s = listar()
        s.listando()
        listaa = s.produtos
        keys = 'id','Nome', 'Preço' , 'Quantidade', 'Data', 'Peso','UniMedida', 'Categoria','Preço_Compra_total', 'Preço_Compra_Unitario'
        self.cantina.tableWidget_2.setRowCount(len(listaa))
        self.cantina.tableWidget_2.setColumnCount(10)
        for c in range(len(listaa)):
            for i, n in enumerate(keys):
                self.cantina.tableWidget_2.setItem(c,i,QtWidgets.QTableWidgetItem(str(listaa[c][n])))
        self.cantina.spinBox_5.setValue(0)
        self.cantina.lineEdit_24.clear()
        self.cantina.lineEdit_22.clear()
        self.cantina.lineEdit_23.clear()
        self.cantina.lineEdit_25.clear()
        return QMessageBox.about(self.cantina, "aviso", "produto atualizado com sucesso")
        
       
    def sair_atualizar(self):
        self.cantina.frame_15.hide()
        self.cantina.frame_14.hide()
        self.cantina.frame_8.hide()
        self.cantina.frame_11.hide()
        self.cantina.frame_10.hide()
        self.cantina.frame_3.show()
        self.cantina.frame_2.show()
        

    
       

    def adicionar_produto(self):
        self.cantina.frame_3.show()
        self.cantina.frame_8.show()
        self.cantina.frame_11.show()
        self.cantina.frame_10.show()
        self.cantina.frame_14.show()
        self.cantina.frame_2.hide()
        
    #colocar logica desse metodo no arquivo adicionar_produto
    def enviar_produto(self):
        self.nome_produto = self.cantina.lineEdit_2.text()
        self.preço = self.cantina.lineEdit_5.text()
        self.quantidade = self.cantina.spinBox.value()
        self.peso = self.cantina.lineEdit_6.text()
        self.categoria = self.cantina.comboBox.currentText()
        self.uniMedida = self.cantina.comboBox_2.currentText()
        self.preço_compra_total = float(self.cantina.lineEdit_8.text())
        self.preço_compra_unitario = float(self.preço_compra_total)/self.quantidade
        if self.nome_produto == " " or self.preço == " " or self.quantidade == 0 or self.peso == 0:
            return QMessageBox.warning(self.cantina, "aviso", "preencha todos os campos")
        mensagem =  QtWidgets.QMessageBox()
        mensagem.setIcon(QtWidgets.QMessageBox.Question)
        mensagem.setWindowTitle("Adicionar")
        mensagem.setText("Deseja realmente adicionar o produto?")
        mensagem.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        botaosim = mensagem.button(QtWidgets.QMessageBox.Yes)
        botaosim.setText("Sim")
        botaonao = mensagem.button(QtWidgets.QMessageBox.No)
        botaonao.setText("Não")
        mensagem.exec() 
        self.preço = self.preço.replace(",", ".")
        self.peso = self.peso.replace(",", ".")
        if mensagem.clickedButton() == botaonao:
           return mensagem.close()
        
       
    
      
       

       #adiciona produto
      
        a = add_prod()
        a.adicionar(self.nome_produto, self.preço, self.quantidade, self.peso, self.uniMedida, self.categoria,self.preço_compra_total, self.preço_compra_unitario)
       
        self.cantina.spinBox.setValue(0)
        self.cantina.lineEdit_2.clear()
        self.cantina.lineEdit_5.clear()
        self.cantina.lineEdit_6.clear()
        self.cantina.lineEdit_8.clear()
        QMessageBox.warning(self.cantina,"aviso", "Produto adicionado com sucesso")
        l = listar()
        l.listando() 
        
        keys ='id','Nome', 'Preço' , 'Quantidade', 'Data', 'Peso','UniMedida', 'Categoria','Preço_Compra_total', 'Preço_Compra_Unitario'
        self.cantina.tableWidget_2.setRowCount(len(l.produtos))
        self.cantina.tableWidget_2.setColumnCount(10)
        for c in range(len(l.produtos)):
            for i, n in enumerate (keys):
                self.cantina.tableWidget_2.setItem(c, i, QtWidgets.QTableWidgetItem(str(l.produtos[c][n]))) 
    #Animações
    def anima(self, maxwidth, enable):
        width = self.cantina.label_2.width()
        width2 = self.cantina.label_3.width()
        width3 = self.cantina.label_4.width()
        width4  = self.cantina.label_5.width()
        
        maxExtend = 60
        standar = 0
        if width == 0:
            widthExtend = maxExtend
            self.cantina.label_2.setStyleSheet("background-color:  rgb(87, 142, 184);border-top-right-radius:15px; border-bottom-right-radius:15px;")
            
            
            self.cantina.pushButton_2.setStyleSheet("background-color:  rgb(87, 142, 184);Border: none; border-top-left-radius:15px; border-bottom-left-radius:15px;")
            
            
            
        else:
            widthExtend = standar
            self.cantina.label_2.setStyleSheet("background-color: rgb(110, 184, 236);")
            
            
            self.cantina.pushButton_2.setStyleSheet("background-color:  rgb(110, 184, 236);Border: none;")
            
        self.animation = QPropertyAnimation(self.cantina.label_2, b"minimumWidth")
        self.animation.setDuration(100)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtend)
        self.animation.start()

        lista = listar()
        lista.listando()
        lista_produtoss = lista.produtos
        keys ='id','Nome', 'Preço' , 'Quantidade', 'Data', 'Peso','UniMedida', 'Categoria','Preço_Compra_total', 'Preço_Compra_Unitario'
        self.cantina.tableWidget_2.setRowCount(len(lista_produtoss))
        self.cantina.tableWidget_2.setColumnCount(10)
        for c in range(len(lista_produtoss)):
            for i, n in enumerate (keys):
                self.cantina.tableWidget_2.setItem(c, i, QtWidgets.QTableWidgetItem(str(lista_produtoss[c][n]))) 
         
        
         

        self.cantina.frame_3.show()
        self.cantina.frame_8.hide()
        self.cantina.frame_11.hide()
        self.cantina.frame_10.hide()
        
        if width2 != 0:
            
            self.animation2 = QPropertyAnimation(self.cantina.label_3, b"minimumWidth")
            self.animation2.setDuration(100)
            self.animation2.setStartValue(width2)
            self.animation2.setEndValue(0)
            self.animation2.start()
            self.cantina.label_3.setStyleSheet("background-color: rgb(110, 184, 236);")
            
            
            self.cantina.pushButton_3.setStyleSheet("background-color:  rgb(110, 184, 236);Border: none;")
        if width3 != 0:
            self.animation2 = QPropertyAnimation(self.cantina.label_4, b"minimumWidth")
            self.animation2.setDuration(100)
            self.animation2.setStartValue(width3)
            self.animation2.setEndValue(0)
            self.animation2.start()
            self.cantina.label_4.setStyleSheet("background-color: rgb(110, 184, 236);")
            
            
            self.cantina.pushButton_4.setStyleSheet("background-color:  rgb(110, 184, 236);Border: none;")
        if width4 !=0:
            self.animation2 = QPropertyAnimation(self.cantina.label_5, b"minimumWidth")
            self.animation2.setDuration(100)
            self.animation2.setStartValue(width4)
            self.animation2.setEndValue(0)
            self.animation2.start()
            self.cantina.label_5.setStyleSheet("background-color: rgb(110, 184, 236);")
            
            
            self.cantina.pushButton_5.setStyleSheet("background-color:  rgb(110, 184, 236);Border: none;")


            

    def anima2(self, maxwidth, enable):
        width = self.cantina.label_2.width()
        width2 = self.cantina.label_3.width()
        width3 = self.cantina.label_4.width()
        width4  = self.cantina.label_5.width()
        
        maxextand = 60
        standar = 0
        if width2 ==0:
            widthextend = maxextand
            self.cantina.label_3.setStyleSheet("background-color:  rgb(87, 142, 184);border-top-right-radius:15px; border-bottom-right-radius:15px;")
            
            
            self.cantina.pushButton_3.setStyleSheet("background-color:  rgb(87, 142, 184);Border: none; border-top-left-radius:15px; border-bottom-left-radius:15px;")
        else:
            widthextend = standar
            self.cantina.label_3.setStyleSheet("background-color: rgb(110, 184, 236);")
            
            
            self.cantina.pushButton_3.setStyleSheet("background-color:  rgb(110, 184, 236);Border: none;")
            

        self.animation3 = QPropertyAnimation(self.cantina.label_3, b"minimumWidth")
        self.animation3.setDuration(100)
        self.animation3.setStartValue(width2)
        self.animation3.setEndValue(widthextend)
        self.animation3.start()
        self.cantina.frame_11.show()
        self.cantina.frame_10.show()
        self.cantina.frame_3.show()
        self.cantina.frame_8.show()
       
        
        if width != 0:
            
            self.animation2 = QPropertyAnimation(self.cantina.label_2, b"minimumWidth")
            self.animation2.setDuration(100)
            self.animation2.setStartValue(width)
            self.animation2.setEndValue(0)
            self.animation2.start()
            self.cantina.label_2.setStyleSheet("background-color: rgb(110, 184, 236);")
            
            
            self.cantina.pushButton_2.setStyleSheet("background-color:  rgb(110, 184, 236);Border: none;")
        if width3 != 0:
            self.animation2 = QPropertyAnimation(self.cantina.label_4, b"minimumWidth")
            self.animation2.setDuration(100)
            self.animation2.setStartValue(width3)
            self.animation2.setEndValue(0)
            self.animation2.start()
            self.cantina.label_4.setStyleSheet("background-color: rgb(110, 184, 236);")
            
            
            self.cantina.pushButton_4.setStyleSheet("background-color:  rgb(110, 184, 236);Border: none;")
        if width4 !=0:
            self.animation2 = QPropertyAnimation(self.cantina.label_5, b"minimumWidth")
            self.animation2.setDuration(100)
            self.animation2.setStartValue(width4)
            self.animation2.setEndValue(0)
            self.animation2.start()
            self.cantina.label_5.setStyleSheet("background-color: rgb(110, 184, 236);")
            
            
            self.cantina.pushButton_5.setStyleSheet("background-color:  rgb(110, 184, 236);Border: none;")
    def anima3(self, maxwidth, enable):
       width = self.cantina.label_2.width()
       width2 = self.cantina.label_3.width()
       width3 = self.cantina.label_4.width()
       width4  = self.cantina.label_5.width()
        
       maxextand = 50
       standar = 0
       if width3 ==0:
            widthextend = maxextand
            self.cantina.label_4.setStyleSheet("background-color:  rgb(87, 142, 184);border-top-right-radius:15px; border-bottom-right-radius:15px;")
            
            
            self.cantina.pushButton_4.setStyleSheet("background-color:  rgb(87, 142, 184);Border: none; border-top-left-radius:15px; border-bottom-left-radius:15px;")
       else:
            widthextend = standar
            self.cantina.label_4.setStyleSheet("background-color: rgb(110, 184, 236);")
            
            
            self.cantina.pushButton_4.setStyleSheet("background-color:  rgb(110, 184, 236);Border: none;")
            

       self.animation3 = QPropertyAnimation(self.cantina.label_4, b"minimumWidth")
       self.animation3.setDuration(100)
       self.animation3.setStartValue(width3)
       self.animation3.setEndValue(widthextend)
       self.animation3.start()
       self.cantina.frame_11.hide()
       self.cantina.frame_10.show()
       self.cantina.frame_3.show()
       self.cantina.frame_8.show()
       if width != 0:
            
         self.animation2 = QPropertyAnimation(self.cantina.label_2, b"minimumWidth")
         self.animation2.setDuration(100)
         self.animation2.setStartValue(width)
         self.animation2.setEndValue(0)
         self.animation2.start()
         self.cantina.label_2.setStyleSheet("background-color: rgb(110, 184, 236);")
            
            
         self.cantina.pushButton_2.setStyleSheet("background-color:  rgb(110, 184, 236);Border: none;")
       if width2 != 0:
            self.animation2 = QPropertyAnimation(self.cantina.label_3, b"minimumWidth")
            self.animation2.setDuration(100)
            self.animation2.setStartValue(width3)
            self.animation2.setEndValue(0)
            self.animation2.start()
            self.cantina.label_3.setStyleSheet("background-color: rgb(110, 184, 236);")
            
            
            self.cantina.pushButton_3.setStyleSheet("background-color:  rgb(110, 184, 236);Border: none;")
       if width4 !=0:
            self.animation2 = QPropertyAnimation(self.cantina.label_5, b"minimumWidth")
            self.animation2.setDuration(100)
            self.animation2.setStartValue(width4)
            self.animation2.setEndValue(0)
            self.animation2.start()
            self.cantina.label_5.setStyleSheet("background-color: rgb(110, 184, 236);")
            
            
            self.cantina.pushButton_5.setStyleSheet("background-color:  rgb(110, 184, 236);Border: none;")
    def anima4(self, maxextend, enable):
       width = self.cantina.label_2.width()
       width2 = self.cantina.label_3.width()
       width3 = self.cantina.label_4.width()
       width4  = self.cantina.label_5.width()
        
       maxextand = 70
       standar = 0
       if width4 ==0:
            widthextend = maxextand
            self.cantina.label_5.setStyleSheet("background-color:  rgb(87, 142, 184);border-top-right-radius:15px; border-bottom-right-radius:15px;")
            
            
            self.cantina.pushButton_5.setStyleSheet("background-color:  rgb(87, 142, 184);Border: none; border-top-left-radius:15px; border-bottom-left-radius:15px;")
       else:
            widthextend = standar
            self.cantina.label_5.setStyleSheet("background-color: rgb(110, 184, 236);")
            
            
            self.cantina.pushButton_5.setStyleSheet("background-color:  rgb(110, 184, 236);Border: none;")
            

       self.animation3 = QPropertyAnimation(self.cantina.label_5, b"minimumWidth")
       self.animation3.setDuration(100)
       self.animation3.setStartValue(width4)
       self.animation3.setEndValue(widthextend)
       self.animation3.start()
       self.cantina.frame_11.hide()
       self.cantina.frame_10.hide()
       self.cantina.frame_3.show()
       self.cantina.frame_8.show()
       if width != 0:
        
            
         self.animation2 = QPropertyAnimation(self.cantina.label_2, b"minimumWidth")
         self.animation2.setDuration(100)
         self.animation2.setStartValue(width)
         self.animation2.setEndValue(0)
         self.animation2.start()
         self.cantina.label_2.setStyleSheet("background-color: rgb(110, 184, 236);")
            
            
         self.cantina.pushButton_2.setStyleSheet("background-color:  rgb(110, 184, 236);Border: none;")
       if width2 != 0:
            self.animation2 = QPropertyAnimation(self.cantina.label_3, b"minimumWidth")
            self.animation2.setDuration(100)
            self.animation2.setStartValue(width3)
            self.animation2.setEndValue(0)
            self.animation2.start()
            self.cantina.label_3.setStyleSheet("background-color: rgb(110, 184, 236);")
            
            
            self.cantina.pushButton_3.setStyleSheet("background-color:  rgb(110, 184, 236);Border: none;")
       if width3 !=0:
            self.animation2 = QPropertyAnimation(self.cantina.label_4, b"minimumWidth")
            self.animation2.setDuration(100)
            self.animation2.setStartValue(width3)
            self.animation2.setEndValue(0)
            self.animation2.start()
            self.cantina.label_4.setStyleSheet("background-color: rgb(110, 184, 236);")
            
            
            self.cantina.pushButton_4.setStyleSheet("background-color:  rgb(110, 184, 236);Border: none;")
            
            
    def relatorio_janerio(self):
        pass
    def load_scree(self):
        #setando tempo de execução do carregamento da barra, no caso a barra ira carregar em 35 milissegundos
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)

        self.timer.start(35)

    def progress(self):
        #carregando a barra
        global counter
        self.carrega.progressBar.setValue(counter)

        if counter > 100:
            self.timer.stop()
            self.cantina.show()
            self.carrega.close()
        counter = counter + 5
    def fechar_tela_cadastro(self):
        self.cantina.frame_14.hide()
        self.cantina.frame_8.hide()
        self.cantina.frame_11.hide()
        self.cantina.frame_10.hide()
        self.cantina.frame_3.show()
        self.cantina.frame_2.show()
     
    def cancelar(self):
        self.cantina.frame_14.hide()
        self.cantina.frame_8.hide()
        self.cantina.frame_11.hide()
        self.cantina.frame_10.hide()
        self.cantina.frame_3.show()
        self.cantina.frame_2.show()
        
    def pesquisa(self):
        a = listar()
        a.listando()
        try:
            
            keys ='id','Nome', 'Preço' , 'Quantidade', 'Data', 'Peso','UniMedida', 'Categoria','Preço_Compra_total', 'Preço_Compra_Unitario'
            self.campo_pesquisa = self.cantina.lineEdit.text()
            if self.campo_pesquisa == "":
                self.cantina.tableWidget_2.setRowCount(len(a.produtos))
                self.cantina.tableWidget_2.setColumnCount(10)
                for c in range(len(a.produtos)):
                    for i,k in enumerate(keys):
                        self.cantina.tableWidget.setItem(c,i, QtWidgets.QTableWidgetItem(str(a.produtos[c][k])))
        
            peq = pesquisa()
            peq.pesquisar(self.campo_pesquisa)
            print(peq.dados.json())
            self.cantina.tableWidget_2.setRowCount(len(peq.dados.json()))
            self.cantina.tableWidget_2.setColumnCount(10)
            for c in range(len(peq.dados.json())):
                for i, k in enumerate(keys):
                    self.cantina.tableWidget_2.setItem(c,i,QtWidgets.QTableWidgetItem(str(peq.dados.json()[c][k])))
        except requests.exceptions.JSONDecodeError:
            return QMessageBox.warning(self.cantina,"aviso", "produto não encontrado")
        
    def Relatorios(self):
        ano = self.cantina.lineEdit_3.text()
        keys = "quantidade", "Preço", "data_venda", "nome", "lucro_do_produto"
        anoregex = re.findall(r'[0-9]{4}',ano)
        if anoregex == []:
            return QMessageBox.warning(self.cantina, 'Aviso', "informe um ano antes de gerar os relatórios")

        #janeiro
        jan = RelatorioJan()
        jan.rel(ano)
        receita = jan.resp['receita']
        self.cantina.tableWidget.setRowCount(len(jan.resp['dados']))
        self.cantina.tableWidget.setColumnCount(5)
        for c in range(len(jan.resp['dados'])):
                for i, k in enumerate(keys):
                    self.cantina.tableWidget.setItem(c, i, QtWidgets.QTableWidgetItem(str(jan.resp['dados'][c][k])))
        
        #novembro
        nov = RelatorioNov()
        nov.rel(ano)
        self.cantina.tableWidget_15.setRowCount(len(nov.resp['dados']))
        self.cantina.tableWidget_15.setColumnCount(5)
        for c in range(len(nov.resp['dados'])):
                for i, k in enumerate(keys):
                    self.cantina.tableWidget_15.setItem(c, i, QtWidgets.QTableWidgetItem(str(nov.resp['dados'][c][k])))
        #fevereiro
        fev = RelatorioFev()
        fev.rel(ano)
        self.cantina.tableWidget_3.setRowCount(len(fev.resp['dados']))
        self.cantina.tableWidget_3.setColumnCount(5)
        for c in range(len(fev.resp['dados'])):
                for i, k in enumerate(keys):
                    self.cantina.tableWidget_3.setItem(c, i, QtWidgets.QTableWidgetItem(str(fev.resp['dados'][c][k])))
        #março
        marc = RelatorioMarc()
        marc.rel(ano)     
        self.cantina.tableWidget_4.setRowCount(len(marc.resp['dados']))
        self.cantina.tableWidget_4.setColumnCount(5)
        for c in range(len(marc.resp['dados'])):
                for i, k in enumerate(keys):
                    self.cantina.tableWidget_4.setItem(c, i, QtWidgets.QTableWidgetItem(str(marc.resp['dados'][c][k]))) 
       
        #abril
        abril = RelatorioAbril()
        abril.rel(ano)
        self.cantina.tableWidget_8.setRowCount(len(abril.resp['dados']))
        self.cantina.tableWidget_8.setColumnCount(5)
        for c in range(len(abril.resp['dados'])):
                for i, k in enumerate(keys):
                    self.cantina.tableWidget_8.setItem(c, i, QtWidgets.QTableWidgetItem(str(abril.resp['dados'][c][k]))) 
        #maio
        maio = RelatorioMaio()
        maio.rel(ano)
        self.cantina.tableWidget_9.setRowCount(len(maio.resp['dados']))
        self.cantina.tableWidget_9.setColumnCount(5)
        for c in range(len(maio.resp['dados'])):
                for i, k in enumerate(keys):
                    self.cantina.tableWidget_9.setItem(c, i, QtWidgets.QTableWidgetItem(str(maio.resp['dados'][c][k]))) 
        #junho
        junho = RelatorioJunho()
        junho.rel(ano)
        self.cantina.tableWidget_10.setRowCount(len(junho.resp['dados']))
        self.cantina.tableWidget_10.setColumnCount(5)
        for c in range(len(junho.resp['dados'])):
                for i, k in enumerate(keys):
                    self.cantina.tableWidget_10.setItem(c, i, QtWidgets.QTableWidgetItem(str(junho.resp['dados'][c][k]))) 
        #julho
        julho = RelatorioJul()
        julho.rel(ano)
        self.cantina.tableWidget_11.setRowCount(len(julho.resp['dados']))
        self.cantina.tableWidget_11.setColumnCount(5)
        for c in range(len(julho.resp['dados'])):
                for i, k in enumerate(keys):
                    self.cantina.tableWidget_11.setItem(c, i, QtWidgets.QTableWidgetItem(str(julho.resp['dados'][c][k]))) 
        #agosto
        ago = RelatorioAgosto()
        ago.rel(ano)
        self.cantina.tableWidget_12.setRowCount(len(ago.resp['dados']))
        self.cantina.tableWidget_12.setColumnCount(5)
        for c in range(len(ago.resp['dados'])):
                for i, k in enumerate(keys):
                    self.cantina.tableWidget_12.setItem(c, i, QtWidgets.QTableWidgetItem(str(ago.resp['dados'][c][k]))) 
        #setembro
        setembro = RelatorioSetembro()
        setembro.rel(ano)
        self.cantina.tableWidget_13.setRowCount(len(setembro.resp['dados']))
        self.cantina.tableWidget_13.setColumnCount(5)
        for c in range(len(setembro.resp['dados'])):
                for i, k in enumerate(keys):
                    self.cantina.tableWidget_13.setItem(c, i, QtWidgets.QTableWidgetItem(str(setembro.resp['dados'][c][k]))) 
        #outubro
        out = RelatorioOut()
        out.rel(ano)
        self.cantina.tableWidget_14.setRowCount(len(out.resp['dados']))
        self.cantina.tableWidget_14.setColumnCount(5)
        for c in range(len(out.resp['dados'])):
                for i, k in enumerate(keys):
                    self.cantina.tableWidget_14.setItem(c, i, QtWidgets.QTableWidgetItem(str(out.resp['dados'][c][k]))) 
        
        
        #dezembro
        dez = RelatorioDez()
        dez.rel(ano)
        receita = dez.resp['receita']
        self.cantina.lineEdit_4.setText(receita)
        self.cantina.tableWidget_16.setRowCount(len(dez.resp['dados']))
        self.cantina.tableWidget_16.setColumnCount(5)
        for c in range(len(dez.resp['dados'])):
                for i, k in enumerate(keys):
                    self.cantina.tableWidget_16.setItem(c, i, QtWidgets.QTableWidgetItem(str(dez.resp['dados'][c][k])))

       
       
        
        #ABRE
        self.cantina.frame_30.show()
        self.cantina.frame_29.show()
        self.cantina.frame_28.show()
        self.cantina.frame_27.show()
        self.cantina.frame_24.show()
        self.cantina.frame_23.show()
        self.cantina.frame_22.show()
        self.cantina.frame_21.show()
        self.cantina.frame_20.show()
        self.cantina.frame_19.show()
        self.cantina.frame_18.show()
        self.cantina.frame_9.show()
           
  
    #nav relatorios
    def tabela_jan(self):
            ano = self.cantina.lineEdit_3.text()
            if not ano :
                return QMessageBox.about(self.cantina, "aviso", "informe uma data antes")
            self.cantina.frame_30.hide()
            self.cantina.frame_29.hide()
            self.cantina.frame_28.hide()
            self.cantina.frame_27.hide()
            self.cantina.frame_24.hide()
            self.cantina.frame_23.hide()
            self.cantina.frame_22.hide()
            self.cantina.frame_21.hide()
            self.cantina.frame_20.hide()
            self.cantina.frame_19.hide()
            self.cantina.frame_18.hide()
            self.cantina.frame_9.show()
           
            nov = RelatorioJan()
            nov.rel(ano)
            receita = nov.resp['receita']
            self.cantina.lineEdit_4.setText(receita)
    def tabela_fev(self):
            ano = self.cantina.lineEdit_3.text()
            if not ano :
                return QMessageBox.about(self.cantina, "aviso", "informe uma data antes")
            self.cantina.frame_30.hide()
            self.cantina.frame_29.hide()
            self.cantina.frame_28.hide()
            self.cantina.frame_27.hide()
            self.cantina.frame_24.hide()
            self.cantina.frame_23.hide()
            self.cantina.frame_22.hide()
            self.cantina.frame_21.hide()
            self.cantina.frame_20.hide()
            self.cantina.frame_19.hide()
            self.cantina.frame_18.show()
            self.cantina.frame_9.show()
            nov = RelatorioFev()
            nov.rel(ano)
            receita = nov.resp['receita']
            self.cantina.lineEdit_4.setText(receita)
    def tabela_marc(self):
            ano = self.cantina.lineEdit_3.text()
            if not ano :
                return QMessageBox.about(self.cantina, "aviso", "informe uma data antes")
            self.cantina.frame_30.hide()
            self.cantina.frame_29.hide()
            self.cantina.frame_28.hide()
            self.cantina.frame_27.hide()
            self.cantina.frame_24.hide()
            self.cantina.frame_23.hide()
            self.cantina.frame_22.hide()
            self.cantina.frame_21.hide()
            self.cantina.frame_20.hide()
            self.cantina.frame_19.show()
            self.cantina.frame_18.show()
            self.cantina.frame_9.show()
            nov = RelatorioMarc()
            nov.rel(ano)
            receita = nov.resp['receita']
            self.cantina.lineEdit_4.setText(receita)
    def tabela_abril(self):
            ano = self.cantina.lineEdit_3.text()
            if not ano :
                return QMessageBox.about(self.cantina, "aviso", "informe uma data antes")
            self.cantina.frame_30.hide()
            self.cantina.frame_29.hide()
            self.cantina.frame_28.hide()
            self.cantina.frame_27.hide()
            self.cantina.frame_24.hide()
            self.cantina.frame_23.hide()
            self.cantina.frame_22.hide()
            self.cantina.frame_21.hide()
            self.cantina.frame_20.show()
            self.cantina.frame_19.show()
            self.cantina.frame_18.show()
            self.cantina.frame_9.show()
            nov = RelatorioAbril()
            nov.rel(ano)
            receita = nov.resp['receita']
            self.cantina.lineEdit_4.setText(receita)
    def tabela_maio(self):
            ano = self.cantina.lineEdit_3.text()
            if not ano :
                return QMessageBox.about(self.cantina, "aviso", "informe uma data antes")
            self.cantina.frame_30.hide()
            self.cantina.frame_29.hide()
            self.cantina.frame_28.hide()
            self.cantina.frame_27.hide()
            self.cantina.frame_24.hide()
            self.cantina.frame_23.hide()
            self.cantina.frame_22.hide()
            self.cantina.frame_21.show()
            self.cantina.frame_20.show()
            self.cantina.frame_19.show()
            self.cantina.frame_18.show()
            self.cantina.frame_9.show()
            nov = RelatorioMaio()
            nov.rel(ano)
            receita = nov.resp['receita']
            self.cantina.lineEdit_4.setText(receita)
    def tabela_jun(self):
            ano = self.cantina.lineEdit_3.text()
            if not ano :
                return QMessageBox.about(self.cantina, "aviso", "informe uma data antes")
            self.cantina.frame_30.hide()
            self.cantina.frame_29.hide()
            self.cantina.frame_28.hide()
            self.cantina.frame_27.hide()
            self.cantina.frame_24.hide()
            self.cantina.frame_23.hide()
            self.cantina.frame_22.show()
            self.cantina.frame_21.show()
            self.cantina.frame_20.show()
            self.cantina.frame_19.show()
            self.cantina.frame_18.show()
            self.cantina.frame_9.show()
            nov = RelatorioJunho()
            nov.rel(ano)
            receita = nov.resp['receita']
            self.cantina.lineEdit_4.setText(receita)
    def tabela_jul(self):
            
            ano = self.cantina.lineEdit_3.text()
            if not ano :
                return QMessageBox.about(self.cantina, "aviso", "informe uma data antes")
            self.cantina.frame_30.hide()
            self.cantina.frame_29.hide()
            self.cantina.frame_28.hide()
            self.cantina.frame_27.hide()
            self.cantina.frame_24.hide()
            self.cantina.frame_23.show()
            self.cantina.frame_22.show()
            self.cantina.frame_21.show()
            self.cantina.frame_20.show()
            self.cantina.frame_19.show()
            self.cantina.frame_18.show()
            self.cantina.frame_9.show()

            nov = RelatorioJul()
            nov.rel(ano)
            receita = nov.resp['receita']
            self.cantina.lineEdit_4.setText(receita)
    def tabela_ago(self):
            ano = self.cantina.lineEdit_3.text()
            if not ano :
                return QMessageBox.about(self.cantina, "aviso", "informe uma data antes")
            self.cantina.frame_30.hide()
            self.cantina.frame_29.hide()
            self.cantina.frame_28.hide()
            self.cantina.frame_27.hide()
            self.cantina.frame_24.show()
            self.cantina.frame_23.show()
            self.cantina.frame_22.show()
            self.cantina.frame_21.show()
            self.cantina.frame_20.show()
            self.cantina.frame_19.show()
            self.cantina.frame_18.show()
            self.cantina.frame_9.show()

            
            nov = RelatorioAgosto()
            nov.rel(ano)
            receita = nov.resp['receita']
            self.cantina.lineEdit_4.setText(receita)
    def tabela_set(self):
            ano = self.cantina.lineEdit_3.text()
            if not ano :
                return QMessageBox.about(self.cantina, "aviso", "informe uma data antes")
            self.cantina.frame_30.hide()
            self.cantina.frame_29.hide()
            self.cantina.frame_28.hide()
            self.cantina.frame_27.show()
            self.cantina.frame_24.show()
            self.cantina.frame_23.show()
            self.cantina.frame_22.show()
            self.cantina.frame_21.show()
            self.cantina.frame_20.show()
            self.cantina.frame_19.show()
            self.cantina.frame_18.show()
            self.cantina.frame_9.show()
            nov = RelatorioSetembro()
            nov.rel(ano)
            receita = nov.resp['receita']
            self.cantina.lineEdit_4.setText(receita)
    def tabela_out(self):
            ano = self.cantina.lineEdit_3.text()
            if not ano :
                return QMessageBox.about(self.cantina, "aviso", "informe uma data antes")
            self.cantina.frame_30.hide()
            self.cantina.frame_29.hide()
            self.cantina.frame_28.show()
            self.cantina.frame_27.show()
            self.cantina.frame_24.show()
            self.cantina.frame_23.show()
            self.cantina.frame_22.show()
            self.cantina.frame_21.show()
            self.cantina.frame_20.show()
            self.cantina.frame_19.show()
            self.cantina.frame_18.show()
            self.cantina.frame_9.show()

            nov = RelatorioOut()
            nov.rel(ano)
            receita = nov.resp['receita']
            self.cantina.lineEdit_4.setText(receita)
    def tabela_nov(self):
            ano = self.cantina.lineEdit_3.text()
            if not ano:
                return QMessageBox.about(self.cantina, "aviso", "informe uma data antes")
            self.cantina.frame_30.hide()
            self.cantina.frame_29.show()
            self.cantina.frame_28.show()
            self.cantina.frame_27.show()
            self.cantina.frame_24.show()
            self.cantina.frame_23.show()
            self.cantina.frame_22.show()
            self.cantina.frame_21.show()
            self.cantina.frame_20.show()
            self.cantina.frame_19.show()
            self.cantina.frame_18.show()
            self.cantina.frame_9.show()
           
             #novembro
           
            nov = RelatorioNov()
            nov.rel(ano)
            receita = nov.resp['receita']
            self.cantina.lineEdit_4.setText(receita)
            
                
    def tabela_dez(self):
            ano = self.cantina.lineEdit_3.text()
            if not ano:
                return QMessageBox.about(self.cantina, "aviso", "informe uma data antes")
            self.cantina.frame_30.show()
            self.cantina.frame_29.show()
            self.cantina.frame_28.show()
            self.cantina.frame_27.show()
            self.cantina.frame_24.show()
            self.cantina.frame_23.show()
            self.cantina.frame_22.show()
            self.cantina.frame_21.show()
            self.cantina.frame_20.show()
            self.cantina.frame_19.show()
            self.cantina.frame_18.show()
            self.cantina.frame_9.show()
           
            nov = RelatorioDez()
            nov.rel(ano)
            receita = nov.resp['receita']
            self.cantina.lineEdit_4.setText(receita)
    


        
        



app()
        


