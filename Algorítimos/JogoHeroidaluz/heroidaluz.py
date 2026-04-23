#Originalmente atividade 5 (extra) da matéria de algorítmos, última da última aula com o prof dreslei

import random
import time

class entidade:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100
        self.pocoes = 3
        self.defendendo = False
    
    def atacar(self, alvo):
        dano = 20
        if alvo.defendendo:
            dano = dano // 2
            print(f'{alvo.nome} defendeu! dano reduzido pela metade!\n')
        else:
            print(f'OPAAA {alvo.nome} sofreu um ataque em cheio!!')
            print(f'-{dano}HP \n')
        alvo.vida -= dano

    def defender(self):
        self.defendendo = True
        print(f'{self.nome} levantou o escudo!')

    def curar(self):
        if self.pocoes > 0:
            self.pocoes -= 1
            self.vida += 40
            print(f'{self.nome} curou sua vida em 40!')
        else:
            print(f'{self.nome} tentou usar uma poção mas estava sem nenhuma! que burrinho!')

    def inventario(self):
        print(f'-='*20, '\n         INVENTÁRIO')
        print(f'Vida: {self.vida}HP\nPoções: {self.pocoes}\n')
        print(f'LV: {lvl_tot}\nXP: {xp_tot}XP\nOuro: {ouro_tot}$')

    
def sortear_inimigo(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

        nomes_limpos = []
        for linha in linhas:
            nomes_limpos.append(linha.strip())
        nome_escolhido = random.choice(nomes_limpos)
        return nome_escolhido
    
novamente = 'S'
ouro_tot = 0
xp_tot = 0
lvl_tot = 1
print("-="*20)
print("             O HERÓI DA LUZ")
print('-='*20)

jogador = entidade(str(input('DIGITE O NOME DO HERÓI DA LUZ: ').strip()))

while novamente == 'S':
    nome_sorteado = sortear_inimigo("Algorítimos\JogoHeroidaluz\inimigos.txt")
    inimigo = entidade(nome_sorteado)

    jogador.defendendo = False
    print(f'OPA, INIMIGO A VISTA, UM {inimigo.nome} APARECEU!!')
    time.sleep(1)
    while jogador.vida > 0 and inimigo.vida > 0:
        print(f'SELECIONE UMA OPÇÃO: \n 1-Ataque\n 2-Defesa \n 3-Cura \n 4-Inventário')
        escolha_jog = int(input(':').strip())
        while escolha_jog not in [1, 2, 3, 4]:
            print('Escolha inválida!\n SELECIONE UMA OPÇÃO: \n 1-Ataque\n 2-Defesa \n 3-Cura \n 4-Inventário')
            escolha_jog = int(input(':'))

        if escolha_jog == 4:
            jogador.inventario()
            print(f'SELECIONE UMA OPÇÃO: \n 1-Ataque\n 2-Defesa \n 3-Cura \n 4-Inventário')
            escolha_jog = int(input(':').strip())
        if escolha_jog == 1:
            jogador.atacar(inimigo)
        elif escolha_jog == 2:
            jogador.defender()
        elif escolha_jog == 3:
            jogador.curar()
        time.sleep(1)
        inimigo.defendendo = False
        escolha_op = random.randint(1, 3)
        if escolha_op == 1:
            inimigo.atacar(jogador)
        elif escolha_op == 2:
            inimigo.defender()
        elif escolha_op == 3:
            inimigo.curar()
        time.sleep(1)
        print('-='*20)
        print(f'{jogador.nome}: {jogador.vida} HP | Poções: {jogador.pocoes}')
        print(f'{inimigo.nome}: {inimigo.vida} HP | Poções: {inimigo.pocoes}')
        print('-='*20)

    xp = random.randint(12, 60)
    ouro =  random.randint(20, 50)

    if inimigo.vida <= 0:
        print(f'Meu deus! Você venceu o {inimigo.nome}, muito bem! ganhou {xp}XP e {ouro}$')
        ouro_tot += ouro
        xp_tot += xp
        if xp_tot == 100:
            xp_tot -= 100
            lvl_tot += 1
            print(f'Parabéns, {jogador.nome} você subiu para o nível {lvl_tot}!')
        time.sleep(1)
    else: 
        print(f'Nãoooo você morreuuu!!')
    
