import random
jogador = 0
print('JOGO DA ADIVINHACAO')
num = random.randint(1, 10)
while jogador != num:
    jogador = int(input('adivinhe um numero de 1 a 10 '))
    if jogador < num:
        print(f'muito pouco')
    elif jogador > num:
        print(f'subiu demais')
        
print('FEITO!!! ACERTOUUU')
