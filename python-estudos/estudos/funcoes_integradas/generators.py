# coding: UTF-8
# Criado por Sostenes em 02/07/2019

"""
    Generators

    Tuple comprehesion

    nomes = ['Carlos', 'Camila', 'Cassiano', 'Cristina', 'Vanessa']

    print(any([nome[0] == 'C' for nome in nomes))

    Poderiamos realizar essa tarefa utilizando generators
"""

nomes = ['Carlos', 'Camila', 'Cassiano', 'Cristina', 'Vanessa']

# List Comprehesion
res = [nome[0] == 'C' for nome in nomes]
print(res)
print(type(res))

print("\n\n")

# Generator
res1 = (nome[0] == 'C' for nome in nomes)
print(res)
print(type(res))

print("\n\n")
# Em relação a performance Generator, consome menos recurso e memória


# A utilidade de getsizeof() é retornar a quantidade de bytes em memória do elemento passado como parâmetro
from sys import getsizeof

print(getsizeof(res))
print(getsizeof(res1))

list_comp = getsizeof([x*10 for x in range(1000)])
set_comp = getsizeof({x*10 for x in range(1000)})
dic_comp = getsizeof({x: x*10 for x in range(1000)})
gen = getsizeof(x*10 for x in range(1000))

print("Memória utilizada na mesma tarefa")
print(f"list_comp: {list_comp}")
print(f"set_comp: {set_comp}")
print(f"dic_comp: {dic_comp}")
print(f"gen: {gen}")

print("\n\n")

# É possível iterar no Generator Expression ? Sim!

gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)