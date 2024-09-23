aluno = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a primeira nota 1: "))

note2 = float(input("Digite a segunda nota 2: "))

note3 = float(input("Digite a segunda nota 3: "))

note4 = float(input("Digite a segunda nota 4: "))

media = (nota1 + note2 + note3 + note4) / 4

if media < 5:
    conceito = 'D'
    print(f"aluno: {aluno} \nMedia: {media:.2f} \nConceito: {conceito}")
elif media < 7:
    conceito = 'C'
    print(f"aluno: {aluno} \nMedia: {media:.2f} \nConceito: {conceito}")
elif media < 9:
    conceito = 'B'
    print(f"aluno: {aluno} \nMedia: {media:.2f} \nConceito: {conceito}")
elif media <= 10:
    conceito = 'A'
    print(f"aluno: {aluno} \nMedia: {media:.2f} \nConceito: {conceito}")
else:
    print("Media invalida: ")





