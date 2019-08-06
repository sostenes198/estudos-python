"""
    Sistema de arquivos e Navegação

    Para fazer o uso de manipulação de arquivos do sistema operacional, precisamos importar
    e fazer uso do módulo os

    os -> Operating System : Sistema Operacional
"""

import os

# Retorna o caminho absoluto
print(os.getcwd())

# Para mudar o diretório, podemos utilizar o chdir()

os.chdir('..')
print(os.getcwd())

# Podemos chegar se um diretório é absoluto ou relativo
print(os.path.isabs('D:\Projetos\Python\estudos-python\python-estudos\estudos'))
print(os.path.isabs('estudos-python\python-estudos\estudos'))

# Podemos identificar o sistema operacional com o módulo os
print(os.name) # posix (Linux e Mac), nt (Windows)

# Podemos ter mais detalhes no sistema operacional
# print(os.uname()) Linux

import sys
print(sys.platform) # Windows

print(os.listdir())

scanner = os.scandir()
arquivos = list(scanner)
[print(arquivo.name) for arquivo in arquivos]
scanner.close()

# OBS: Quando utilizamos a função scandir() nós precisamos fecha-lá, assim quando abrirmos um arquivo
with list(os.scandir()) as arquivos:
    [print(arquivo.name) for arquivo in arquivos]

