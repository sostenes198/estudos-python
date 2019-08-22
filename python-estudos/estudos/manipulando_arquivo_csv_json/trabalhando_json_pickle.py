"""
    JSON e Pickle

    JSON -> Java Script Object Notation

    Escrevendo em arquivo json com jsonpickle

    with open('felix.json', 'w') as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)
"""

import json
import jsonpickle

ret = json.dumps(['produto', {'Playstation4': ('2tb', 'Novo', '220V', 2340)}])
print(type(ret))
print(ret)

class Gato(object):

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

felix = Gato('Felix', 'Vira-Lata')

print(felix.__dict__)

ret = json.dumps(felix.__dict__)

print(ret)

print('\n\n')

ret = jsonpickle.encode(felix)
print(ret)


# Lendor arquivo json

with open('felix.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(type(ret))
    print(ret)
    print(ret.__dict__)
    print(ret.nome)