# coding: UTF-8
# Criado por Sostenes em 27/03/2019

"""
    Tipo String

    Em python, o dado sempre é considerado uma string quando:

    - Estiver entre aspas simples 'Isso é uma string' 
    - Ou aspas duplas "Isso é uma string"
"""
    #- Ou aspas simples triplas """ Isso também é uma string"""


nome = "Soso"
print(nome)
print(type(nome))

nome = "Soso\nSouza"
print(nome)
print(type(nome))

nome = """
    Soso
    Souza
"""
print(nome)
print(type(nome))

"""
    Colocar todas as letras em masiculo
    nome.upper()
    
    Colocar todas as letras em minusculo
    nome.lower()
    
    Transforma uma string em um array
    nome.split()
"""

nome = "Sostenes G de Souza"
print(nome[0:4]) # Slice de string

nome = "Sostenes G de Souza"
print(nome[5:15]) # Slice de string

# [::-1] começe do primeiro elemento vá até o ultimo elemento e inverta
nome = "Sostenes G de Souza"
print(nome[::-1])  # Inversão de string Pythônica



