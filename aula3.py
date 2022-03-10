"""Aula 3 - Condicional if """
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
if a > b and a > c:
    print(f'o maior número é {a}')
elif b > a and b > c:
    print(f'O maior número é {b}')
else:
    print(f'O maior número é {c}')
print("Fim do programa")
