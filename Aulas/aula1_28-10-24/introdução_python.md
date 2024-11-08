# Instalação

instalando o extensão Python no **VScode** no campo pesquisar digite:  Python

instalando o code-runner para execução dos projetos de forma automática, no campo pesquisar digite: [code-runner](formulahendry.code-runner)

instalando o django-html para utilização futura de itens html
no campo pesquisar digite:  django-html

instalando o todo  para utilização de comentários 
no campo pesquisar digite:  [todo-tree](akiega.tree)

 Na linha 7 do arquivo settings temos:
"*python.pythonPatch*":  "Caminho para criação dos projetos " funciona como um work space
Na linha 22 podemos escolher entre o cmd ou o power-shell
 
~~~~ linux
Para instalação no Linux
sudo apt update -y
sudo apt upgrade -y
sudo apt install curl -y
sudo apt install git -y

sudo apt install python3.8 python3.8-dev python3.8-venv \
  python3-venv idle-python3.8 python3-pip virtualenv gcc \
  default-libmysqlclient-dev libssl-dev -y

sudo snap install pycharm-community --classic
~~~~
# Primeiro Projeto
Crie uma pasta em seu computador onde serão colocados todos os seus projetos chamamos esta pasta de workspace no meu caso será:
d:CursoPython/aula1Canal

Para criação do ambiente virtual digitamos o seguinte código estando dentro da pasta criada:
~~~~
python -m venv venv
~~~~
agora precisamos ativar o ambiente com o comando
~~~~
venv \ Scripts \ activete.bat
~~~~
após o comando deverá aparecer o item (**venv**) antecedendo o caminha do seu projeto.
Nas versores mais novas não aparece.

agora vamos criar nosso arquivo de código fonte para isso click e new file de o nome de **app.py** e salve

dentro do arquivo vamos escrever o seguinte código:
~~~~ python
print('Primeiro Projeto em Python')
~~~~
salve o arquivo

neste momento se houver necessidade a própria ferramente vai pedir para instalar novas extensões
Provavelmente serão: linter e autopep8

agora  click no icole do **run** no canto superior direito e veja o resultado no cmd que aparecerá abaixo

Comentarios no python
para comentar linhas
~~~
"""   codigos """ para bloco de comentarios geralmente utilizado para documentaçao
tambem pode ser utilizados ''' codigos '''
~~~
Exemplo: 

comentário em uma linha
~~~ python
#print('ola mundo') 
~~~
comentário em mais de uma linha:
~~~ python
'''
print('ola mundo') 
print('introdução a python!')
'''
~~~
=========================
##### Concatenação
~~~~ python
print('Estou aprendendo python', 'hoje foi a primeira aula')

print('Estou aprendendo python', 'hoje foi a primeira aula', sep='-')

print('Estou aprendendo python', 'hoje foi a primeira aula', sep='-', end='***')
print('Sabado ', 'dia de estudar', sep='-', end='')
~~~~
##### Exemplo de utilização
~~~ python
print('772', '558','333', sep='.', end='-')
print('20')
#Observe o resultado
~~~~
Formas de impressão de caracteres
~~~ python
print("texto 'texto entre aspas simples' ")
print('texto "texto entre aspas duplas" ')
~~~~