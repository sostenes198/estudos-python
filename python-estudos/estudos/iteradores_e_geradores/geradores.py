"""
    Geradores

    - Geradores (Generators) são Iterators (Iteradores):

    OBS: O contrário não é verdadeiro. Ou seja, nem todo iterator é um generator

    Outras informações:
        - Generators podem ser criados com funções geradoras;
        - Funções geradores utilizam a palavra reservada yield;
        - Generators podem ser criados com Expressões Geradoras

    Diferença entre funções e Generator Functions (Funções Geradoras)

--------------------------------------------------------------------------------------------------------------------
    |   Funções                                     |    Generator Functions                                       |
--------------------------------------------------------------------------------------------------------------------
    |   utilizam return                             |   utilizam yield                                             |
--------------------------------------------------------------------------------------------------------------------
    |   retorna uma vez                             |   podem utilizar yield múltiplas vezes                       |
--------------------------------------------------------------------------------------------------------------------
    |   quando executado, retorna um valor          |   quando executado, retorna um generator                     |
--------------------------------------------------------------------------------------------------------------------

    OBS: Um generator Function não é um Generator. Ele gera um generator
"""
# Exemplo Função Geradora (Generator Function)
def cont_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1


for n in cont_ate(10):
    print(n)