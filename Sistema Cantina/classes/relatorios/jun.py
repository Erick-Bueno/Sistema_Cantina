import requests

class RelatorioJunho:
    def rel(self, ano):
        url = "http://localhost:8040/junho"
        json = {
            'ano': ano  
        }
        self.dados = requests.get(url=url, json=json)
        self.resp = self.dados.json()