from random import randint
for i in range(6):
    soreteado = randint(1, 60)
    print(soreteado)

###

# outro exemplo
produtos = [
    ['p1', 128],
    ['p2', 430],
    ['p3', 318],
    ['p4', 785],
    ['p5', 855],
]
# utilizano lanbda para passar os prdutos como parametro e imprimindo-os pelo indice nome
print(sorted(produtos, key=lambda index: index[0]))

###

# utilizando lanbda para passar os prdutos como parametro e imprimindo-os pelo preço
print(sorted(produtos, key=lambda index: index[1], reverse=True))
#observação o index[1] já funciona como o comando return

# recurso legal para desempacotamento lista comprehension python
carrinho = []
carrinho.append(('p1', 90))
carrinho.append(('p2', 34))
carrinho.append(('p3', 580))
carrinho.append(('p4', 102))

soma = sum([float(valores) for item, valores in carrinho])
print(carrinho)
print('Valor total dos produtos', soma)

###


pedido1 = [125, 132, 98, 10]
pedido2 = [25, 28, 102, 35, 50, 65]

# maneira peba
lista_soma = []
for i in range(len(pedido1)):
    lista_soma.append(pedido1[i]+pedido2[i])
print(lista_soma)

# maneira pro
lista_soma_pro = [x+y for x, y in zip(pedido2, pedido1)]
print(lista_soma_pro)