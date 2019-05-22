# coding: UTF-8
# Criado por Sostenes em 10/04/2019

"""
    Conjuntos

    Conjuntos em qualquer lingagem de programação, estamos fazendo referência a teoria dos conjuntos
    da matematica

    No python conjuntos são chamados de Set

    -   Sets (conjuntos) não possuem valores duplicados
    -   Sets (conjuntos) não possuem valores ordenados
    -   Sets (conjuntos) não possuem acesso via indices, ou seja conjuntos não são indexados

    Conjuntos são bons para se utilizar quando precisamos armazenar elementos, mas não nos importa
    com a ordenação deles.

    Os conjuntos (sets) são referenciados em python com chaves {}

    Diferença entre conjunto (sets) e Mapas (Dicionarios) em Python:
    -   Um dicionario tem chave/valor
    -   Um conjunto tem apenas valor
"""

# Definindo Conjunto

# Forma 1
s = set({1,2,3,4,5,6, 6})
print(s)

# Obs Ao criar um conjunto valor repetidos são ignorados

# Forma 2
s = {1,2,3,3,5,6}