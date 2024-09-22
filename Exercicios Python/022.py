numero = int(input("Digite um numero: "))

unidade = numero % 10
dezenas = (numero / 10) % 10
centenas = numero / 100

print(f'centenas: {centenas:.0f} dezenas: {dezenas:.0f} Unidade: {unidade:.0f}')