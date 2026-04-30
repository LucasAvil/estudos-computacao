# ==============================================================================
# ANOTAÇÕES GERAIS
# ==============================================================================
# for (for i in lista)
# while (while true ou while i == true)
#

# ==============================================================================
# ATIVIDADE 1 
# ==============================================================================
#mult = 1
#lista = [2, 5, 10, 3]
#for numeros in lista:
#   mult *= numeros
#   
#print(mult)

# ==============================================================================
# ATIVIDADE 2 
# ==============================================================================
#num = int(input('digite um numero: '))
#for i in range (1, 11):
#    mult = i * num
#    print(mult)

# ==============================================================================
# ATIVIDADE 3 
# ==============================================================================
#lista_par = []
#lista_impar = []
#for i in range (1,16):
#    if i % 2 == 0:
#        lista_par.append(i)
#    else:
#        lista_impar.append(i)
#print(f'os pares sao {lista_par} e os impares {lista_impar}')

# ==============================================================================
# ATIVIDADE 4 
# ==============================================================================
#num1 = int(input('digite o primeiro numero: '))
#num2 = int(input('digite o segundo '))
#if num1 == num2:
#   print('os dois numeros nao podem ser iguais')
#for i in range((num1 + 1), num2):
#    print(i)

# ==============================================================================
# ATIVIDADE 5 
# ==============================================================================
#pares = 0
#soma = 0
#for i in range(1, 101):
#    if i % 2 == 0:
#        pares += 1
#        print(i)
#        soma += i
#print(f'a soma deu {soma} e tem {pares} numeros pares')

# ==============================================================================
# ATIVIDADE 6 
# ==============================================================================
#palavra = str(input('Digite uma palavra: ').strip().lower())
#vogal = 0
#vogais = "aeiou"
#
#for letra in palavra:
#    if letra in vogais:
#        vogal += 1
#
#print(f"A palavra tem {vogal} vogais.")

# ==============================================================================
# ATIVIDADE 7 
# ==============================================================================
#reprovados = 0
#for i in range(4):
#    nota1 = float(input('digite a primeira nota: ').strip())
#    nota2 = float(input('digite a segunda nota: ').strip())
#    media = (nota1 + nota2) / 2
#    if media < 5:
#        reprovados += 1
#print(f'tivemos {reprovados} alunos reprovados')

# ==============================================================================
# ATIVIDADE 8 (PARTE 1 - Versão FOR)
# ==============================================================================
#for i in range(1, 5):
#    filho1 = int(input('digite a idade do primeiro filho: ').strip())
#    filho2 = int(input('digite a idade do segundo filho: ').strip())
#    soma = filho1 + filho2
#    print(f'a soma da idade do casal de numero {i} deu {soma}')

