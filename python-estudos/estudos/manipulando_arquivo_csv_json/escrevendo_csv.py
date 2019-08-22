"""
    Escrevendo arquivo CSV

    reader() -> (leitor), writer (escritor)

    writerow() -> escreve uma linha

    with open('filmes.csv', 'w') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Titulo', 'Genero', 'Duracao'])
    while filme != 'sair':
        filme = input('Informe o nome do file: ')
        if filme != 'sair':
            genero = input('Informe o genero: ')
            duracao = input('Informe a duracao: ')
            escritor_csv.writerow([filme, genero, duracao])

print('\n\n\n')
"""

from csv import writer, DictWriter

with open('filmes2.csv', 'w') as arquivo:
    cabecalho = ['Titulo', 'Genero', 'Duracao']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do file: ')
        if filme != 'sair':
            genero = input('Informe o genero: ')
            duracao = input('Informe a duracao: ')
            escritor_csv.writerow({"Titulo": filme, "Genero": genero, "Duracao": duracao})
            # OBS as chaves do dicionario devem ser as mesmas utilizadas como cabeçalho