# coding: UTF-8
# Criado por Sostenes em 12/03/2019

"""
PEP8 - Python Enchament Proposal

São propostas de melhorias para a linguagem Python

The zen of python

import this

A ideia da PEP8 é que possamos escrever código Python de forma Pythônica

[1] - Utilize Camel Case para nomes de classes:
    Exemplo:
        class Calculadora:
            pass

[2] - Utilize nomes em minusculo separado por underline para funções ou variáveis

    Exemplo:
        def some():
            pass

        def soma_dois():
            pass

        numero = 4
        numero_impar = 3

[3] - Utilize 4 espaços para identação ! (Não use tab)
    Exemplo:
        if 'a' in 'banana':
            print('tem')

[4] - Linhas em branco
        - Separar funções e definições de classes com duas linhas em branco
        - Métodos dentro de uma classe deve ser separado com uma linha em branco

[5] - Imports
        - Imports devem ser sempre feitos em linhas separadas
        Exemplos:
            # Import Errado
                import sys, os
            # Import Correto
                import sys
                import os
            # Não há problemas em utilizar:
                from types import StringTYpe, ListType
            # Caso tenha muitos importes de um mesmo pacote, recomenda-se fazer:
                from types import {
                    StringTYpes,
                    ListTypes,
                    SetType
                    OutroType
                }
            # Imports devem ser colocados no top do arquivo, logo depis de quaisquer comentários ou decstrings
              e antes de constantes ou variáveis globais

[6] - Espaços em expressões e instruções

[7] - Termine uma instrução sempre com uma nova linha

"""

