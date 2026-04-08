import random 

digitadas = []
novamente = 'S'

print ('-=' * 20)
print('         JOGO DA FORCA')
print ('-=' * 20)

palavras_secretas = []
while novamente == 'S':
    chances = 6
    with open ("Algorítimos\jogoForca\Palavras.txt", "r") as palavra_arquivo:
        palavras_secretas = palavra_arquivo.read().splitlines()
        
    palavra_secreta = random.choice(palavras_secretas)
    palavraVisual = ['*'] * len(palavra_secreta)


    while chances > 0 and '*' in palavraVisual:
        tentativa = str(input('digite uma letra: ').lower().strip())
        if len(tentativa) > 1 and tentativa != palavra_secreta and len(tentativa) < 4:
            print('apenas uma letra por vez')
            continue
        if tentativa in digitadas:
            print('você ja digitou essa letra')
            continue
        elif tentativa not in palavra_secreta or tentativa != palavra_secreta and len(tentativa) >= 4:
            print(f'ERRROOU, {tentativa} não está na palavra')
            chances -= 1
        if tentativa == palavra_secreta:
            print('toma, foi direto, sem massagem')
            palavraVisual = tentativa
            break
        if tentativa in palavra_secreta:
            print(f'boa, acertou uma letra ')
            for i in range(len(palavra_secreta)):
                if tentativa == palavra_secreta[i]:
                    palavraVisual[i] = tentativa
        
            
        digitadas.append(tentativa)
        print(f'\n {''.join(palavraVisual)} \n Chances: {chances}\n')


    if '*' not in palavraVisual:
        print(f'ganhaste, a palavra era {palavra_secreta.upper()}!!')
    else:
        print(f'perdeu mano, a palavra era {palavra_secreta.upper()}!!')

    novamente = str(input('quer jogar novamente? (s/n) ').capitalize().strip())
    digitadas = []

    while novamente not in ['S', 'N']:
        novamente = str(input('gurizão, escreveu errado, quer tentar denovo? (s/n) ').capitalize().strip())
print('jogo encerrado, obrigado por jogar')