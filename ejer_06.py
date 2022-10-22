class Color:
    color = 'Negro'
class Ruedas:
    cantiad = 4
class Puertas:
    cantidad = 5
class Velociad:
    velociad = None
class Cilindrada:
    cantidad = 12

class Vehiculo:
    color = Color()
    ruedas = Ruedas()
    puertas = Puertas()

class Coche(Vehiculo):
    velociad = Velociad()
    cilindrada = Cilindrada()

c = Coche()

print('El coche es de color ',c.color.color)
print('El coche tiene', c.puertas.cantidad, 'puertas', ',' ,c.ruedas.cantiad, 'ruedas', 'y', c.cilindrada.cantidad, 'de cilindros')
