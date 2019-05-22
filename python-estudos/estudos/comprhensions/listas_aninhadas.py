# coding: UTF-8
# Criado por Sostenes em 15/05/2019

"""
    Listas aninhadas

    - Algumas linguagens de programação possuem estruturas de dados arrays:
        - Unidimensionais (Array/Vetores)
        - Multidimensionais (Matrizes)

    Em python temos as liastas

    numeros = [1,2,3,4]
"""

# Exemplos

listas = [[1,2,3], [4,5,6], [7,8,9]] # Matriz 3 x 3

print(listas)
print(type(listas))

print("\n\n")
# Iterando com loops  em uma lista aninhada
for lista in listas:
    for num in lista:
        print(num)

# List comprehension

[[print(valor) for valor in lista] for lista in listas]