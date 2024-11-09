from produtos import Produto

print('Digite o nome do produto')
nome = input()

print('Digite o valor do produto')
valor = float(input())

print('Digite o valor do desconto')
desc = int(input())
prod2 = Produto(nome, valor)
prod2.desconto(desc)

#print(f'Nome: {prod2.nome} Valor do desonto {prod2.valor}')
print(
    f'Nome do Produto: ​​​​​​{prod2.nome}​​​​​​ | Valor com Desconto: {prod2.valor}​​​​​​')

##############################################################################

from mercado import Carrinho, ProdutoDisponivel

meucarrinho = Carrinho()
# print(meucarrinho)

produto1 = ProdutoDisponivel('Mouse', 35)
produto2 = ProdutoDisponivel('Teclado', 50)

meucarrinho.inserir_produto(produto1)
meucarrinho.inserir_produto(produto2)
meucarrinho.lista_produto()

# como o metodo tem um returno interno precisamos dar um print
print("Total do Carrinho R$: ", meucarrinho.soma_total())
