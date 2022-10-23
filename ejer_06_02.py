class Alumno:
    nombre = input('Nombre de alumno: ')
    nota = float(input('Nota de alumno: '))
    resultado =''
    def Aprobado(self):
        if self.nota >= 4 and self.nota <= 10:
            self.resultado = 'aprobado'
        else:
            self.resultado = 'suspendido'
    def Resultado(self):
        return self.resultado
a = Alumno()
a.Aprobado()
a.Resultado()
print(a.nombre, 'ha', a.resultado,'con nota', a.nota)