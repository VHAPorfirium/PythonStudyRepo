custoFabrica = float(input('Digite o custo da fabrica: '))

porcentagemDistribuidor =  (custoFabrica * 0.12)

impostos = (custoFabrica * 0.30)

total = custoFabrica + porcentagemDistribuidor + impostos

print(f"Total do valor do carro: R$ {total:.2f}.")