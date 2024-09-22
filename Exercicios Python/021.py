tempoSegundos = int(input('tempo em segundos: '))


segundos = tempoSegundos % 60
minutos = tempoSegundos / 60
horas = tempoSegundos / 3600

print(f"{horas:.0f}h {minutos:.0f}m {segundos:.0f}s")