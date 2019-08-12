"""
    Teste de Velocidade com Expressão Geradoras
"""

# Generators (Geradores)

def nums():
    for num in range(1, 10):
        yield num

g1 = nums()
print(g1)
print(next(g1))
print(next(g1))

# Generator Expression
g2 = (num for num in range(1,10))
print(g2)
print(next(g2))
print(next(g2))

# Realizando Teste de Velocidades
import time

# Generator Expression
gen_inicio = time.time()
print(sum(num for num in range(100000000)))
gen_tempo = time.time() - gen_inicio
print(gen_tempo)

# List Comprehension
list_inicio = time.time()
print(sum([num for num in range(100000000)]))
list_tempo = time.time() - list_inicio


print(f'Generator Expression levou {gen_tempo}')
print(f'List Comprehension levou {list_tempo}')

