import requests

class att_cliente:
    def attcliente(self, id, nome, telefone):
        url = f"http://localhost:8040/clientes/{id}"
        jsonn = {
            "Nome": nome,
            "Telefone": telefone
        }
        requests.put(url=url, json=jsonn)