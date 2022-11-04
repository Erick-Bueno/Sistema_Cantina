import requests


class del_prod:
    def dele(self,id):
        self.res = requests.delete(f"http://localhost:8040/produto/{id}")
        self.resp = self.res.json()

