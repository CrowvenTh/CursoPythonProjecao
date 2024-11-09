# criando uma classe
class Pessoa:
    # def comer(self):
    #     print('Não come carne')
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_nascimento(self):
        print(self.nome, "nasceu em ", self.ano_atual - self.idade)