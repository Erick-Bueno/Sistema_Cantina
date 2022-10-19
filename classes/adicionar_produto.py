import requests

class add_prod:
    def adicionar(self, nome_produto, preço, quantidade, peso,unimedida, categoria, valor_compra_total, valor_compra_unitaria):
        ulr = "http://localhost:8040/produto/add"
        
        resposta = {
            "Nome": nome_produto,
            "Preço": preço,
            "Quantidade": quantidade,
            "Peso": peso,
            "UniMedida": unimedida,
            "Categoria": categoria,
            "Preço_Compra_total" : valor_compra_total,
            "Preço_Compra_Unitario": valor_compra_unitaria
        }
        requests.post(url=ulr, json=resposta)
        
        

    
        