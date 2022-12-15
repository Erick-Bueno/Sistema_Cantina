import requests

class pesquisarcliente:
    def pes_cli(self, campo_pes):
        url = "http://localhost:8040/clientes/pesq"
        json = {
            "pesqCliente": f"{campo_pes}"
        }
        req= requests.post(url=url, json=json)
        self.resp = req.json()
        