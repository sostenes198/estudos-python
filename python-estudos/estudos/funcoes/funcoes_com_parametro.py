# coding: UTF-8
# Criado por Sostenes em 08/05/2019

"""
    Funções com parâmetro de entradas

    Funções que recebem parametros de entrada para serem processados dentro da mesma

    Diferença entre parâmetros e argumentos

    # Parâmetros são variaveis declaradas na definição de uma função
    # Argumentos são dados passados durante a execução de uma função
"""

def quadrado(numero):
    return numero * 2

# Argumentos nomeados, quando utilizado argumentos nomeados para informa-los, podemos utilizar em qualquer ordem

def nome_completo (nome, sobrenome):
    print(f'Nome: {nome} \nSobrenome:{sobrenome}')

print(nome_completo(nome="Sóso", sobrenome="Dois_Hit"))