#Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# alcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia=float(input('Digite uma distancia de viagem (km)?'))

if distancia <= 200:
    preco=distancia*0.50
    print('Para distancia de {}, o valor da passagem é de R${:.2f}'.format(distancia,preco))
else:
    preco=distancia*0.45
    print('Para distancia de {}, o valor da passagem é de R${:.2f}'.format(distancia,preco))

#Outro modo
distancia=float(input('Digite uma distancia de viagem (km)?'))
preco=distancia*0.50 if distancia <=200 else distancia * 0.45
print('Para distancia de {}, o valor da passagem é de R${:.2f}'.format(distancia,preco))