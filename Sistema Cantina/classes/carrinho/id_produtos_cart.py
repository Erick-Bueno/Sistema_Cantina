import requests

class Id_produtos_cart:
    def id_prod(self, nome):
        url = "http://localhost:8040/encontrar"
        json = {
            'nome' : nome
        }
        self.dados = requests.post(url=url, json=json)