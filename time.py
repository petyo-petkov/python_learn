import time

hora = time.strftime('%H')
fin = '19'
if hora > fin:
    print('Hora de volver a casa')
else:
    q = int(fin) - int(time.strftime('%H'))
    print('Te quedan ', q,'horas de trabajo')