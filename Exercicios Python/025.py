A = int(input("Digite o número A: "))
B = int(input("Digite o número B: "))

if B == 0:
    print("Divisão não pode ser efetuada")
elif A % B == 0:
    print("Numero A é  divisivel pelo numero B")
else:
    print("Numero A não é  divisivel pelo numero B")