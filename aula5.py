"""Aula 5 Manipulação de listas"""
lista = [9, 1, 5, 3]
lista_animal = ['cachorro', 'gato', 'elefante', 'cavalo', 'arara']
# print(lista_animal[1])
print(f'esta lista está fora da ordem numérica\n {lista}')
lista.sort()
print(f'esta lista está em ordem numérica\n {lista}')

print(f'estas lista está fora da ordem alfabética\n {lista_animal}')
lista_animal.sort()
print(f'esta lista está em ordem alfabética\n {lista_animal}')
lista_animal.reverse()
print(f'esta lista está em ordem alfabética invertida \n {lista_animal}')

# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print(soma)
# print(min(lista))
# print(max(lista_animal))

# if 'gato' in lista_animal:  # testa se existe na lista um elemento especificado
#    print('Existe gato na lista')

if 'lobo' in lista_animal:
    print('Existe lobo na lista')
else:
    print('Não existe gato na lista, então será incluído')
    lista_animal.append('lobo')  # adiciona ao final da lista o elemento especificado
    print(lista_animal)

lista_animal.pop(2)  # remove o último elemento
print(lista_animal)
lista_animal.remove('cachorro')  # remove o elemento especificado
print(lista_animal)
