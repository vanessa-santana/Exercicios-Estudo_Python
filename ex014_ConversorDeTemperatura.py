#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temp=(float(input('Digite a temperatura em Celsius: ')))
fahrenheit= (temp*1.8)+32

print('O valor da temp é de {:.2f}°C e convertendo para Fahrenheit {:.2f}°F'.format(temp,fahrenheit) )