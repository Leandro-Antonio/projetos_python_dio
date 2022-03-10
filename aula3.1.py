"""Aula3.1 -  testar se o número é par"""
numero = int(input('Entre com um número: '))
resto = numero % 2
if resto == 0:
    print(f'O número {numero} é par.')
else:
    print(f'O número {numero} é ímpar')
print('Fim do programa')
