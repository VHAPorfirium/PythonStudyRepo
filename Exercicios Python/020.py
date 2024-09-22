areaTotalTerreno = float(input('Digite a area do terreno: '))

areaConstruida = float(input('Digite a area construida: '))

areaNaoConstruida = areaTotalTerreno - areaConstruida

impostos = (areaConstruida * 5) + (areaNaoConstruida * 3.80)

print(f'Valor do impoto = {impostos:.2f} reais')