# coding: UTF-8
# Criado por Sostenes em 08/04/2019

"""
    Loop for

    Loop -> Estrutura de repetição
    For -> Uma estrutura de repetição

    C ou Java
    for(int i = 0; i < length; i++){
        // Execução do código
    }

    Python

    for item in interval:
        // Execução do loop


    Utilizamos loop para iterear sobre sequências ou sobro valores iteraveis

    Exemplos de iteraveis:
    -String
        nome = "Soso"
    -Lista
        lista = [1,2,3]
    -Range
        numeros = range(1,10)
"""

nome = 'Soso'
lista = [1,2,3,4,5]
numeros = range(1,10)

# Interando em uma string
for letra in nome:
    print(letra)

print("-----------------------------")

# Interando em uma lista
for numero in lista:
    print(numero)

print("-----------------------------")

# Interando em um range
for numero in numeros:
    print(numero )

print("-----------------------------")

# Enumerate forma de interar em uma lista com indice e valor
for indice, valor in enumerate(nome):
    print(indice)
    print(valor)