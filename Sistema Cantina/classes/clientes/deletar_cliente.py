import requests

class deletar_cli:
    def del_cli(self, id):
        self.ulr= f"http://localhost:8040/clientes/{id}"
        
        requests.delete(url=self.ulr)