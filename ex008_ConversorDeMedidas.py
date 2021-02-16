#Escreva um programa que leia um vetor em metros e a exiba converitdo em centimetro e milimetros

medida=float(input('Digite a medida em metros: '))
cm=medida*100
ml=medida*1000
print('A medida de {} metros corresponde a:\nCentimetro:{:.0f}.\nMilimetro é {:.0f}.'.format(medida,cm,ml))