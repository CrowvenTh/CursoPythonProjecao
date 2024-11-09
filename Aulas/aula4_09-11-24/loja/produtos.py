class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
    
    def desconto(self, percentual):
        self.valor = self.valor - (self.valor * (percentual / 100))

    # metodos getters and setters

    # get para retorno do valor
    @property 
    def valor(self):
        return self._valor

    #setter com validação de tipo
    @valor.setter
    def valor(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._valor = valor