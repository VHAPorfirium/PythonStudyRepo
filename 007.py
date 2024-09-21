valor = float(input('Digite o valor do produto: '))

desconto = float(int(input('Digite o desconto do produto: ')))

calculo = valor - (valor * desconto / 100)

print(f"Novo valor = {calculo:.2f} reais")