import requests

class adicionar_Prod_cart:
    def add(self, Nome , Quantidade):
        url = "http://localhost:8040/carrinho/add"
        json = {
            "Nome": Nome,
            "Quantidade": Quantidade
        }
        requests.post(url=url, json=json)