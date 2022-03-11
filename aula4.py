# """Aula 4 condicional for, testa se um número é primo"""
#
# """Percorre de 0 a 100 e exibe cada passada """
# for x in range(101):
#     print(x)
# print('fim ')
#
# """Percorre de 90 até 109 e exibe cada passada"""
# for y in range(90, 100):
#     print(y)
# print("fim")

# """Testa se um número é primo """
# div = 0
# numero = int(input("Digite um número"))
# for z in range(1, numero + 1):
#     resto = numero % z
#     if resto == 0:
#         print(numero, resto)
#         div += 1
# if div == 2:
#     print(f'número {numero} é primo')
# else:
#     print(f'número {numero} não é primo')

# """Testa se um número é primo a partir da entrada digitada pelo usuário"""
#
# a = int(input('Entre com um valor: '))
# for numero in range(a):
#     div = 0
#     for z in range(1, numero + 1):
#         resto = numero % z
#         # print(z, resto)
#         if resto == 0:
#             div += 1
#     if div == 2:
#         print(numero)

"""Caso seja digitado uma nota maior que 10 o laço de repetição while retorna uma mensagem de erro"""
nota = float(input('Entre com uma nota: '))
while nota > 10:
    print('Você digitou uma nota errada. Digite apenas nota entre 0 e 10.')
    nota = float(input('Digite novamente: '))
print(nota)
