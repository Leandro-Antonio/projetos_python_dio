"""Aula3.2 - Testar se dois números digitados são pares, ou se um deles é par ou se nenhum é par"""
numero_a = int(input('Entre com um número: '))
numero_b = int(input('Entre com um número: '))
resto_a = numero_a % 2
resto_b = numero_b % 2

if resto_a == 0 and resto_b == 0:
    print('Ambos os números são pares')
elif resto_a == 0 or resto_b == 0:
    print('Pelo menos um dos números é par.')
else:
    print('Nenhum dos números é par')
print('Fim do programa')
