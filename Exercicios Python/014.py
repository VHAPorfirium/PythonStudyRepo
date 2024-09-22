import math

x = (int(input("X: ")))
y = (int(input("Y: ")))

calculo = math.sqrt((3 * x + 30) / 3) + ((y - 32) ** 4)

print(f'{calculo:.2f}')