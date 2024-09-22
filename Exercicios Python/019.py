tempoViagem = float(input("Digite o tempo de viagem: "))

velocidadeMedia = float(input("Digite a velocidade media: "))

distancia = tempoViagem * velocidadeMedia

litrosUsados = distancia / 12

print(f"Litros por KM {litrosUsados:.2f} km")