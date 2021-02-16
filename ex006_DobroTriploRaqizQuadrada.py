#Faça um programa que leia um numero e mostre o seu dobro, triplo e raiz

num=int(input('Digite um numero: '))

print('Analisando o valor {}.O dobro é {}.Triplo é {}.A raiz quadrada é {}'.format(num,(num*2),(num*3),pow(num,(1/2))))