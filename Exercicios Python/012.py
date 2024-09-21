a1 = float(input("Digite o primeiro termo (a1): "))
r = float(input("Digite a razão (r): "))
n = int(input("Digite o valor de n (n-ésimo termo): "))

an = a1 + (n - 1) * r

print(f"O {n}-ésimo termo da P.A. é: {an}")
