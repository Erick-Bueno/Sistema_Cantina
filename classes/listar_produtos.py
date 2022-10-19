import requests

class listar:
    def listando(self):
        self.resposta = requests.get("http://localhost:8040/produto")
        self.produtos = self.resposta.json()


       