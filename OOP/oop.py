from canecas.caneca import Caneca
from canecas.caneca_londrina import CanecaLondrina
from canecas.caneca_batman import CanecaBatman 

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