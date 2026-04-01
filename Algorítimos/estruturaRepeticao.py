# for (for i in lista)
# while (while true ou while i == true)
#
#########
#mult = 1
#lista = [2, 5, 10, 3]
#for numeros in lista:
#   mult *= numeros
#   
#print(mult)
##########
#num = int(input('digite um numero: '))
#for i in range (1, 11):
#    mult = i * num
#    print(mult)
##########
#lista_par = []
#lista_impar = []
#for i in range (1,16):
#    if i % 2 == 0:
#        lista_par.append(i)
#    else:
#        lista_impar.append(i)
#print(f'os pares sao {lista_par} e os impares {lista_impar}')
########## 
#num1 = int(input('digite o primeiro numero: '))
#num2 = int(input('digite o segundo '))
#
#for i in range((num1 + 1), num2):
#    print(i)
###########
#pares = 0
#soma = 0
#for i in range(1, 101):
#    if i % 2 == 0:
#        pares += 1
#        print(i)
#        soma += i
#print(f'a soma deu {soma} e tem {pares} numeros pares')
############
palavra = str(input('Digite uma palavra: ').strip().lower())
vogal = 0
vogais = "aeiou"

# "Para cada letra na palavra:"
for letra in palavra:
    if letra in vogais:
        vogal += 1 # Forma mais curta de escrever vogal = vogal + 1

print(f"A palavra tem {vogal} vogais.")
print('bananas')