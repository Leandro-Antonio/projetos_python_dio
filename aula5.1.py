"""Aula 5.1 — Tuplas e converção de lista para tupla, tupla em lista"""
lista = [9, 1, 5, 3]
lista_animal = ['cachorro', 'gato', 'elefante', 'cavalo', 'arara']

# lista_animal[0] = 'macaco'  # acrescenta na posição zero o elemento especificado
# print(lista_animal)

# tuplas não podem ser alteradas diferentemente das listas
# tupla = (1, 10, 12, 14)
# tupla[0] = 3  # Vai retornar um erro porque tuplas não podem ser alteradas
# print(tupla)

tupla = (1, 10, 12, 14)
print(len(tupla))  # conta quantos elementos existem na tupla
print(len(lista_animal))  # conta quantos elementos existem na lista
tupla_animal = tuple(lista_animal)  # converte lista para tupla
print(type(tupla_animal))
print(tupla_animal)

lista_numerica = list(tupla)  # converte uma tupla em lista
print(type(lista_numerica))
print(lista_numerica)
