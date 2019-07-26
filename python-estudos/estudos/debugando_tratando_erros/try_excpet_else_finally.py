"""
    try/excpet/else/finally


    try:
        num = int(input("Informe um número"))
    except ValueError as err:
        print("Valor incorrerto")
    else:
        print(f'Voce digitou {num}')

    try:
        num = int(input("Informe um número"))
    except ValueError as err:
        print("Valor incorrerto")
    else:
        print(f'Voce digitou {num}')
    finally:
        print("Acabou toda execução")
"""

# Else -> É executado somente se não ocorrer o erro declarado.

# Finally -> O bloco finally é sempre executado idependente se houve exceção ou não.
# OBS: Normalmente utilizado para fechar conexões ou desalocar recursos

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um erro {err}'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))

