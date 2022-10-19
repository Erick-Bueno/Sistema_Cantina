from urllib import response
import requests

class att_prod:
    def atualizar(self, id, nome_produto, preço, quantidade, peso,unimedida, categoria, valor_compra_total, valor_compra_unitaria):
        self.url = f"http://localhost:8040/produto/{id}"
        self.resposta = {
            "Nome": nome_produto,
            "Preço": preço,
            "Quantidade": quantidade,
            "Peso": peso,
            "UniMedida": unimedida,
            "Categoria": categoria,
            "Preço_Compra_total" : valor_compra_total,
            "Preço_Compra_Unitario": valor_compra_unitaria
        }
        requests.put(url=self.url, json=self.resposta)