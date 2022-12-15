import requests

class deletar_tudo:
    def deletar(self):
        url = "http://localhost:8040/deletarvenda"
        self.dado = requests.delete(url=url)