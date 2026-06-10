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
#import random
#loja = [
#    {"nome": "Facão", "dano": 30, "custo": 25, "descricao": "Corta o inimigo com uma faconada!!"},
#    {"nome": "Cajado", "dano": 45, "custo": 55, "descricao": "Atinge os inimigos com um ataque mágico!"},
#    {"nome": "Arco", "dano": 40, "custo": 40, "descricao": "Atinge os inimigos a distância com uma flecha!"},
#    {"nome": "Bodoque", "dano": 35, "custo": 35, "descricao": "Joga uma pedra na cabeça do adversário! útil para matar passarinhos!"},
#    {"nome": "Poção", "dano": 40, "custo": 15, "descricao": "Cura em 40 de Hp, tem gosto de morango"}
#
#
#]
#print('-='*20)
#print('                 LOJA')
#print('-='*20)
#itens_sorteados = random.sample(loja, 3)
#
#for item in itens_sorteados:
#    print(f"{item['nome']:<10} ${item['custo']:<5} {item['dano']}HP    {item['descricao']}")
# ==============================================================================
# ATIVIDADE 01 - Lusa
# ============================================================================== 
#for item in itens_sorteados:
#    print(f"{item['nome']:<10} ${item['custo']:<5} {item['dano']}HP    {item['descricao']}")
#x = 1
#while True:
#    try:
#        qnt_nomes = int(input("digite a quantidade de nomes: "))
#        lista_nomes = []
#        if qnt_nomes < 0:
#            print("numeros negativos sao invalidos!!")
#           continue
#        for i in range (qnt_nomes):
#            nome = str(input(f'digite o nome de numero {i + 1}: '))
#            lista_nomes.append(nome)
#        break
#    except:
#        ValueError
#        print("valor invalido!")
#
#lista_nomes.reverse()
#for nome in lista_nomes:
#    print(f'{x} - {nome}')
#    x += 1
#    
#excl = int(input("digite o numero do nome que você quer apagar: "))
#x = 1
#lista_nomes.pop(excl - 1)
#
#for nome in lista_nomes:
#    print(f'{x} - {nome}')
#    x += 1

# ==============================================================================
# ATIVIDADE 02 - Lusa
# ============================================================================== 
#banco_dados = []
#
#dado_1 = {
#    'nome': str(input('Digite seu nome: ')),
#    'sobrenome': input('digite o seu sobrenome: '),
#    'data_nascimento': input('digite sua data de nascimento: '),
#    'telefones': [input('digite o primeiro telefone: '), input('digite o segundo telefone: ')],
#    'endereco': {'rua': input('digite a sua rua: '), 'bairro': input('digite o seu bairro: '), 'cidade': input('digite a sua cidade: ')}
#        }
#dado_2 = {
#    'nome': str(input('Digite seu nome: ')),
#   'sobrenome': input('digite o seu sobrenome: '),
#    'data_nascimento': input('digite sua data de nascimento: '),
#    'telefones': [input('digite o primeiro telefone: '), input('digite o segundo telefone: ')],
#    'endereco': {'rua': input('digite a sua rua: '), 'bairro': input('digite o seu bairro: '), 'cidade': input('digite a sua cidade: ')}
#        }
#
#dado_3 = {
#    'nome': str(input('Digite seu nome: ')),
#    'sobrenome': input('digite o seu sobrenome: '),
#    'data_nascimento': input('digite sua data de nascimento: '),
#    'telefones': [input('digite o primeiro telefone: '), input('digite o segundo telefone: ')],
#    'endereco': {'rua': input('digite a sua rua: '), 'bairro': input('digite o seu bairro: '), 'cidade': input('digite a sua cidade: ')}
#        }
#
#banco_dados.append(dado_1)
#banco_dados.append(dado_2)
#banco_dados.append(dado_3)
#
#print(banco_dados)

# ==============================================================================
# ATIVIDADE 03 - Lusa
# ============================================================================== 
#sum - soma
#max - maior valor
#min - menor valor
#map - recebe dois parametros, o primeiro é a lista e a segunda é o lambda (função anonima) - passa de valor em valor e tira o valor que nao precisa
#abs - absoluto (tira o negativo)
#valores = [1, 10, -5, 13, 2, 1]
#pares = filter(lambda a: a%2==0, valores)
#print(sum(pares))
# ==============================================================================
# ATIVIDADE 04 - Lusa
# ============================================================================== 
# def validacao(valor):
#     if valor <= 10 and valor >= 1:
#         return True

# def converter(valor):
#     return int(valor)
    

