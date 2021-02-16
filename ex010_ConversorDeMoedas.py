#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dolares ela pode comprar
#Considerando U$$1.00=3.27

moeda=float(input('Digite um valor em reais (separado por (.)):'))
print('R$ {:.2f} convertido em dolar é:\nU$$ {:.2f}'.format(moeda,(moeda/3.27)))