from functools import reduce

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

impares = filter(lambda x: x % 2 != 0, lista)
impares = list(impares)

def suma(a, b):
    return a +b

resultado = reduce(suma, impares)

print(impares)
print(resultado)