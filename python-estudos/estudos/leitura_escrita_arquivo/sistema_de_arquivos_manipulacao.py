"""
    Sistema de arquivos manipulação

    https://docs.python.org/3/library/os.html?highlight=os#module-os
"""

import os

# Descobrindo se um arquivo existe Ou diretório
print(os.path.exists('texto.txt'))
print(os.path.exists('texto-nao-existe.txt'))

# Criando arquivos

# Forma 1
open('arquivo-teste.txt', 'w').close()

# Forma 2
open('aruivo-teste2.txt', 'a').close()

# Forma 3
with open('arquivo-teste3.txt', 'w') as arquivo:
    pass

# Forma 4
# os.mknod('arquivo-teste4.txt') Somente linux
#os.mkdir('teste-pasta')

# Renomear arquivos e diretórios
#os.rename('arquivo-teste.txt', 'arquivo-com-novo-nome.txt') # Renomeando arquivpo
#os.rename('teste-pasta', 'pasta') # Renomeando pasta

# Obs se o diretório que queremos renomear não estiver vazio, teremos OSError

# Deletando arquivos. OBS: Tome cuidado com comando de deleção, os arquivos somem não vão pra lixeira
# os.remove('arquivo-teste3.txt') # Remove arquivo

# OBS: Se você estiver no Windows e o arquivo que você for deletar estiver em uso, você tera um erro.
# OBS: Caso o arquivo não exista, teremos o FileNotFoundError
# OBS: Se você informar um diretório ao invés de um arquivo, teremos um IsADirectoryError


# Removendo diretórios vazios
# os.rmdir('pasta') # Remove o diretório

# OBS: Se o diretório tiver qualquer conteúdo teremos um OSError
# OBS: Se o diretório não exister teremos um FileNotFoundError