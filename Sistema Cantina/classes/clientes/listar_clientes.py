import requests

class listarClientes:
    def listarCli(self):
        url = "http://localhost:8040/clientes"
        resp = requests.get(url=url)
        self.dados = resp.json()
