import math

raio = float(input("Digite o raio da esfera: "))

area = math.pi * raio ** 2

perimetro = 2 * math.pi * raio

print(f"Area: {area:.2f}")

print(f"Perimetro: {perimetro:.2f}")