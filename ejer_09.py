nombres = input('Introduzca nombres de paises: ')

s = set(nombres.title().split())
for i in s:
    if nombres in s:
        continue

print(list(sorted(s)))