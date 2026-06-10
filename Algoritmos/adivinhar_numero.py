import random
jogador = 0
resposta = 'S'
pontuacao = 0
print('| Adivinhe o número! |')
while resposta == 'S':
    tentativas = int(input('quantas tentativas quer ter? ').strip())
    num = random.randint(1, 10)
    
    while tentativas > 0:

        jogador = int(input(f"adivinhe um numero de 1 a 10, você tem {tentativas} tentativas "))
        if jogador not in range(1, 10):
            jogador = int(input(f"ei ei ei, o número que tu botou nao é válido, é entre 1 e 10!, escreva outro: "))
        if jogador < num:
            print(f'\n Mais \n ')
        elif jogador > num:
            print(f'\n Menos \n')
        tentativas = tentativas - 1

        if num == jogador:
            break

    if num == jogador:
        if tentativas >= 1:
            resposta = str(input(f'você ganhou! ainda sobraram {tentativas} tentativas, jogar novamente? (s/n) ').capitalize().strip())
        else:
            resposta = str(input(f'você ganhou na última tentativa! gosta de jogar arriscado né? jogar novamente? (s/n) ').capitalize().strip())
            
    else:
        resposta = str(input(f'Você perdeu!  o numero era {num}!! jogar novamente? (s/n) ').capitalize().strip())
    while resposta not in ['S', 'N']:
        resposta = str(input('você digitou algo errado, tentar novamente?  (s/n) ').capitalize().strip())
    pontuacao = pontuacao + 1
    #print(f'Tentativas: {tentativas} \nAcertos: {pontuacao}')
    

print('Jogo encerrado!')

