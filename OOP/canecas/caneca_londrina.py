from canecas.caneca import Caneca

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