# ==============================================================================
# ATIVIDADE 8 (PARTE 2 - Versão WHILE)
# ==============================================================================
#casal = 0
#while casal != 4:
#    casal += 1
#    filho1 = int(input('digite a idade do primeiro filho: ').strip())
#    filho2 = int(input('digite a idade do segundo filho: ').strip())
#    soma = filho1 + filho2
#    print(f'a soma da idade do casal de numero {casal} deu {soma}')
# ==============================================================================
# ATIVIDADE 9
# ==============================================================================
#dias = int(input('quantos dias o carro ficou alugado? '))
#km = float(input('quantos km foram rodados? '))
#
#diaria = dias * 60
#kmPagar = 0.15 * km
#
#print(f' ---------------------------- \n Valor gasto com a diária do carro: {diaria} \n Valor gasto com Km rodado: {kmPagar} \n Valor total a pagar: {kmPagar + diaria}')
# ==============================================================================
# ATIVIDADE 9
# ==============================================================================
#novamente = 'S'
#while novamente == 'S':
#    
#    menu = int(input('=== Calculadora === \n 1 - Soma \n 2 - Subtração \n 3 - Divisão \n 4 - Multiplicação \n 0 - Sair \n').strip())
#    if menu in [0, 1, 2, 3, 4]:
#        if menu == 0:
#            break    
#        num1 = float(input('Digite o primeiro numero: '))
#        num2 = float(input('Digite o segundo numero: '))
#        if menu == 1:
#            print(f'A soma deu: {num1 + num2}')
#        elif menu == 2:
#            print(f'A subtração deu: {num1 - num2}')
#        elif menu == 3:
#            print(f'A divisão deu: {num1 / num2}')        
#        elif menu == 4:
#            print(f'A multiplicação deu: {num1 * num2}')
#        novamente = str(input('Quer fazer um novo calculo? (s/n)').capitalize().strip())
#    else:
#        novamente = str(input('Opção inválida, quer tentar novamente? (s/n)').capitalize().strip())
#        
#    
#    while novamente not in ['S', 'N']:
#        novamente = str(input('Você escreveu algo errado, quer tentar novamente? (s/n)').capitalize().strip())
#        
#print('Calculadora encerrada')
# ==============================================================================
# ATIVIDADE 10
# ==============================================================================
#st = 0
#val = 0
#vel = int(input("Selecione a velocidade desejada (300, 600 ou 1000 Mbps) ").strip())
#
#while vel not in [300, 600, 1000]:
#    vel = int(input("Digite uma opção válida (300, 600 ou 1000 Mbps)").strip())
#
#streaming = str(input("Deseja adicionar streaming? (S/N)").capitalize().strip())
#
#cli = float(input("É cliente a quantos meses? ").strip())
#
#if vel == 300:
#    val += 79.90
#   
#elif vel == 600:
#    val += 109.90
#
#elif vel == 1000:
#    val += 129.90
#
#if streaming == "S":
#    st = 19.90
#    val += 19.90
#
#if cli > 6:
#    val - val / 10
#
#
#print(f'Você selecionou o plano de {vel}Mb\nAdicional R${st} \n Desconto: Total: R${val / 10}\nR${val} ')
# ==============================================================================
# ATIVIDADE 11
# ==============================================================================
#mensal = float(input("digite o valor "))
#mes = int(input("digite a quantidade de meses: ").strip())
#saldo = 0
#for i in range (mes):
#    saldo += mensal
#    print(f'Mes {i+1}: Saldo acumulado = R${saldo}')
# ==============================================================================
# ATIVIDADE 12
# ==============================================================================    
#opcao = 0
#estoque = 10
#while opcao != 4:
#    
#    opcao = int(input('Escolha uma opcão\n1 - Adicionar unidades\n2 - Remover unidades\n3 - Exibir estoque\n4 - Sair\nDigite a opcão desejada: ').strip())
#    if opcao == 1:
#        quant = int(input('Quantas unidades deseja adicionar? ').strip())
#        estoque += quant
#        if estoque > 10 or estoque < 0:
#            print('Valor inválido! Estoque não pode ser maior que 10 ou menor que 0!')
#            estoque -= quant
#        else:    
#            print('\nUnidades adicionadas com sucesso.\n')
#        
#    
#    if opcao == 2:
#        quant = int(input('Quantas unidades deseja remover? ').strip())
#        estoque -= quant
#        if estoque > 10 or estoque < 0:
#            print('Valor inválido! Estoque não pode ser maior que 10 ou menor que 0!')
#            estoque += quant
#        else:
#            print('\nUnidades removidas com sucesso.\n')
#   
#    if opcao == 3:
#        print(f'Estoque: {estoque}')
#    
#    while opcao not in [1, 2, 3, 4]:
#        opcao = int(input('Opcão inválida! digite 1 para tentar novamente: ').strip())
#        continue
#print(f'Encerrando...')
# ==============================================================================
# ATIVIDADE 13
# ==============================================================================
#import random
#novamente = 'S'
#while novamente == 'S':
#    computador = random.randint(1,6)
#    jogador = random.randint(1,6)
#    while novamente not in ['S', 'N']:
#        novamente = str(input('Opção inválida deseja tentar novamente? (S/N) ').strip().capitalize())
#        
#    if computador == jogador:
#        print('EMPATE!')
#        novamente = str(input('Quer jogar novamente? (S/N) ').strip().capitalize())
#    elif computador > jogador:
#        print(f'\nComputador: {computador}\nJogador: {jogador}\nVocê perdeu!')
#        novamente = str(input('Quer jogar novamente? (S/N) ').strip().capitalize())
#    else:
#        print(f'\nComputador: {computador}\nJogador: {jogador}\nVocê ganhou!')
#        novamente = str(input('Quer jogar novamente? (S/N) ').strip().capitalize())
#
#print('Jogo encerrado!')        
# ==============================================================================
# ATIVIDADE 14
# ==============================================================================       
#continuada no arquivo "heroidaluz.py" por ser legal demais e receber mudanças no futuro
# ==============================================================================
# ATIVIDADE 15 -- Atividade de dicionarios feita por conta própria
# ============================================================================== 
import random
loja = [
    {"nome": "Facão", "dano": 30, "custo": 25, "descricao": "Corta o inimigo com uma faconada!!"},
    {"nome": "Cajado", "dano": 45, "custo": 55, "descricao": "Atinge os inimigos com um ataque mágico!"},
    {"nome": "Arco", "dano": 40, "custo": 40, "descricao": "Atinge os inimigos a distância com uma flecha!"},
    {"nome": "Bodoque", "dano": 35, "custo": 35, "descricao": "Joga uma pedra na cabeça do adversário! útil para matar passarinhos!"},
    {"nome": "Poção", "dano": 40, "custo": 15, "descricao": "Cura em 40 de Hp, tem gosto de morango"}


]
print('-='*20)
print('                 LOJA')
print('-='*20)
itens_sorteados = random.sample(loja, 3)

for item in itens_sorteados:
    print(f"{item['nome']:<10} ${item['custo']:<5} {item['dano']}HP    {item['descricao']}")


    