# def solicitar_entrada(msg, validador, conversor):
#     while True:
#         valor = input(msg)
#         try:
#             valor = conversor(valor)
#             if validador(valor):
#                 break
#         except:
#             pass
    
#         print('Valor inválido!!. Informe novamente')
#     return valor

# vlr_1 = solicitar_entrada("informe o primeiro valor: ", validacao, converter)

# print(vlr_1)
# ==============================================================================
# ATIVIDADE 04 - dicionários
# ============================================================================== 
# categorias = {}
# while True:
#     prod = input("Digite os valores: ")
    
#     if ";;" in prod:
#         print("Encerrando")
#         break

#     prod_separado = prod.split(';')

#     if prod_separado[1] not in categorias:
#         categorias[prod_separado[1]] = int(prod_separado[2])
        
#     else:
#         categorias[prod_separado[1]] += int(prod_separado[2])

#     print("Produtos adicionados")

# print(categorias)

# ==============================================================================
# ATIVIDADE 05 - dicionários
# ============================================================================== 
# medias = {}

# while True:
#     nome = (input("Digite o nome do estudante: ")) 
#     nota = float(input("Digite a nota: "))

#     medias[nome] = nota

#     sair = input("Deseja sair? (S/N) ").strip().capitalize()

#     for x, y in medias.items():
#         if y < 6:
#             del x
    
#     if sair == 'S':
#         break
    

# print(medias)

# ==============================================================================
# ATIVIDADE 06 - dicionários
# ============================================================================== 
# nomes = []
# while True:
#     entrada = input("digite um nome: ").upper()

#     if entrada == 'STOP':
#         break
    
#     nomes.append(entrada)

# busca = input("digite a string de busca: ").upper()

# for n in nomes:
#     if busca in n:
#         print(n)

# ==============================================================================
# ATIVIDADE 07 - dicionários
# ============================================================================== 
# lista = []
# while True:
#     numero = int(input("digite um numero"))

#     lista.append(numero)
#     lista_sem_rep = list(dict.fromkeys(lista))
#     parar = input("deseja parar? (S/N):  ").upper()

#     if parar == 'S':
#         break

# print(lista_sem_rep)
# ==============================================================================
# ATIVIDADE 01 - funções
# ============================================================================== 
# valores = [10, 5, 12.5, 7.5]
# def media(valor):
#     return sum(valor) / len(valor)

# def maior_menor(valor):
#     return (max(valor), min(valor))

# def amplitude(valor):
#     return max(valor) - min(valor)

# print(media(valores))
# print(maior_menor(valores))
# print(amplitude(valores))
# ==============================================================================
# ATIVIDADE 02 - funções
# ============================================================================== 
# def nota_valida(n):
#     return 10 <= n and n >= 0

# def normalizar_nota(n):
#     return max(0, min(10, n))

# def media_notas(notas):
#     return sum(notas) / len(notas)

# notas = [8, 12, -1, 6.5]
# print([normalizar_nota(n) for n in notas])
# print(media_notas(notas))
# ==============================================================================
# ATIVIDADE 03 - funções
# ============================================================================== 
# def celsius_para_farenheit(c):
#     f = (9/5) * c + 32
#     return f

# def farenheit_para_celsius(f):
#     c = (5/9) * (f-32)
#     return c

# def converter_temperaturas(valores, origem):
#     if origem == 'C':
#         return [celsius_para_farenheit(i) for i in valores]
#     elif origem == 'F':
#         return [farenheit_para_celsius(i) for i in valores]
    
# print(celsius_para_farenheit(0))
# print(farenheit_para_celsius(212))
# print(converter_temperaturas([0, 10, 20], 'C'))
# ==============================================================================
# ATIVIDADE 04 - funções
# ============================================================================== 
# def limpar_texto(s):
#     return (s.strip().lower().replace(" ", ""))

# def contar_vogais(s):
#     dicio_vogais = {}
#     for i in limpar_texto(s):
#         if i in 'aeiou':
#             if i in dicio_vogais:
#                 dicio_vogais[i] += 1
#             else:
#                 dicio_vogais[i] = 1
#     return dicio_vogais

# def eh_palindromo(s):
#     s = limpar_texto(s)
#     invert = s[::-1]
#     return s == invert
    
# print(limpar_texto("        Oi Mundo       "))
# print(contar_vogais("Abacate"))
# print(eh_palindromo("Socorram me subi no onibus em Marrocos")) 
# ==============================================================================
# ATIVIDADE 05 - funções
# ============================================================================== 
# def inserir_ordenado(ordenada, x):
#     for i in range (len(ordenada)):
#         if ordenada[i] > x:
#             ordenada.insert(i, x)
#             return ordenada
#     ordenada.append(x)
#     return ordenada

