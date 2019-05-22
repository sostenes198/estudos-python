# coding: UTF-8
# Criado por Sostenes em 08/04/2019

"""

    Saindo de loops com break

    Funciona da mesma forma de c ou java

    Utilizamos break para sair de looops de maneira projetadas

"""

#Exemplo 1

for numero in range(1, 10):
    if numero == 6:
        break
    else:
        print(numero)

print("Saiu do loop")

#Exemplo 2

while True:
    comando = input("Digite sair para sair:")
    if comando == "sair":
        break