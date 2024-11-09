from produtos import Produto

prod1 = Produto('tênis',235)
prod1.desconto(10)
print(prod1.valor)

prod2 = Produto('tênis', 'R$200')
prod2.desconto(10)
print(prod2.valor)