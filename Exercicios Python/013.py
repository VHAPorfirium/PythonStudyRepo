salarioMinimo = float(input('Digite o valor do salario minimo: '))

unidadeLCD = int(input('Digite a quantidade de unidade de tv LCD vendida: '))
unidadeLED = int(input('Digite a quantidade de unidade de tv LED vendida: '))
unidadePLASMA = int(input('Digite a quantidade de unidade de tv de plasma vendida: '))

comissaoLCD = 50 * unidadeLCD
comissaoLED = 60 * unidadeLED
comissaoPLASMA = 75 * unidadePLASMA

total = (salarioMinimo * 2) + comissaoLCD + comissaoLED + comissaoPLASMA


print(f"O salario total é de R$ {total:.2f} reais.")