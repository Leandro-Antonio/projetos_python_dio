"""Aula3.3 — Calcula a média da nota de um aluno e verifica se a nota foi digitada corretamente entre 0 e 10"""

n1 = float(input('Digite a nota do primeiro bimestre: '))
if n1 > 10:
    print('Você digitou errado. Primeiro bimestre.\nDigite somente número menor ou igual a 10.')
n2 = float(input('Digite a nota do segundo bimestre: '))
if n2 > 10:
    print('Você digitou errado. Segundo bimestre.\nDigite somente número menor ou igual a 10.')
n3 = float(input('Digite a nota do terceiro bimestre: '))
if n3 > 10:
    print('Você digitou errado. Terceiro bimestre.\nDigite somente número menor ou igual a 10.')
n4 = float(input('Digite a nota do quarto bimestre: '))
if n4 > 10:
    print('Você digitou errado. Quarto bimestre.\nDigite somente número menor ou igual a 10.')
media = (n1 + n2 + n3 + n4) / 4
print(f'média {media}')
