'''Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes '''

print('-=-' *20)
print('Analisador de triangulos')
print('-=-' *20)
lado1=float(input('Digite o primeiro segmento: '))
lado2=float(input('Digite o segundo segmento: '))
lado3=float(input('Digite o terceiro segmento: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado1:
    print('Os segmentos podem formar um triangulo!',end=(''))
    if lado1==lado2==lado3:
        print ('Lados {}, {}, {} formam um triangulo equilatero'.format(lado1,lado2,lado3))
    elif lado1!=lado2!=lado3!=lado1:
        print ('Lados {}, {}, {} formam um triangulo escaleno'.format(lado1,lado2,lado3))
    else:
        print ('Lados {}, {}, {} formam um triangulo isósceles'.format(lado1,lado2,lado3))
else:
    print('Não podem formar um triangulo')