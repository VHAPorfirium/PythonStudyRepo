# Leitura dos valores
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

print(f"Valores antes da troca: A = {A}, B = {B}")

temp = A
A = B
B = temp

print(f"Valores após a troca: A = {A}, B = {B}")
