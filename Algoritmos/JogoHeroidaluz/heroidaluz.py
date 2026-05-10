#Originalmente atividade 5 (extra) da matéria de algorítmos, última da última aula com o prof dreslei

import random
import time

itens_loja = [
    {"nome": "Facão", "dano": 30, "custo": 25, "descricao": "Corta o inimigo com uma faconada!!"},
    {"nome": "Cajado", "dano": 45, "custo": 55, "descricao": "Atinge os inimigos com um ataque mágico!"},
    {"nome": "Arco", "dano": 40, "custo": 40, "descricao": "Atinge os inimigos a distância com uma flecha!"},
    {"nome": "Bodoque", "dano": 35, "custo": 35, "descricao": "Joga uma pedra na cabeça do adversário! útil para matar passarinhos!"},
    {"nome": "Poção", "dano": 40, "custo": 15, "descricao": "Cura em 40 de Hp, tem gosto de morango"}
    ]
inv = [
    {"nome": "punho", "dano": 20, "descricao": "Par de punhos laváveis e levemente fortes"}
]
class entidade:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100
        self.pocoes = 3
        self.defendendo = False
        self.dano = 20
        if nome in ["Rato mutante", "Mosca atômica", "Formiga atômica", "Amalgamação", "Marcelo maligno"]:
            self.vida = 200
            self.pocoes = 2
            self.dano = 30
            inimigo_forte = 1
        if nome == 'debug':
            self.dano = 80
            self.vida = 1000
            self.pocoes = 10
    
    def atacar(self, alvo):
        if alvo.defendendo:
            self.dano = self.dano // 2
            print(f'{alvo.nome} defendeu! dano reduzido pela metade!\n')
            alvo.defendendo = False
            self.dano = self.dano * 2
        else:
            print(f'OPAAA {alvo.nome} sofreu um ataque em cheio!!')
            print(f'-{self.dano}HP \n')
        if self.nome in ["Enguia", "Mosca atômica", "Amalgamação"]:
            chance = random.randint(1, 5)
            if chance == 1:
                paralisia = True
                print(f'{self.nome} te paralisou! vai ficar 1 turno esperando!')
        alvo.vida -= self.dano

    def defender(self):
        if self.defendendo == False:
            self.defendendo = True
            print(f'{self.nome} levantou o escudo!')
        else:
            print(f'{self.nome} tentou defender enquanto já defendia, nada alterado!')

    def curar(self):
        if self.pocoes > 0:
            print(f'{self.nome} curou sua vida em 40!')
            if self.vida < 100:
                self.pocoes -= 1
                self.vida += 40
                if self.vida > 100:
                    self.vida = 100
            else:
                print(f'{self.nome} tentou se curar mas a sua vida já estava cheia!')
        else:
            print(f'{self.nome} tentou se curar mas estava sem poções!')
        

    def inventario(self):
        print(f'-='*20, '\n         INVENTÁRIO')
        print(f'Vida: {self.vida}HP\nPoções: {self.pocoes}\n')
        print(f'LV: {lvl_tot}\nXP: {xp_tot}XP\nOuro: {ouro_tot}$')
        print(f"Arma: {inv['nome']:<10} ${inv['custo']:<5} {inv['dano']}HP    {inv['descricao']}")
        print(f'-='*20)

    def checar(self, inimigo):
        print(f'-='*20, '\n         ',inimigo.nome)
        print(f'Ataque: {inimigo.dano} Vida: {inimigo.vida} Poções: {inimigo.pocoes}')
        if inimigo.nome in ["Rato mutante", "Mosca atômica", "Formiga atômica", "Amalgamação", "Marcelo maligno"]:
            if inimigo.nome in ["Enguia", "Mosca atômica", "Amalgamação"]:
                print(f'Habilidade especial: 20% de chance no ataque de te paralisar por um turno')
    
        
    def loja(self):
        i = 1
        print('-='*20)
        print('                 LOJA')
        print('-='*20)
        itens_sorteados = random.sample(itens_loja, 3)
        
        for item in itens_sorteados:
            print(f"{i} - {item['nome']:<10} ${item['custo']:<5} {item['dano']}HP    {item['descricao']}")
            i += 1
        print(f"4 - Sair")
        selecionar_item_loja = int(input("Selecione o numero do item que deseja comprar: ").strip())
        while selecionar_item_loja not in [1, 2, 3, 4]:
            print("Opção inválida!")
            selecionar_item_loja = int(input("Selecione o numero do item que deseja comprar: ").strip())
        for item in itens_sorteados:
            if selecionar_item_loja == itens_sorteados[item] - 1 and itens_sorteados[selecionar_item_loja - 1]['nome'] != 'Poção' :
                inv.pop[0]
                inv.append[itens_sorteados[item]]
            elif selecionar_item_loja == 4:
                break
            if itens_sorteados[selecionar_item_loja - 1]['nome'] == 'Poção':
                self.pocoes += 1
    

