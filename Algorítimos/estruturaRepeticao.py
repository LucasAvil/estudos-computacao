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
novamente = 'S'
while novamente == 'S':
    
    menu = int(input('=== Calculadora === \n 1 - Soma \n 2 - Subtração \n 3 - Divisão \n 4 - Multiplicação \n 0 - Sair \n').strip())
    if menu in [0, 1, 2, 3, 4]:
        if menu == 0:
            break    
        num1 = float(input('Digite o primeiro numero: '))
        num2 = float(input('Digite o segundo numero: '))
        if menu == 1:
            print(f'A soma deu: {num1 + num2}')
        elif menu == 2:
            print(f'A subtração deu: {num1 - num2}')
        elif menu == 3:
            print(f'A divisão deu: {num1 / num2}')        
        elif menu == 4:
            print(f'A multiplicação deu: {num1 * num2}')
        novamente = str(input('Quer fazer um novo calculo? (s/n)').capitalize().strip())
    else:
        novamente = str(input('Opção inválida, quer tentar novamente? (s/n)').capitalize().strip())
        
    
    while novamente not in ['S', 'N']:
        novamente = str(input('Você escreveu algo errado, quer tentar novamente? (s/n)').capitalize().strip())
        
print('Calculadora encerrada')

        
        