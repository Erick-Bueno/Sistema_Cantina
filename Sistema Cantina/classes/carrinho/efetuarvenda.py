import requests

class EfetuarVenda:
    def venda(self, venda):
        url = "http://localhost:8040/vendas/est"
    
        self.resp = requests.post(url=url, json=venda)