#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('-=-' *20)
print('Analisador de triangulos')
print('-=-' *20)
lado1=float(input('Digite o primeiro segmento: '))
lado2=float(input('Digite o segundo segmento: '))
lado3=float(input('Digite o terceiro segmento: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado1:
    print('Os segmentos podem formar um triangulo!')
else:
    print('Não podem formar um triangulo')