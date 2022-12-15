import requests

class RelatorioOut:
    def rel(self, ano):
        url = "http://localhost:8040/outubro"
        json = {
            'ano': ano  
        }
        self.dados = requests.get(url=url, json=json)
        self.resp = self.dados.json()