"""
    Trabalhando com modulos Builtin (modulos integrados, que ja vem instalados no Python)

    https://docs.python.org/3/py-modindex.html
"""

# Utilizando alias (apelido) para modulos/funcões

import random as rdm
from random import shuffle as sf

# Podemos utilizar todas as funções de um módulo utilizando o *
from random import *
print(random())

# Multiplos imports
from random import random, randint, shuffle, choice

# Pode-se se utilizar tuple para colocar múltiplos imports de um mesmo módulo

from random import(
    random,
    randint,
    shuffle,
    choice
)

print(randint)
