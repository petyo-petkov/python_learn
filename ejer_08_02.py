import pickle
class Vehiculo:
    color = ''
    purtas = 0

    def __init__(self, color, puertas):
        self.color = color
        self.purtas = puertas
    def __str__(self):
        return f'El color es {self.color} y el numero de purtas es {self.purtas}'

v = Vehiculo('rojo', 5)
f = open('ejercicio.bin', 'wb')
pickle.dump(v, f)
f.close()
