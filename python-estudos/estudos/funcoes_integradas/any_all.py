# coding: UTF-8
# Criado por Sostenes em 02/07/2019

"""
    Any e All

    all() -> retorna true se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio
    any() -> retorna true se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna false
"""

# Exemplos all()
print(all([0,1,2,3,4])) #False
print(all([1,2,3,4])) # True
print(all([])) #True

nomes = ['Carlos', 'Carlito', 'Conica', 'Carla']
nomesFalse = ['Carlos', 'Marlito', 'Conica', 'Carla']

print(all(nome[0] == 'C' for nome in nomes))

print("\n\n")

#Exeplos any()

print(any([0,1,3,4])) # true
print(any([0])) # false
print(any([])) # false