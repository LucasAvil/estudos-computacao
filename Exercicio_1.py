import random

print("Jogo Jokenpo!")

opcoes = ["Pedra", "Papel", "Tesoura"]

jogador = str(input("Escolha entre Pedra, Papel ou Tesoura: ").capitalize())

if jogador not in opcoes:
    print("Escolha errada.")
else:
    pc = random.choice(opcoes)

    print("O computador escolheu:", pc)

    if jogador == pc:
        print("Empate!")
    elif jogador == "Pedra":
        if pc == "Tesoura":
            print("Você venceu!")
        else:
            print("O seu adversario venceu!")
    elif jogador == "Papel":
        if pc == "Pedra":
            print("Você venceu!")
        else:
            print("O seu adversario venceu!")
    elif jogador == "Tesoura":
        if pc == "Papel":
            print("Você venceu!")
        else:
            print("O seu adversario venceu!")