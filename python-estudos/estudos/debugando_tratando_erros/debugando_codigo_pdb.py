"""
    Debungando código com pdb -> Python Debugger

    def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um erro {err}'

    num1 = input('Informe o primeiro número: ')
    num2 = input('Informe o segundo número: ')

    print(dividir(num1, num2))

"""

# Exemplo com PDB -> Python Debugger

# Para utilizar o Python Debugger, precisamos importar a biblioteca pdb e então utilizar a função set_trace()

# Comandos básicos do PDB
# l (listar onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a excução - finaliza debbugin)

"""
    Exemplo 1
    
    import pdb
    nome = "Soso"
    sobrenome = "Souza"
    pdb.set_trace()
    nome_completo = f'{nome} {sobrenome}'
    print(nome_completo) 
"""

"""
    Exemplo 2
        
    nome = "Soso"
    sobrenome = "Souza"
    import pdb; pdb.set_trace()
    nome_completo = f'{nome} {sobrenome}'
    print(nome_completo)
"""

# A partir do python 3.7, não é mais necessário importar a biblioteca pdb, pois o comando de debug foi
# incorporado como função built-in (integrada) chamada breakpoint()

nome = "Soso"
sobrenome = "Souza"
breakpoint()
nome_completo = f'{nome} {sobrenome}'
print(nome_completo)