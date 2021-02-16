#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

contMaior=0
contMenor=0
for i in range (1,6):
    peso=float(input('Digite o peso da {}ª pessoa (kg): '.format(i)))
    if  peso==1:
        contMaior=peso
        contMenor=peso
    else: 
        if peso > contMaior:
            contMaior=peso
        if peso < contMenor:
            contMenor=peso

print('O maior peso é {}'.format(contMaior))
print('O menor peso é {}'.format(contMenor))

