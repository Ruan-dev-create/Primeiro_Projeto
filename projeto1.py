from random import randint

computador = randint(0, 50)

chance = int(input('São quantas tentativas?'))
tentativas = 0

while chance != tentativas:
    print(computador)
    usuario = int(input('Digite o valor: '))
    tentativas += 1

    if usuario < computador: 
        print('É maior...')
        print('-=' * 20)

    elif usuario > computador:
        print('É menor...')
        print('-=' * 20)
    
    elif usuario == computador:
        print('Você acertou o número')
        print(f'O número sorteado foi o {computador}')
        break

    if tentativas > chance:
        break

if usuario != computador:
    print('Suas tentativas acabaram. Tente novamente!')
    print(f'O número sorteado foi o {computador}')

print('-=' * 30)

