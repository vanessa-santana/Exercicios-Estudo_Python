#Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.

veloc=int(input('Digite a velocidade do carro: '))

if veloc > 80:
    print('MULTADO! Excedeu o limite que é de 80km/h')
    multa=(veloc-80)*7
    print('Deve pagar multa de R${:.2f}'.format(veloc,multa))
print('{}km/h. Tenha um bom dia e dirija com segurança'.format(veloc))