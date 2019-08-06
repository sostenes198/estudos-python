"""
    Bloco Witch

    Passo para se trabalhar com arquivos

    # 1 - Abrimos arquivos
    # 2 - Manipulamos arquivos
    # 3 - Fechamos arquivos

    O bloco with é utilizado para criar um contexto de trabalho, onde os recursos utilizados
    são fechados após o bloco with
"""

# Exemplo - Forma Pythônica de manipular arquivos
with open('texto.txt') as arquivo:
    print(arquivo.readlines())