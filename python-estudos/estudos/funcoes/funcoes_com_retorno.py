# coding: UTF-8
# Criado por Sostenes em 08/05/2019

"""
    Funcões com retorno

    OBS: EM Python, quando uma função não retornar nenhum valor, o retorno é NONE

    OBS sobre a palavra return:
        1 - Ele finaliza a função ou seja, ele sai da execução da função
        2 - Podemos ter, em uma função diferentes returns
        3 - Podemos, em uma função retornar qualquer tipo de dados e até mesmo multiplos valores
"""

def quandrado_de_7():
    return 7*7

quadrado_de_7 =  quandrado_de_7()

def retorno_multiplos_valores():
    return 1,2,3,4

valor = retorno_multiplos_valores()

print(valor)

print(quadrado_de_7)