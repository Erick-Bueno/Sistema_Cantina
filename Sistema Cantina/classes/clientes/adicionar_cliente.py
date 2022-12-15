import json
import requests

class add_cliente:
    def Addcliente(self, nome, telefone):
        url = "http://localhost:8040/clientes/add"
        jsonn = {
            "Nome": nome,
            "Telefone": telefone
        }
        resp = requests.post(url=url, json=jsonn)
