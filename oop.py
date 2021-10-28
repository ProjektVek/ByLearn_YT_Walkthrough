class Caneca: #Creating a class
    formato = 'Cilíndrico com alça lateral'

    logo = ''
    cor = ''
    nome = ''

    def __init__(self, nome, logo, cor): #Creating Constructor
        self.nome = nome
        self.logo = logo
        self.cor = cor
        self.status = 'Cheia'

    def beber(self): #function receiving the object itself as parameter
        print('Estou bebendo da caneca ', self.nome)
        self.status = 'Vazia'

    def encher(self):
        print('Enchendo a caneca ', self.nome)
        self.status = 'Cheia'

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

caneca1 = Caneca('Caneca Londrina', 'Cidade de Londres', 'Branca')
caneca2 = Caneca('Caneca ByLearner', 'Foguete da ByLearn', 'Branca')

print('A caneca ', caneca1.nome, 'possui a logo', caneca1.logo)
print('A caneca ', caneca2.nome, 'possui a logo', caneca2.logo)