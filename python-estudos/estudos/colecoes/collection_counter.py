# coding: UTF-8
# Criado por Sostenes em 10/04/2019

"""

    Collections -> High performance Container Types

    Counter -> Recebe um interável e cria um objeto do tipo Collection Counter que é parecido
    com um dicionario, contendo como chave o elemento da lista passada como parametro e com valro a
    quantidade de ocorrencias deste elemento

"""

from collections import Counter

lista = [1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,6,7,7,7,7,7]

res = Counter(lista)

print(type(res))
print(res)