# def ordenar(valores):
#     lista = []
#     for i in valores:
#         lista = inserir_ordenado(lista, i)
#     return lista

# def mediana(valores):
#     lista = ordenar(valores)
#     n = len(lista)
#     meio = n // 2
#     if n %2==0:
#         centro = lista[meio-1]
#         centro2 = lista[meio]
#         return (centro + centro2) / 2
#     else:
#         return lista[meio]


# print (inserir_ordenado([1, 2, 3, 10, 11], 12))
# print(ordenar([3, 1, 2]))
# print(mediana([10, 2, 8]))
# print(mediana([10, 2, 8, 4]))
# ==============================================================================
# ATIVIDADE 06 - funções
# ============================================================================== 
# def  subtotal_item(preco, qtd):
#     return preco * qtd
# def total_compra(itens):
#     soma = 0
#     for i in itens:
#             if i[1] < 0 or i[2] < 0:
#                  return None
            
#             soma += subtotal_item(i[1], i[2])
#     return soma

# def aplicar_desconto(total, percentual):
#      desconto = total * percentual / 100
#      return total - desconto

# itens = [('feijao', 6.5, 2), ('farinha', 7.0, 1)]
# print(total_compra(itens)) 
# print(aplicar_desconto(20.0, 10))
# ==============================================================================
# ATIVIDADE 07 - funções
# ==============================================================================
# def eh_primo(n):
#     if n <= 1:
#         return False
#     limite = int(n ** 0.5) + 1

#     for i in range (2, limite):
#         if n % i == 0:
#             return False
#     return True

# def proximo_primo(n):

#     while eh_primo(n) == False:
#         n += 1
    
#     return n

# def listar_primos(inicio, fim):
#     lista = []
#     for i in range (inicio, fim + 1):
#         if eh_primo(i):

#             lista.append(i)

#     return lista
        
# print(eh_primo(2))
# print(eh_primo(21))
# print(proximo_primo(22))
# print(listar_primos(10, 20))
# ==============================================================================
# ATIVIDADE 08 - funções
# # ==============================================================================
# def proximo_collatz(n):
#     if n % 2 == 0:
#         n = n//2
#     else:
#         n = 3 * n + 1
#     return n

# def sequencia_collatz(n):
#     lista = [n]
#     while n != 1:
#         n = proximo_collatz(n)
#         lista.append(n)

#     return lista

# def comprimento_collatz(n):
#     return len(sequencia_collatz(n))

# print(proximo_collatz(6))
# print(sequencia_collatz(6))
# print(comprimento_collatz(6))
# ==============================================================================
# ATIVIDADE 09 - funções
# ==============================================================================
# def eh_matriz_retangular(m):
#     if m == []:
#         return False
#     padrao = len(m[0])
#     for i in range (len(m)):
#         if len(m[i]) != padrao:
#             return False
#     return True

# def soma_linhas(m):
#     if eh_matriz_retangular(m) == False:
#         return None
#     soma = []
#     for i in range(len(m)):
#         soma.append(sum(m[i]))
#     return soma

# def soma_colunas(m):
#     if eh_matriz_retangular(m) == False:
#         return None
#     soma = []
#     for i in range (len(m[0])):
#         soma.append(m[0][i] + m[1][i])
#     return soma


# m = [[1, 2, 3], [4, 5, 6,]]

# print(eh_matriz_retangular(m))
# print(soma_linhas(m))
# print(soma_colunas(m))
# ==============================================================================
# ATIVIDADE 10 - funções
# ==============================================================================
# def parse_venda(linha):
#     partes = linha.split(';')
#     return partes[0].strip(), int(partes[1])

# def consolidar_vendas(linhas):
#     dic = {}
#     for i in linhas:
#         try:
#             partes = parse_venda(i)
#             produto = partes[0]
#             quantidade = partes[1]
#             if produto in dic:
#                 dic[produto] += quantidade
#             else:
#                 dic[produto] = quantidade
#         except (IndexError, ValueError):
#             continue
#     return dic

# def listar_consolidado(consolidado):
#     return sorted(consolidado.items())
        
        
# linhas = ["arroz;2", " feijao;1", "arroz;3", "invalido", "carne;X"]
# consolidado = consolidar_vendas(linhas)
# print(consolidado)
# print(listar_consolidado(consolidado))
# ==============================================================================
# ATIVIDADE 1 - prova teste1
# ==============================================================================
        