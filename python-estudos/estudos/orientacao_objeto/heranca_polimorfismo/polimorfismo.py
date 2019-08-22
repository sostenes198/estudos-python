"""
    POO - Polimorfismo

    Poli -> Muitas
    Morfis -> Formas

    Overriding é a reimplementação  de um método presente na classe pai em classes filhas
"""

from abc import abstractmethod


class Animal(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, nome):
        self.__nome = nome

    @abstractmethod
    def falar(self):
        raise NotImplementedError('Tem que implementar porra')

    def comer(self):
        print(f'{self.__nome} está comendo...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala wauwau')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala miamiu')


class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)


# Testes
cachorro = Cachorro('cachorro')
cachorro.comer()
cachorro.falar()

gato = Gato('gato')
gato.comer()
gato.falar()

rato = Rato('rato')
rato.comer()
rato.falar()