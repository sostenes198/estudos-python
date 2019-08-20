"""
    POO - Classes

    Em Poo - Classes nada mais são que modelos dos objetos do mundo real sendo representados
    computacionalmente

    Imagine que você queira fazer um sistema para automitizar o controle das lâmpadas da sua casa.

    Classes podem conter:
        Atributos -> Representa as caracteristicas do objeto
        Métodos (Funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto
        pode realizar no seu sistema.

    Para criar classe em python utiliza-se a palavra reservada class

    OBS: Utilizamos a palavra 'pass' em Python quando temos um bloco de código que ainda não está implementando.

    OBS: Quando nomeamos classes em Python utilizamos a converção o nome com inicial maiúsculo. Se o nome for composto,
    utiliza-se de ambas as palavras em maiúsculo, todos juntos.
"""

class Lampada:
    pass

lampada = Lampada()
print(type(lampada))