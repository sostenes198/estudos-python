"""
    Ententendo Iterators e Iterables

    Iterator ->
        - Um objeto que pode ter iterado
        - Um objeto que retorna um dado, sendo um elemento por vez quando um função next() é chamado;

    Iterable ->
        - Um objeto que irá retornar um iterator quando a função iter() for chamada.
"""

# Exemplo
nome = 'Geek' # É um iterable mas não é um iterator
numeros = [1,2,3,4,5] # É um iterable mas não é um iterator

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))
print(next(it2))