# Interando na lista mas com funcionamento incorreto
#lista_nums = [100, 200, 300, 400]
#
#for item in lista_nums:
#    item += 1000
#print(lista_nums)

# Código para pecorrer uma lista baseado em um índice
#lista_nums = [100, 200, 300, 400]
#for i in range(len(lista_nums)):
#    lista_nums[i] += 1000
#print(lista_nums)

lista_nums = [100, 200, 300, 400]
for index, item in enumerate(lista_nums):
    lista_nums[index] += 1000
print(lista_nums)
