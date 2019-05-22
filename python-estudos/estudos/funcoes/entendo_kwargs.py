# coding: UTF-8
# Criado por Sostenes em 08/05/2019

"""
    *kwargs

    Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras em uma tupla,
    o **kwargs exige que utilizemos parâmetros nomeados e transforma esses parâmetros extras em um
    dicionário
"""

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')

cores_favoritas(marcos='verde', julia='amarelo', sostnes='azul', raquel='rosa')

# OBS: Os parâmetros *args e **kwargs não são obrigatórios

# Desempacotar com **kwargs

def mostrar_nome(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}

print(mostrar_nome(**nomes))

def soma(a, b,c ):
    print(a + b + c)

lista = [1,2,3]
tupla = (1,2,3)
conjunto ={1,2,3}
dicionario = dict(a=1, b=2, c=3)
soma(*lista)
soma(*tupla)
soma(*conjunto)
soma(**dicionario)

# OBS: Os nomes da chaves em um dicionario devem ser o mesmo dos parâmetros da função