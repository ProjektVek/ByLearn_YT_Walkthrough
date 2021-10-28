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
        self.__preco_fabrica = 15.

    def beber(self): #function receiving the object itself as parameter
        print('Estou bebendo da caneca ', self.nome)
        self.status = 'Vazia'
        return f'É da {self.nome} que eu estou bebendo'

    def encher(self):
        print('Enchendo a caneca ', self.nome)
        self.status = 'Cheia'
        return f'Estou enchendo a {self.nome}'