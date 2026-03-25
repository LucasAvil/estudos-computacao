import random
# Vai ficar com média 3
print('jokempo!!!')

opcoes = ["Pedra", "Papel", "Tesoura"]

jogador = str(input("escolha entre pedra papel ou tesoura: ").capitalize())

pc = random.choice(opcoes)

if pc == jogador:
    print('empate!!')
    
elif pc == "Pedra" and jogador == "Papel" or pc == "Papel" and jogador == "Tesoura" or pc == "Tesoura" and jogador == "Pedra":
    print('você ganhou!!')
    
elif pc == "Papel" and jogador == "Pedra" or jogador == "Papel" and pc == "Tesoura" or jogador == "Tesoura" and pc == "Pedra":
    print('voce perdeu!!')
    
print(f'a maquina usou {pc} e você usou {jogador}')
