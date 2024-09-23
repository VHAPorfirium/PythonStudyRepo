print("Menu: ")
print("1- Adição")
print("2- Subtração")
print("3- Multiplicação")
print("4- Divisão")
print("Escolha uma operação")
escolha = input()

print()

numero1 = int(input("Digite um numero: "))

numero2 = int(input("Digite outro numero: "))

print()

if escolha == "1":
    print(numero1 + numero2)
elif escolha == "2":
    print(numero1 - numero2)
elif escolha == "3":
    print(numero1 * numero2)
elif escolha == "4":
    if numero2 == 0:
        print("Divisão inpossivel com o denominador valendo 0")
    else:
        print(numero1 / numero2)
else:
    print("Opção invalida.")

