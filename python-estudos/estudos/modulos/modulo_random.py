"""
    Módulo random e oque são modolos

    - Em Python módulos nada mais são que outros aquivos em Python.

    Módulo Random -> Possui várias funções para geração de números pseudo-aletórios
"""

# OBS: Existem duas formas de se utilizar um módulo ou função deste

# Forma 1 (Não recomendado)
#import random
#print(random.random())

# Ao relizar o import te todo o módulo, todas as funcões, atributos, classes e propriedades que estiverem
# Dentro do módulo ficarão disponíveis (Ficarão em memória)
#C Caso saiba quais as funções que você precisa utilizar deste módulo, então não será necessário está forma de utilização.

# Forma 2

from random import random

print(random())

# uniform() -> Gera um número pseudo-aleatório entre os valores estabelecidos

from random import uniform

print(uniform(3,7)) # Obs: Último número não é incluido

# randint() -> Gera valores pseudo-aleatórios inteiros entre os valores estabelecidos

from random import randint

print(randint(4, 10))

# choice() -> Mostra um valor alteaório entre um iterável

jogadas = ['pedra', 'papel', 'tesoura']

from random import choice

print(choice(jogadas))

# shuffle() -> Tem a função de embaralhar dados

from random import shuffle

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']
print(cartas)
shuffle(cartas)
print(cartas)
shuffle(cartas)
print(cartas)