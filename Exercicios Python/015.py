import math

x1 = int (input('x1: '))
y1 = int (input('y1: '))
x2 = int (input('x2: '))
y2 = int (input('y2: '))

distanciaEuclidiana = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print()

print(f'{distanciaEuclidiana:.2f}')