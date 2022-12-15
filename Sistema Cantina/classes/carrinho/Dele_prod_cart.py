import requests

class dele_produto_cart:
    def delete(self, id):
        url=f"http://localhost:8040/carrinho/{id}"
        requests.delete(url=url)