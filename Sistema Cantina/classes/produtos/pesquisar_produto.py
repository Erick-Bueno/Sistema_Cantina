import requests
class pesquisa:
    def pesquisar(self, pesq):
        url = "http://localhost:8040/produto/pesquisar"

        request = {
    "campo_pesquisa": f"{pesq}"
    }

        self.dados = requests.post(url=url, json=request)
    