def soma(num1, num2):
    return print(f"Soma: {num1} + {num2} = ", num1+num2)
def subtracao(num1, num2):
    return print (f"Subtração: {num1} - {num2} = ", num1-num2)
def multiplicacao (num1, num2):
    return print (f"Multiplicação: {num1} * {num2} = ", num1*num2)
def divisao(num1, num2):
    return print (f"Divisão: {num1} / {num2} = ", num1/num2)
print('--------------------------------')
print('--------------------------------')
print('      --  Calculadora   --    ')
print('--------------------------------')
num1 = int(input('Digite o primeito numero: '))
num2 = int(input('Digite o segundo numero: '))
print (' ( + ) adição')
print (' ( - ) subtração')
print (' ( * ) multiplicação')
print (' ( / ) divisão')
operador = input ('Escolha uma operação :')
if operador == '+':
    soma(num1, num2)
elif operador == '-':
     subtracao(num1, num2)
elif operador == '*':
     multiplicacao(num1, num2)
elif operador == '/':
     divisao(num1, num2)
else:
    print('Operador desconhecido')

### Calculadora II

def calc(op, num1, num2):
    if(op == '+'):
        return print(f"Soma: {num1} + {num2} = ", num1+num2)

    if(op == '-'):
        return print(f"Soma: {num1} - {num2} = ", num1-num2)

    if(op == '*'):
        return print(f"Soma: {num1} * {num2} = ", num1*num2)

    if(op == '/'):
        if (num2 > 0):
            return print(f"Divisão: {num1} / {num2} = ", num1/num2)
        else:
            return print(f"Erro na Divisão: ", 0)


sair = '1'
while (sair != '0'):
    print('--------------------------------')
    print('--------------------------------')
    print('      --  Calculadora   --    ')
    print('--------------------------------')
    num1 = int(input('Digite o primeito numero: '))
    num2 = int(input('Digite o segundo numero: '))
    print(' ( + ) adição')
    print(' ( - ) subtração')
    print(' ( * ) multiplicação')
    print(' ( / ) divisão')
    operador = input('Escolha uma operação :')
    calc(operador, num1, num2)

    sair = input(
        'Digite 0 para sair  ou 1 Para continuar :')
    print('--------------------------------------------------------')
 