import requests

class RelatorioSetembro:
    def rel(self, ano):
        url = "http://localhost:8040/setembro"
        json = {
            'ano': ano  
        }
        self.dados = requests.get(url=url, json=json)
        self.resp = self.dados.json()