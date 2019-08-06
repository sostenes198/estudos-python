"""
    Seek e Cursors

    seek() -> É utilizada para movimentar o curso pelo arquivo
"""

arquivo = open('texto.txt')
print(arquivo.read())

# Movimentando o cursor pelo arquivo com a função seek()

arquivo.seek(0) # seek(0) -> Movimento o curso para o inicio do arquivo
print(arquivo.read())

arquivo.seek(10)
print(arquivo.read())
arquivo.close()

# readline() -> Função que lê o arquivo linha a linha
arquivo = open('texto.txt')
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())
arquivo.close()

# readlines() -> Lê todas as linhas do arquivo
arquivo = open('texto.txt')
print(arquivo.readlines())
arquivo.close()

"""
OBS: Quando abrimos um arquivo coma função open() é criada uma conexão entre o arquivo no disco do computador
e o nosso programa. Esse conexão é chamada de streaming. Ao finalizar os trabalhos com o arquivo devemos fechar a conexão.
Para isso utilizamos a função close()
"""

arquivo = open('texto.txt')
print(arquivo.read(10))
arquivo.close()