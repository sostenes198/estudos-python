# coding: UTF-8
# Criado por Sostenes em 08/05/2019

"""
    Documetando funções com docstring

    OBS: Podemos ter acesso à documentação de uma função em Python
    utilizando a propriedade especial __doc__

    Podemos ainda fazer acesso a documentação com a função help
"""

#print(help(print))

# Exemplos
def diz_oi():
    """Uma função simples que retornar a string oi"""
    return "Oi"

#print(help(diz_oi))
#print(diz_oi.__doc__)

def exponencial(numero, potencial=2):
    """
    Função que retorna por padrão o quadrado de um número
    :param numero: Numero que desejamos gerar exponencial
    :param potencial: Potência que queremos gerar o exponecial por padrão o valor é 2
    :return: Retorna o exponecial do 'número'
    """
    return numero ** potencial

print(help(exponencial))
print(exponencial.__doc__)