from classes002 import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()
produto = Produto()

p1 = produto('Camiseta', 50)
p2 = produto('Calça', 80)
p3 = produto('bermuda', 60)

carrinho.inserir_produto(p1)

carrinho.lista_produto()