from canecas.caneca import Caneca

class CanecaBatman(Caneca):
    def __init__(self):
        super().__init__('Caneca Gotham', 'Batman', 'Preta')
        self.bebida = 'Café'
        self.preco = 34.90

    def som(self):
        print("I'm Batman")

    def beber(self):
       return super().beber() + f' {self.bebida}'

'''
caneca1 = Caneca() #Creating an object
caneca1.nome = 'Teste'
caneca1.logo = 'Logo'
caneca1.cor = 'Verde'

print(caneca1.nome, caneca1.logo, caneca1.cor)
caneca1.beber()

Caneca.logo = 'Padrão'
caneca2 = Caneca()
print(caneca2.logo)
'''
