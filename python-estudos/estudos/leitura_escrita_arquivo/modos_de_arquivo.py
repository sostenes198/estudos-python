"""
    Modos de abertura de Arquivo

    r -> Abre para leitura : Padrão
    w -> Abre para a escrita : Sobrescreve caso o arquivo já exista
    x -> Abre para escrita se o arquivo não existir. Caso exista, gera o erro FileExistError
    a -> Abre para a escrita adicionando o conteúdo ao final do arquivo
        OBS: Abrindo no modo 'a' -> append, se o arquivo não existir será criado. Caso exista, o novo conteúdo
            será adicionado ao final.
    + -> Abre para o modo atualização. Leitura e Escrita

    https://docs.python.org/3/library/functions.html#open
"""