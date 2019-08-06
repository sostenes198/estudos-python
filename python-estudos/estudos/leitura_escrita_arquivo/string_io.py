"""
    String IO

    Atenção: Para ler ou escrever dados em arquivos do sistema operacional o software precisa.
    ter permissão:
        - Permissão de Leitura -> Para ler o arquivo.
        - Permissao de Escrita -> Para escrever o arquivo.
"""

# Primeiro fazemos o import
from io import StringIO

mensagem = "Está é apenas uma mensagem normal"

# Podemos criar um arquivo em memória já com uma string inserida ou mesmo vazio inserimos texto depois
arquivo = StringIO(mensagem)
