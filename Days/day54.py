"""Compreensões de Listas"""

l1 = [1, 2, 3, 4, 5, 6, 7, 8]
lista_pares = [n for n in l1 if n % 2 == 0]
lista_impares = [n for n in l1 if n % 2 != 0]
lista_dobrada = [n * 2 for n in l1]
lista_quadratica = [n**2 for n in l1]
# Exibindo os resultados
print(l1)
print(lista_pares)
print(lista_impares)
print(lista_dobrada)
print(lista_quadratica)
