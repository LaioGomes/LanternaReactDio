lista_preco = [500, 100, 490, 340, 58]

#caso 1
nova_lista_preco = []
for preco in lista_preco:
    nova_lista_preco.append(preco * 2)
print(nova_lista_preco)

#caso 2
nova_lista_preco2 = [preco * 2 for preco in lista_preco]
print(nova_lista_preco2)

print(2**2 -4 * 1 * 3)


#listComprehension
casa = [10, 7, 21, 19, 15]

nova_lista = [i ** 2 for i in casa]
print(f'a lista é {casa} e o resultado ao quadrado é {nova_lista}')


import random 

print(random.random()*10)

print(random.choice(['asa', 'coxa', 'filé']))


var = 'pizza'
x = len(var)
print(var + f' tem {x} letras')

print(var[4])
print(var[1:4])
print(var[:])
print(var[:4])
a = var + ' ' + "brasileira," + ' '
print(a*10)
print(var[0:2] + 'tágoras')
