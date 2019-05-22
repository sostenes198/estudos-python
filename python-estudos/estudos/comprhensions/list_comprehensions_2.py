# coding: UTF-8
# Criado por Sostenes em 15/05/2019

"""
    List comprehensions

    Nós podemos adicionar estruturas condicionais lógicas às nossas List comprehensions
"""

#Exeplos
#1
numeros =[1,2,3,4,5,6]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# Refatoração

pares = [numero for numero in numeros if not numero % 2 ]
impares = [numero for numero in numeros if numero % 2 ]

print(pares)
print(impares)