def sortear_inimigo(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

        nomes_limpos = []
        for linha in linhas:
            nomes_limpos.append(linha.strip())
        nome_escolhido = random.choice(nomes_limpos)
        return nome_escolhido

newgame = 'S'
while newgame == 'S':
    inimigo_forte = 0
    novamente = 'S'
    ouro_tot = 0
    xp_tot = 0
    lvl_tot = 1
    paralisia = False
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
            if paralisia == False:
                print(f'SELECIONE UMA OPÇÃO: \n 1-Ataque\n 2-Defesa \n 3-Cura \n 4-Inventário\n 5-Checar inimigo')
                escolha_jog = int(input(':').strip())
                while escolha_jog not in [1, 2, 3, 4, 5]:
                    print('Escolha inválida!\n SELECIONE UMA OPÇÃO: \n 1-Ataque\n 2-Defesa \n 3-Cura \n 4-Inventário\n 5-Checar inimigo')
                    escolha_jog = int(input(':'))
                while escolha_jog in [4, 5]:
                    if escolha_jog == 4:
                        jogador.inventario()
                    if escolha_jog == 5:
                        jogador.checar(inimigo)
                    print(f'SELECIONE UMA OPÇÃO: \n 1-Ataque\n 2-Defesa \n 3-Cura \n 4-Inventário \n 5-Checar inimigo')
                    escolha_jog = int(input(':').strip())
                if escolha_jog == 1:
                    jogador.atacar(inimigo)
                elif escolha_jog == 2:
                    jogador.defender()
                elif escolha_jog == 3:
                    jogador.curar()
                paralisia = False
            time.sleep(1)
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
        
        if inimigo_forte == 1:
            xp = random.randint(70, 147)
            ouro =  random.randint(67, 115)
        else:
            xp = random.randint(12, 60)
            ouro =  random.randint(20, 50)

        if inimigo.vida <= 0:
            print(f'Meu deus! Você venceu o {inimigo.nome}, muito bem! ganhou {xp}XP e {ouro}$')
            ouro_tot += ouro
            xp_tot += xp
            if xp_tot >= 100:
                xp_tot -= 100
                lvl_tot += 1
                print(f'Parabéns, {jogador.nome} você subiu para o nível {lvl_tot}!')

            time.sleep(1)
            novamente = str(input('Jogar novamente? (S/N)').capitalize().strip())
            while novamente not in ['S', 'N']:
                print('Opção inválida!')
                novamente = str(input('Jogar novamente? (S/N)').capitalize().strip())
            jogador.loja()
            
        else: 
            print(f'Nãoooo você morreuuu!!')
            break
    newgame = str(input('Quer começar um jogo novo? (S/N)').capitalize().strip())
    while newgame not in ['S', 'N']:
        print('Opção inválida!')
        newgame = str(input('Quer criar um herói novo? (S/N)').capitalize().strip())
print('Jogo encerrado...')
    
