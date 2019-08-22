"""
    Métodos mágicos

    Métodos mágicos, são métodos que utilizam dunder

    dunder init() -> __init()__

"""
from typing import TypeVar

T = TypeVar('T', str, bool)


class Livro(object):

    def __init__(self, titulo, autor, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas

    def __repr__(self):
        return f'{self.__titulo} escrito por {self.__autor}'

    def __str__(self):
        return f'{self.__autor} {self.__titulo} escrito por {self.__autor}'

    def __len__(self):
        return self.__paginas

    def __del__(self):
        print('Um objeto do tipo livro vazou da memória')

    def __add__(self, outro):
        return f'{self} - {outro}'

    def teste(self, valor: T) -> T:
        return f'{valor}'


livro1 = Livro('P', 'AB', 100)
livro2 = Livro('A', 'HG', 200)

print(livro1)
print(len(livro1))
print(livro2)
print(len(livro2))
print(livro1 + livro2)

print(livro1.teste(1.1))
print(livro1.teste('awe'))
