"""
    Leitura Arquivo

    Para ler o conteudo de um arquivo em Python, utilizamos a função integrada open(),
    que literalmente significa 'abrir'

    open() -> A forma mais simples de utilização, é passado apenas um parametro de entrada, que neste caso é o caminho
    do arquivo a ser lido. Essa função retorna um _io.TextIOWrapper e é com ele que trabalhamos.

    <_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>

    mode r -> Modo de leitura. r -> read() -> ler

    encoding='cp1252'
"""

# Exemplo

arquivo = open('texto.txt')
print(arquivo)
print(type(arquivo))

# Para ler o conteudo de um arquivo apos aberto, utiliza-se a função read()
print(arquivo.read())

ret = arquivo.read()
print(type(ret))
print(ret)

# OBS: O Python, utiliza um recurso para trablahar com arquivos chamado cursos. Esse cursos
# Funciona com um cursosr quando estamos escrevendo

# OBS: A funcao read(), lê todo o conteúdo do arquivo