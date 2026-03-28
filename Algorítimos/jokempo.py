import random

print('jokempo!!!')
vitoria = 0
partidas = 0
novamente = 'S'
opcoes = ["Pedra", "Papel", "Tesoura"]
while novamente == 'S':
    jogador = str(input("escolha entre pedra papel ou tesoura: ").capitalize().strip())

    pc = random.choice(opcoes)
    if jogador in opcoes:
        if pc == jogador:
            print('Empate!')
        elif pc == "Pedra" and jogador == "Papel" or pc == "Papel" and jogador == "Tesoura" or pc == "Tesoura" and jogador == "Pedra":
            print('Você ganhou!!')
            vitoria = vitoria + 1
        else:
            print('Você perdeu!')

        partidas = partidas + 1
        novamente = str(input(f'A máquina usou {pc} e você usou {jogador}, você deseja jogar novamente? s/n ').capitalize().strip())
        aproveitamento = (vitoria / partidas) * 100
        print(f'\nPontuação: {vitoria}\n Partidas: {partidas}\n Aproveitamento: {aproveitamento:.2f}% \n')

    else:
        novamente = str(input('você escreveu alguma coisa errada, deseja repetir? s/n ').capitalize().strip())
        if novamente == 'N':
            break
        elif novamente == 'S':
            continue
    while novamente not in ['S', 'N']:
        novamente = str(input('Opção inválida, gostaria de tentar novamente? s/n ').capitalize().strip())
        continue
print(f'Jogo encerrado! Obrigado por jogar!')

