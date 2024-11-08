# nome = 'Thiago'
# idade = 20
# res_bol = idade >= 18
# data_ano = 2024

# print('Nome: ',nome)
# print('Idade: ',idade)
# print('Resultado booleano: ',res_bol)
# print('Ano: ',data_ano)

# # IMC

# peso = 75
# altura = 1.67

# imc = peso / (altura ** 2)
# print('IMC: ',imc)
# print(f'IMC, {imc: ,.2f}')

# ======================================

# nome = input("Digite o nome")
# idade = input("digite sua idade")

nome = 'Thiago'
idade = 20

if(idade > 17):
    maiorIdade = "maior de idade"
else:
    maiorIdade = "Menor de idade"

result = f'Seu nome é {nome}, você tem {idade} anos de idade e é {maiorIdade}'
print(result)