# coding: UTF-8
# Criado por Sostenes em 27/03/2019

"""
    Recebendo dados do usuário

    input() -> todo dado recebido via input é recebido como string
"""

# Entrada de dados
#print("Olá qual o seu nome ?")
nome = input("Olá qual o seu nome ?")

# Exemplo de print antigo 2.X
#print("Seja bem vindo(a) %s", nome)

# Exemplo print 3.X +
#print("Seja bem vindo {0}".format(nome))

# Exemplo de print Mais atual
print(f'Seja bem vindo {nome}')

#print("Qual sua idade?")
#idade = input("Qual sua idade?")
idade = int(input("Qual sua idade?"))

# Processamento

#Saida
#print("A {0} tem {1} anos".format(nome, idade))
print(f'A {nome} tem {idade} anos')

#print(f'A {nome} nasceu em {2019 - int(idade)}')
print(f'A {nome} nasceu em {2019 - idade}')

"""
    Cast é a conversão de um tipo de dados para outro 'explicitamente'
"""

