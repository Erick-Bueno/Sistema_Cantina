import requests

class listar_produto_cart:
    def listar(self):
        url = "http://localhost:8040/carrinho"
        self.dados = requests.get(url=url)