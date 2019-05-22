# coding: UTF-8
# Criado por Sostenes em 10/04/2019

"""

    Default dict

    Ao criar um dicionario utilizando-o, nos informamos um valor default,
    podendo utilizar uma lambda para isso, Este valor será utilizado sempre que não houver
    um valor definido. Caso tentemos acessar uma chave que não existe, essa chave sera
    criada e o valor default será atribuido

"""

from collections import defaultdict

dicionario = defaultdict(lambda : 0)

print(dicionario)

dicionario['curso'] = 'Programação em Python inicial'
print(dicionario)