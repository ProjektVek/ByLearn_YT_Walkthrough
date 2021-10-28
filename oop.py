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
        self.preco = 24.90
        self.__preco_fabrica = 15

    def beber(self): #function receiving the object itself as parameter
        print('Estou bebendo da caneca ', self.nome)
        self.status = 'Vazia'
        return f'É da {self.nome} que eu estou bebendo'

    def encher(self):
        print('Enchendo a caneca ', self.nome)
        self.status = 'Cheia'
        return f'Estou enchendo a {self.nome}'

class CanecaLondrina(Caneca):
    def __init__(self):
        super().__init__('Caneca Londrina', 'Cidade de Londres', 'Branca')
        self.bebida = 'Chá'
        self.preco = 29.90

    def extras(self):
        print('Como bônus vc ganha uma colher')

    def beber(self):
        self.status = 'Vazia'
        print('Tá na hora do chá das 5')

        '''
        self.nome = 'Caneca Londrina'
        self.logo = 'Cidade de Londres'
        self.cor = 'Branca'
        self.status = 'Cheia'
        '''
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

caneca1 = Caneca('Caneca Londrina', 'Cidade de Londres', 'Branca')
caneca2 = Caneca('Caneca ByLearner', 'Foguete da ByLearn', 'Branca')

print('A caneca ', caneca1.nome, 'possui a logo', caneca1.logo)
print('A caneca ', caneca2.nome, 'possui a logo', caneca2.logo)

caneca3 = CanecaLondrina()
caneca4 = CanecaLondrina()
caneca5 = CanecaLondrina()

print(caneca1)
print(caneca2)
print(caneca3)
print(caneca4)
print(caneca5)

caneca_londres = CanecaLondrina()
caneca_batman = CanecaBatman()
caneca_bylearn = Caneca('Caneca ByLearner', 'Foguete da ByLearn', 'Branca')

caneca_londres.extras()
caneca_batman.som()

print(caneca_bylearn.beber())
print(caneca_londres.beber())
print(caneca_batman.beber())

print("Promoção:")
caneca_batman.preco = caneca_batman.preco - 5
caneca_londres.preco = caneca_londres.preco - 5
caneca_bylearn.preco = caneca_bylearn.preco - 5

print('Novos Preços')
print(f'A {caneca_batman.nome} tem o valor de {caneca_batman.preco} reais')
print(f'A {caneca_londres.nome} tem o valor de {caneca_londres.preco} reais')
print(f'A {caneca_bylearn.nome} tem o valor de {caneca_bylearn.preco} reais')