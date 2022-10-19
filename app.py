from ast import Delete, Try
from audioop import add
from cProfile import label
import enum
from itertools import count
from classes import deletar_produto
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
from classes.adicionar_produto import add_prod
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from classes.listar_produtos import listar
from classes.pesquisar_produto import pesquisa
from classes.deletar_produto import del_prod
from classes.atualizar_produto import att_prod
counter = 0
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
        self.cantina.frame_14.hide()
        self.cantina.frame_15.hide()
        self.cantina.pushButton_21.clicked.connect(self.adicionar_produto)
        self.cantina.pushButton_23.clicked.connect(self.cancelar)
        self.cantina.pushButton_20.clicked.connect(self.enviar_produto)
        self.cantina.lineEdit_4.setText(f"0R$")
        self.cantina.pushButton.setGraphicsEffect(effect3)
        self.cantina.pushButton_19.setGraphicsEffect(effect2)
        self.cantina.pushButton_21.setGraphicsEffect(effect)
        self.cantina.pushButton_23.setGraphicsEffect(effect5)
        self.cantina.pushButton_20.setGraphicsEffect(effect4)
        self.cantina.pushButton_34.setGraphicsEffect(effect6)
        self.cantina.pushButton_35.setGraphicsEffect(effect7)
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
        self.load_scree()
        self.carrega.show()
        self.app.exec()
    #produtos
    def deletar(self):
            linha = self.cantina.tableWidget_2.currentRow()
            if linha == -1:
                 return QMessageBox.about(self.cantina,"aviso","selecione um produto antes de deletar")
            id = self.cantina.tableWidget_2.item(linha,0).text()
            
          
            
            
            
            d = del_prod()
            d.dele(id)
            l = listar()
            l.listando() 
            self.cantina.tableWidget_2.removeRow(linha)
       
      
            return QMessageBox.about(self.cantina,"aviso","produto deletado com sucesso")
    def atualizar(self):
        linha = self.cantina.tableWidget_2.currentRow()
        

 
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
        
       

        
        
        



app()
        


