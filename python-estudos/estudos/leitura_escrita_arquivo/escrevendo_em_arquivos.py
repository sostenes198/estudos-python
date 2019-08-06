"""
    Escrevendo em arquivos

    OBS: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele. Apenas ler. Da mesma forma, se abrirmos um arquivo
    para a escrita, não podemos le-lo, somente escrever nele.

    Abrindo um arquivo para escrita com modo 'w', se o arquivo não existir ele será criado. Caso ele já exista,
    o anterior será apagado e um novo será criado. Dessa forma, todo o conteudo no arquivo anterior é perdido
"""

# Exemplo - w  -> Write (escrita)
with open('texto.txt', 'w') as arquivo:
    arquivo.write('Escrever em arquivos é izi\n')
    arquivo.write('Podemos escrever quantas linhas quisermos\n')
    arquivo.write('Essa é a ultima linha\n')