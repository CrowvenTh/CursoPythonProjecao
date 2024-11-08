def calculos(op, v1, v2):
    if op == 1:
        return v1 + v2
    elif op == 2:
        return v1 - v2
    elif op == 3:
        return v1 * v2
    elif op == 4:
        return (v1 + v2)/2
    else:
        return 0

# chamando a função passando valores
# podemos receber o valor de retorno em uma variavel local

print(calculos(4, 8, 3))