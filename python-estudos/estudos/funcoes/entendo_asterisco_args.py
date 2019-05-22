# coding: UTF-8
# Criado por Sostenes em 08/05/2019

"""
    Entendo o *args

    O *args é um parâmetro, como outro qualquer. Isso signigica que você podera chamar
    de qualquer coisa desde que comece com *

    Exemplo:
    *xis

    Porém por convenção nomeamos como *args para defini-lo

    o parâmetro *args utilizado em uma função, coloca os valores extras informados como entrada
    em uma tupla. Então desde já lembre-se que tuplas são imutáveis

    OBS: O asterisco serve para que informamos ao Python que estamos passando como argumento uma coleção
    de dados. Desta forma, ele saberá que precisará antes desempacotar estes dados
"""

def soma_todos_numeros(*args):
    total = 0
    for numero in args:
        total += numero
    return total

print(soma_todos_numeros(1))
print(soma_todos_numeros(1,2))
print(soma_todos_numeros(1,2,3))
print(soma_todos_numeros(1,2,3,4,5,6,7))