import random 
digitadas = []
chances = 6
print ('-=' * 20)
print('         JOGO DA FORCA')
print ('-=' * 20)

palavras_secretas = []
with open ("Palavras.txt", "r") as palavra_arquivo:
    palavras_secretas.append(palavra_arquivo.readline())
    
palavra_secreta = random.choice(palavras_secretas)

while digitadas not in palavra_secreta:

    while chances > 0:
        tentativa = str(input('digite uma letra: ').lower().strip())
        digitadas.append(tentativa)
        if len(tentativa) > 1:
            print('apenas uma letra por vez')
            continue
        if tentativa not in palavra_secreta:
            print(f'ERRROOU, {tentativa} não está na palavra')
            chances -= 1
            continue
        if tentativa in palavra_secreta:
            print(f'boa, acertou uma letra, ')
        
