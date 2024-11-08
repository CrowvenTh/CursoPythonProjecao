# Laço de repetição
~~~ python 
nomes = ['Julia', 'João', 'Marcos']         
for nome in nomes:
    print(nome)
~~~~
### For/else
~~~python
nomes = ['Julia', 'João', 'Marcos']
for nome in nomes:
    print(nome)
else:
    print("Todos os nomes foram listados com sucesso")
~~~
### For de string
~~~python
palavra = "Vamos estudar Python"
for letra in palavra:
    print(letra)
~~~
### For listando vetor
~~~python
pessoas = [({'nome': 'João', 'cidade': 'Ceilandia'}),
           ({'nome': 'Maria', 'cidade': 'Taguatinga'}),
           ({'nome': 'Pebinha', 'cidade': 'Ceilandia'})]
contador = 0
for pessoa in pessoas:
    contador += 1
    print(contador)
    print(pessoa['nome'], "mora em", pessoa['cidade'])
    # break
~~~
### For com  break
~~~python
pessoas = [({'nome': 'João', 'cidade': 'Ceilandia'}),
           ({'nome': 'Maria', 'cidade': 'Taguatinga'}),
           ({'nome': 'Pebinha', 'cidade': 'Ceilandia'})]
contador = 0
for pessoa in pessoas:
    contador += 1
    print(contador)
    if pessoa['nome'] == 'Maria':
        print(pessoa['nome'], "mora em", pessoa['cidade'])
        break
~~~
### For com continue
~~~python
pessoas = [({'nome': 'João', 'cidade': 'Ceilandia'}),
           ({'nome': 'Maria', 'cidade': 'Taguatinga'}),
           ({'nome': 'Pebinha', 'cidade': 'Ceilandia'})]
contador = 0
for pessoa in pessoas:
    contador += 1
    if pessoa['nome'] == 'Maria':
        continue
    print(contador)
    print(pessoa['nome'], "mora em", pessoa['cidade'])
~~~
### For com range que retorna o valor do contador o conteudo
~~~python
for numero in range(10):
    if numero % 2 == 0:
        print("O número", numero, "é par")
~~~
### For com enumerate
~~~python
for i, j in enumerate(range(10, 1, - 1)):
    print(i, j)
~~~
### For alinhado
~~~python
for numero_coluna1 in range(2, 5):
    print("Tabuada do ", numero_coluna1)
    for numero_coluna2 in range(11):
        print(numero_coluna1, "x", numero_coluna2, " = ", numero_coluna1 * numero_coluna2)
~~~
### Exemplo relogio
~~~python
import time
import os
for h in range(1, 24):
    for m in range(1, 60):
        for s in range(1, 60):
            print("h: ", h, "m: ", m, "s: ", s)
            time.sleep(1)
            os.system("cls")
~~~
### **Desafio**
Faça um programa em que o usuario ira digitar os valores de entrada de
hora, minuto e segundo para despertar chegando nestes valores especificos bipar o alarme para despertar 
~~~python
#Correção
import time
import os
import winsound
for h in range(1, 24):
    for m in range(1, 60):
        for s in range(1, 60):
            print("h: ", h, "m: ", m, "s: ", s)
            time.sleep(1)
            os.system("cls")
            frequency = 2500  # Set Frequency To 2500 Hertz
            duration = 1000  # Set Duration To 1000 ms == 1 second
            winsound.Beep(frequency, duration)
~~~
### Estrutura de Repetição Enquanto
~~~python
contador = 0
while (contador < 50):
    print(contador)
    contador = contador + 1
~~~
~~~python
While com String
nome = input('Digite um nome')
while nome:
    input('Digite um nome')
~~~
### Desempacontando listas
~~~python
lista = ['Joao', 'Fabio', 'julia', 1, 2, 3, 4, 5, 6, 8, 9, 10]
v1, v2, v3, *partenumerica = lista

print(v1, v2, v3, partenumerica)

v1, v2, v3, *partenumerica, ultimo = lista

print(v1, v2, v3, partenumerica, ultimo)
~~~
~~~python
"""
Utilizando dicionario para fazer um quiz
primeiro passo listando as perguntas e as opcoes de respostas 
"""
perguntas = {
    'Pergunta 1': {
        'pergunta': 'Qual a melhor Linguagem?',
        'respostas': {'a': 'Java', 'b': 'Python', 'c': 'Angular', },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Qual o Professor mais legal?',
        'respostas': {'a': 'Joao', 'b': 'Pedro', 'c': 'Maria', },
        'resposta_certa': 'a',
    }
}
print()
# indice_p indice da pergunta, indice_op indice da opçao
for indice_p, txtpergunta in perguntas.items():
    print(f'{indice_p}: {txtpergunta["pergunta"]}')

    print('respostas: ')
    for indice_r, valor_r in txtpergunta['respostas'].items():
        print(f'[{indice_r}]: {valor_r}')

 # verificando as respostas do usuario
    resposta_usuario = input('escolha a opcao ')

    if resposta_usuario == txtpergunta['resposta_certa']:
        print('acertou')
    else:
        print('errou')
        print()
~~~
### Hora da atividade para finalizar

Complemente o programa para rodar 10 vezes e mostre a quantidade de questões acertivas no final