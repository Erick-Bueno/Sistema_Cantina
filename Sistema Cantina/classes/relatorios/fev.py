import requests

class RelatorioFev:
    def rel(self, ano):
        url = "http://localhost:8040/fevereiro"
        json = {
            'ano': ano  
        }
        self.dados = requests.get(url=url, json=json)
        self.resp = self.dados.json()