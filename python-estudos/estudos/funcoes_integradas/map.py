# coding: UTF-8
# Criado por Sostenes em 01/07/2019

"""
    Map

    Com map fazemos mapeamentos de valores para função.
"""

import math

def area(r):
    """Calcula a área de um círculo com 'r'"""
    return math.pi * (r ** 2)


print(area(2))
print(area(3))

print("\n\n")

raios = [2,4,5,7.1,0.3,10,44]


# Utilizando Map
areas = map(area, raios)

print(type(areas))
print(list(areas))


"""
    Map é uma função que recebe dois parâmetros
    
    O primeiro é a função.
    O segundo é o iterável.
    
    Seu retorno é do tipo Map
"""

print("\n\n")

# Utilizando map com expressão lambda

print(list(map(lambda r: math.pi * (r ** 2), raios)))

print("\n\n")

# Obs: após utilizar a função map(), depois da primeira utilização do resultado, ele zera.