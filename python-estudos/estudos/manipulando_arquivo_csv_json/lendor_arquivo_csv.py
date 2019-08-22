"""
    Lendo arquivo CSV

    CSV - Comma Separeted Values - Valores Separados por vírgula
"""

from csv import DictReader, reader

# SEM CABECALHO
with open('lutadores.csv', encoding='utf8') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=';')
    for linha in leitor_csv:
        print(f'{linha["Nome"]} nasceu no(a)(s) {linha["País"]} e mede {linha["Altura (em cm)"]}')

print("\n\n\n")

with open('lutadores.csv', encoding='utf8') as arquivo:
    leitor_csv = reader(arquivo, delimiter=';')
    for linha in leitor_csv:
        print(f'{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]}')

print("\n\n\n")

with open('lutadores.csv', encoding='utf8') as arquivo:
    leitor_csv = reader(arquivo, delimiter=';')
    next(leitor_csv)
    for linha in leitor_csv:
        print(f'{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]}')