

f = open('miArchivo.txt', 'w')
texto = f.write('Este es mi texto')
f.close()

f = open('miArchivo.txt', 'r')
texto = f.read()
f.close()
print(texto)