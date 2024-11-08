# Map python linkando arquivos
produtos = [
    {'nome': 'p1', 'preco': 10},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 10},
    {'nome': 'p4', 'preco': 10},
    {'nome': 'p5', 'preco': 10},
]

clientes = [
    {'nome': 'Ana', 'idade': 18},
    {'nome': 'Maria', 'idade': 20},
    {'nome': 'Jose', 'idade': 35},
    {'nome': 'Pebinha', 'idade': 16},
    {'nome': 'juquinha', 'idade': 12},
]

from dados import produtos, clientes

for produto in produtos:
    print(produto)
# com isto estamos buscando os produtos no arquivo dados e imprimindo no arquivo principal
#Buscando os preços com map

precos = map(lambda p: p['preco'], produtos)

for preco in precos:
    print(preco)