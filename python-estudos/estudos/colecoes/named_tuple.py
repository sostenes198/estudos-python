# coding: UTF-8
# Criado por Sostenes em 10/04/2019

"""
    Modulo: collection - Named Tuple

    São tuplas diferenciadas, onde, especificamos um nome para a mesma e também parâmetros
"""

from collections import namedtuple

# Forma 1
cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3
cachorro = namedtuple('cachorro', {'idade', 'raca', 'nome'})

# Usando

# Forma 1
ray = cachorro(idade=2, raca='cho cho', nome='ray')
print(ray)
print(ray[0])
print(ray[1])
print(ray[2])

# Forma 2
ray = cachorro(idade=2, raca='cho cho', nome='ray')
print(ray)
print(ray.idade)
print(ray.raca)
print(ray.nome)
