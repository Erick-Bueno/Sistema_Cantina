import requests

class att_produto_cart:
    def atualizar(self, id, Nome, Quantidade):
        url = f"http://localhost:8040/carrinho/{id}"
        json = {
            "Nome": Nome,
            "Quantidade": Quantidade
        }
        requests.put(url=url, json=json)