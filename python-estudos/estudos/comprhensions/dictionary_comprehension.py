# coding: UTF-8
# Criado por Sostenes em 15/05/2019

"""
    Dictiornary comprehension

    Pense no seguinte:

    Criar
        lista = [1,2,3,4]
        Tupla = (1,2,3,4)
        cojunto(set) = {1,2,3,4}
        dicionario = {'a': 1, 'b':2, 'c':3, 'd':4}
"""

#Exemploos

numeros = {'a': 1, 'b': 2, 'c': 3, 'd':4}
quadrado={chave:valor ** 2 for chave, valor in numeros.items()}