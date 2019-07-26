"""
    try/except Python

    Utilizamos o bloco try/except para tratar erros que podem ocorre no nosso código, previnindo assim que o programa
    para de fundionar e receba mensagens inesperadas.

    A forma geral mais simples é:

    try:
        // execução de código
    except:
        // Código  deve ser feito caso de problema
"""
try:
    geek()
except:
    print("Deu algum problema")

try:
    geek()
except NameError as ex:
    print(ex)
