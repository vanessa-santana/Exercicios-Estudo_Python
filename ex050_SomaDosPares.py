# Desenvolva um programa que leia seis números inteiros e 
# mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma=0
cont=0
contPar=0

for i in range(1,7):
    num=int(input('Digite um {}° num inteiro: '.format(i)))
    cont+=1
    if num %2==0:
        soma+=num
        contPar+=1
    else:
        next
print('Informou {} numeros, sendo {} numeros pares e a soma destes é {}'.format(cont,contPar,soma))
    
