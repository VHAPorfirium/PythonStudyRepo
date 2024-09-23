nome = input('Qual o seu nome? ')

idade = int(input('Qual a sua idade? '))

if idade < 18:
    print(f'{nome} é menor de idade. ')
else:
    print(f'{nome} é maior de idade. ')